Auto update news
---------------------
author:RubyL
date:2019/3/2
discription:新闻更新懒人包
version:1.0
---------------------------------------
源码update_news.py文件也一并上传了，欢迎报bug
email:ruby_ocelot@mail.ustc.edu.cn
---------------------------------------
开发目的：
1）免除将微信版新闻转为少院网站版新闻时复制粘贴的烦恼，缩短日常更新耗时
2）避免忘记修改index.html,tzgg.html和yhyw.html
3）解决新闻样式过于简略问题 
4）tzgg.html中的滚轮图片自动裁切为4:3,保证美观
5）同时还有.sh懒人包自行食用，简化github操作

环境：目前只支持windows10，win7应该不行，Linux以后再说，Mac就不管了。
---------------------------------------------------------------------------------
操作说明：
注：以下说明建立已经默认使用者
1)安装过git
2)fork过BARaphael/website-of-SCGY
3)clone过自己fork下来的库到本地，这样origin就是使用者自己的项目地址，拥有push的权限
p.s.如果参考的是群里的”github教程第二版“，不要使用 git init 命令，如果已经用了，自己看着办吧

以下.sh不需要传参，可直接双击运行

（一）同步原始项目到本地
懒人：git_pull.sh
Or
git命令：git pull git@github.com:BARaphael/website-of-SCGY.git master

（二）修改网页内容
p.s.此处建议用懒人exe，避免手动修改破坏格式
懒人：auto_renewX.X.exe （有可能遇到验证码，并需要手动决定是否更新/更新类别）
Or（不推荐手动）
手动改注意看注释，以及本txt后面的注意事项，避免破坏格式导致以后使用懒人包出错

（三）检查内容
用浏览器打开本地的html，检查index.html yhyw.html tzgg.html对应部分是否正常
如果（二）中控制台打印信息 "!!!注意...!!!" 提示修改的话，需手动修改对应部分。
如果（二）中操作失误，运行
懒人：git_again.sh
Or
git命令：
git clean -df （删除所有新添加文件）
git checkout . （恢复所有修改和删除的文件）

p.s.已经add过的文件不会通过此方法还原，想还原去问搜索引擎

还原过后从（二）重来

（四）推送到自己的远程仓库
懒人：git_push_news.sh（此处commit的注释为”update_news")（如果origin不是自己的仓库就别用了）
Or
git命令:
git add .
git commit -m "自己的注释，英文"
git push origin master

（五）发送pullrequest
去https://github.com想办法发pullrequest，发完以后找有权限的人merge

搞定owo
===================================================================
注意事项：
1.tzgg.html和yhyw.html里的<!--replace_tag-->保持在顶端
2.yhyw文件夹命名规则为new_+发布日期（下划线格式）,如果不止一个，新建的后加_n
3.tzgg没什么好说的，000是用来凑数的
4.tzgg.html滚轮的标题不要为空！上次还看见一个标题为空，把字P在图上的，不要学Ta
5.滚轮图片自己裁4：3咯
6.index.html里tzgg和yhyw对应两张图片的src不要改，新图片改名就好


