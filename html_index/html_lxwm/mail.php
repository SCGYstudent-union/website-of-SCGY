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
$mail->Username = "2197255751@qq.com";
$mail->Password = "ljf200411";
$mail->SetFrom("2197255751@qq.com", "someone");
$mail->AddReplyTo("2197255751@qq.com", "someone");
$mail->Subject = "少院网站——联系我们";
$mail->AltBody = "";
$mail->MsgHTML($content);
$mail->AddAddress("2197255751@qq.com");

if (!$mail->Send()) {
    echo "Error:".$mail->ErrorInfo;
} else {
    echo "Success!";
}

?>