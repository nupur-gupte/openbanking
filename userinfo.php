<?php
$con = mysqli_connect('localhost','root');
if($con)
{
  echo"connection sucessfull";

}
else
{
  echo"no connection!";
}
mysqli_select_db($con,'notesdoubt');
$name = $_POST['name'];
$phone = $_POST['phone'];
$email = $_POST['email'];
$subject = $_POST['subject'];
$message = $_POST['message'];

$query = "insert into userinfodata1(name,phone,email,subject,message)
values('$name','$phone','$email','$subject','$message')";

echo "$query";
mysqli_query($con, $query);
echo"connection sucessfull";
header('location:index.html');
?>