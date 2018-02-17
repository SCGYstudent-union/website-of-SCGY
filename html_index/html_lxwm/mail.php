<?php
require_once('class.phpmailer.php');
require_once("class.smtp.php");

$content="内容<br/>：".$message;

$mail = new PHPMailer();

$mail->CharSet = "UTF-8";
$mail->IsSMTP();
$mail->SMTPAuth = true;
$mail->SMTPSecure = "ssl";
$mail->Host = "smtp.exmail.qq.com";
$mail->Port = 465;
$mail->Username = "scgypf@ourscgy.ustc.edu.cn";
$mail->Password = "s1g2c3y4";
$mail->SetFrom("scgypf@ourscgy.ustc.edu.cn", "someone");
$mail->AddReplyTo("scgypf@ourscgy.ustc.edu.cn", "someone");
$mail->Subject = "少院网站——联系我们";
$mail->AltBody = "";
$mail->MsgHTML($content);
$mail->AddAddress("scgypf@ourscgy.ustc.edu.cn");

if (!$mail->Send()) {
    echo "Error:".$mail->ErrorInfo;
} else {
    echo "Success!";
}

?>