import requests
import os
from time import localtime
from time import strftime
from re import findall
import urllib
import webbrowser
from urllib.request import urlopen

from bs4 import BeautifulSoup
from PIL import Image

def gs(i):#数字格式，不满3位前面补0
    if i>=100:
        return str(i)
    if i>=10:
        return '0'+str(i)
    return '00'+str(i)

def crop_img(img_dir):#切成长宽4：3
    im = Image.open(img_dir)
    img_w=im.size[0]
    img_h=im.size[1]
    if img_h/img_w<0.75:
        y1=0
        y2=img_h
        x1=(img_w-img_h*4/3)/2
        x2=img_w-x1
    elif img_h/img_w>0.75:
        x1=0
        x2=img_w
        y1=(img_h-img_w*3/4)/2
        y2=img_h-y1
    im.crop((x1, y1, x2, y2)).save(img_dir)

def download_img(img_dir,img_url):
    data = urlopen(img_url).read()#下载图片
    f = open(img_dir, "wb")
    f.write(data)
    f.close

work_path=['./html_index/html_yhyw/html_news/news_content','./html_index/html_tzgg/tzgg_content']
type_str=['yhyw','tzgg']

def change_index(news_type,folder_name,title):#改index内容
    index = BeautifulSoup(open('./index.html', encoding='utf-8'), 'html.parser')
    all=index.find('p', id=type_str[news_type]+'_title')
    pre_title=all.string
    all=index.find('a', id=type_str[news_type]+'_href') 
    pre_href=all['href']
    f=open('./index.html','r',encoding="utf-8")
    index=f.read().replace(pre_title,title)#改标题
    f.close()
    if news_type==0:
        new_href=work_path[0]+'/'+folder_name+'/'+folder_name+'.html'
    else:
        new_href=work_path[1]+'/html_'+folder_name+'/'+folder_name+'.html'
    index=index.replace(pre_href,new_href)#改链接
    f=open('./index.html','w',encoding="utf-8")
    f.write(index)
    f.close()

def empty_warn(i):
    print('!!!!!注意，滚轮第 '+ str(i)+' 张中旧标题为空，自动改变标题失败，请检查滚轮中标题并手动更改!!!!!' )

def check_cover_name(news_type):
    index = BeautifulSoup(open('./index.html', encoding='utf-8'), 'html.parser')
    cover_name=index.find('img', id=type_str[news_type]+'_cover')['src']
    if cover_name!='./index_material/'+type_str[news_type]+'_cover.jpg':
        print('!!!!!注意，请将index.html中的id为"'+type_str[news_type]+'_cover"的img标签的src改为:"./index_material/'+type_str[news_type]+'_cover.jpg",否则图片无法显示!!!!!')

def change_index_and_material(news_type,folder_name,title,cover_url):
    change_index(news_type,folder_name,title)
    download_img('./index_material/'+type_str[news_type]+'_cover.jpg',cover_url)
    crop_img('./index_material/'+type_str[news_type]+'_cover.jpg')
    check_cover_name(news_type)

