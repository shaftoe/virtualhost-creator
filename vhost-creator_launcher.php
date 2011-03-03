<?php
$domainName = "";
?>
<html>
<head>
<title>vhost creator</title>
</head>
<body>
<h2 style="text-align: center; padding: 10px; background:#dee">
<form method="post" action="<?php echo $PHP_SELF;?>">
Domain Name: <input type="text" size="25" maxlength="100" name="DomainName">
<input type="submit" value="submit" name="submit">
</form>
<?php
$domainName = $_POST["DomainName"];
if ($domainName) system("python vhost-creator.py " . $domainName);
?>
</h2>
</body>
</html>
