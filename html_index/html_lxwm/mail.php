<?php
require_once('class.phpmailer.php');
require_once("class.smtp.php");

$content=$message;

$mail = new PHPMailer();

$mail->CharSet = "UTF-8";
$mail->IsSMTP();
$mail->SMTPAuth = true;
$mail->SMTPSecure = "ssl";
$mail->Host = "smtp.163.com";
$mail->Port = 465;
$mail->Username = "scgyunion@163.com";
$mail->Password = "scgysu";
$mail->SetFrom("scgyunion@163.com", "someone");
$mail->AddReplyTo("scgyunion@163.com", "someone");
$mail->Subject = "少院网站——联系我们";
$mail->AltBody = "";
$mail->MsgHTML($content);
$mail->AddAddress("scgyunion@163.com");

if (!$mail->Send()) {
    echo "Error:".$mail->ErrorInfo;
} else {
    echo "Success!";
}

?>