def make_html(news_type,title,url,_time,p1,cover_url):
    #news_type0 为yhyw，1为tzgg

    #读取新闻的微信版html
    req = urllib.request.Request(url)
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
    wc_html=urlopen(req).read().decode('utf-8')
    #

    os.chdir(work_path[news_type])#进入yhyw/tzgg目录
    if news_type==0:
        #确定文件名
        folder_path='./new_'+_time.replace('-','_')
        if os.path.exists(folder_path)!= 0:
            i=2
            while os.path.exists(folder_path+'_'+str(i))!= 0:
                i+=1
            folder_path=folder_path+'_'+str(i)
        os.mkdir(folder_path)
        folder_name=folder_path.replace('./','')
        #
        os.chdir('../..')#yhyw.html所在目录
        #添加到timeline
        f=open('./yhyw.html','r',encoding="utf-8")
        yhyw_html=f.read()
        f.close()
        time_block="""
        <div class=\"cd-timeline-block\">
            <div class=\"cd-timeline-img cd-picture\">
            </div>
            <div class=\"cd-timeline-content\">
                <h2><a href=\"./html_news/news_content/news_name/news_name.html\">title</a></h2>
                <p>p1<br /></p>
                <span class=\"cd-date\">news_date</span>
            </div>
        </div>
        """
        time_block=time_block.replace('news_name',folder_name).replace('title',title).replace('p1',p1).replace('news_date',_time)
        yhyw_html=yhyw_html.replace('<!--replace_tag-->','<!--replace_tag-->'+time_block)
        f=open('./yhyw.html','w',encoding="utf-8")
        f.write(yhyw_html)
        f.close()
        #
        
        os.chdir('../..')#index.html所在目录
        #修改index内容
        change_index_and_material(news_type,folder_name,title,cover_url)

        os.chdir('./html_index/html_yhyw/html_news/news_content')
    else:
        #确定文件名
        folder_path='./html_tzgg'
        i=1
        while os.path.exists(folder_path+gs(i))!= 0:
            i+=1
        folder_path=folder_path+gs(i)
        os.mkdir(folder_path)
        folder_name=folder_path.replace('./html_','')

        os.chdir('..')#tzgg.html所在目录
        #添加至通知列表
        f=open('./tzgg.html','r',encoding="utf-8")
        tzgg_html=f.read()
        f.close()
        notice_block="""
				<div>
					<a href="tzgg_content/html_news_name/news_name.html">
						<b style="margin-top:50px;color:black">title</b>
					</a>
					<p class="text-right">news_date</p>
					<a class="btn btn-default" href="tzgg_content/html_news_name/news_name.html" role="button" style="color:black">查看</a>
					<hr>
				</div>"""
        notice_block=notice_block.replace('news_name',folder_name).replace('title',title).replace('news_date',_time.replace('-','/'))
        tzgg_html=tzgg_html.replace('<!--replace_tag-->','<!--replace_tag-->'+notice_block)
        #

        #替换Carousel滚轮图片和标题
        tzgg = BeautifulSoup(open('./tzgg.html', encoding='utf-8'), 'html.parser')
        href=['0']*4
        src=['0']*4
        tit=['0']*4
        for i in range(1,4):
            all=tzgg.find_all('div', id='slide'+str(i))
            href[i]=all[0].a['href']
            src[i]=all[0].img['src']
            tit[i]=str(all[0].font)
        href[0]='./tzgg_content/html_'+folder_name+'/'+folder_name+'.html'
        src[0]='tzgg_material/'+folder_name+'.jpg'
        tit[0]='<font color="white">'+title+'</font>'
        for i in range(1,4):
            tzgg_html=tzgg_html.replace(href[i],href[i-1]).replace(src[i],src[i-1])
            if tit[i]=='':
                empty_warn(i)#输出旧标题为空的警告
            else:
                tzgg_html=tzgg_html.replace(tit[i],tit[i-1])
        #

        f=open('./tzgg.html','w',encoding="utf-8")
        f.write(tzgg_html)
        f.close()
        
        os.chdir('../..')#index.html所在目录
        #修改index内容
        change_index_and_material(news_type,folder_name,title,cover_url)
        
        os.chdir('./html_index/html_tzgg/tzgg_material')
        #下载滚轮图片
        download_img('./'+folder_name+'.jpg',cover_url)
        crop_img('./'+folder_name+'.jpg')
        #
        os.chdir('../tzgg_content')

    os.chdir(folder_path)#进入对应新闻目录

    image_path = './material'
    if  os.path.exists(image_path)== 0:
        os.mkdir(image_path)
    os.chdir(image_path)#进入图片目录

    #图片变为本地
    pattern = 'data-src="(.+?)"'
    result = findall(pattern, wc_html)
    sec_html=findall('<section(?:(?:.|\n)*)</section>',wc_html)
    content=sec_html[0]
    content=content.replace("data-src","src")
    for index, item in enumerate(result,1):
        s=str(item)
        download_img(gs(index) + '.jpg',s)#下载图片
        content=content.replace(s,image_path+'/'+gs(index)+'.jpg')#替换链接
    #

    os.chdir('..')#回到新闻目录

    #编辑写入新闻本体
    if news_type==0:
        f=open('../../../../../auto_update_news/yhyw_model.html','r',encoding="utf-8")
    else:
        f=open('../../../../auto_update_news/tzgg_model.html','r',encoding="utf-8")

    model_html=f.read()
    f.close
    model_html=model_html.replace('empty_zhengwen',content).replace('empty_title',title).replace('empty_time',_time)#tzgg其实没有empty_time
    f=open(folder_name+'.html','w',encoding="utf-8")
    f.write(model_html)
    f.close
    #

    #回到和index.html同级
    os.chdir('../../../..')
    if news_type==0: 
        os.chdir('..')
    print('更新 < '+title+' > 为'+type_str[news_type]+'完毕！')
        
def url_no_yzm(url,headers):
    r = requests.get(url=url, headers=headers)
    while '验证码' in str(r.text):
        print('[-]发现验证码请访问URL:{}输入验证码,输完关掉网页回来按键以继续'.format(r.url))
        webbrowser.open(r.url)
        os.sys("pause")
        r = requests.get(url=url, headers=headers)
    else:
        return r

def zhuaqu():
    #改变工作目录，进入html_index上级
    while(not(os.path.exists('./html_index'))):
        os.chdir('..')

    user='中国科大少年班学院'
    headers={'user-agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)'}
    url='http://weixin.sogou.com/weixin?type=1&s_from=input&query={}&ie=utf8&_sug_=y&_sug_type_=&w=01015002&oq=jike&ri=0&sourceid=sugg&stj=0%3B0%3B0%3B0&stj2=0&stj0=0&stj1=0&hp=36&hp1=&sut=4432&sst0=1529305369937&lkt=5%2C1529305367635%2C1529305369835'.format(user.rstrip())

    while(1):
        try:
            num_of_news=int(input('请输入要查看的新闻篇数(最大为10）：'))
            break
        except:
            print('请输入一个数字!!!')

    r=url_no_yzm(url,headers)
    rsw = findall('src=.*&amp;timestamp=.*&amp;ver=.*&amp;signature=.*', str(r.text))
    cis = findall('.*?==', str(rsw[0]))
    qd = "".join(cis).replace(';', '&')
    urls = 'https://mp.weixin.qq.com/profile?'+ qd
    xiau=url_no_yzm(urls,headers)
    houxu=findall('{.*?}',xiau.content.decode('utf-8'))
    title=findall('"title":".*?"',str(houxu))
    purl=findall('"content_url":".*?"',str(houxu))
    datetime=findall('"datetime":[0-9]*',str(houxu))
    digest=findall('"digest":".*?"',str(houxu))
    cover_url=findall('"cover":".*?"',str(houxu))

    if(num_of_news>=len(title)):
        num_of_news=10
    print('\n将按时间从前向后展示 '+str(num_of_news)+' 条新闻：')

    for i in range(num_of_news-1,-1,-1):
        title[i]=title[i].replace('"','').replace('title:','')#对应title
        purl[i]=purl[i].replace('"','').replace('content_url:','')
        jc=('https://mp.weixin.qq.com'+purl[i]).replace(';','&')#对应链接

        datetime[i]=datetime[i].replace('"datetime":','')
        _time=localtime(float(datetime[i]))
        datetime[i]=(strftime("%Y-%m-%d",_time))

        digest[i]=digest[i].replace('"','').replace('digest:','')#摘要/第一段

        print('-----------------------------------------------------------\n')
        print('第 '+str(num_of_news-i)+ ' 条:')
        print(datetime[i]+': < '+title[i]+' >\n')
        print('摘要:'+digest[i]+'\n')

        print('请输入更新类别：0 for yhyw; 1 for tzgg; 2 for skip')
        news_type=input('input 0/1/2 :')
        while news_type!='0'and news_type!='1'and news_type!='2':
            print('Wrong Input!')
            print('请输入更新类别：0 for yhyw; 1 for tzgg; 2 for skip')
            news_type=input('input 0/1/2 :')
        else:
            print('')
            if news_type=='2':
                print('已跳过 < '+title[i]+' >！\n')
                continue
            else:
                print('请稍候，正在更新...')
                cover_url[i]=cover_url[i].replace('"','').replace('cover:','')#封面图片的链接
                make_html(int(news_type),title[i],jc,datetime[i],digest[i],cover_url[i])
            print('')
                        

zhuaqu()
print('===========================================================\n')
print('本次更新完毕！请检查是否有“注意”内容需要手动修改！')
os.system("pause")