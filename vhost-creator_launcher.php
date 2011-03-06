<?php
$domainName = "";
?>
<html>
<head>
<title>vhost creator</title>
</head>
<body>
<h2 style="text-align: left; padding: 10px; background:#dee; padding: 10px">
<form method="post" action="<?php echo $PHP_SELF;?>">
Domain Name: <input type="text" size="25" maxlength="100" name="DomainName"><br/>
Aliases, space separated: <input type="text" size="25" maxlength="100" name="Aliases"><br/>
<input type="submit" value="submit" name="submit">
</form>
<?php
$domainName = $_POST["DomainName"];
$aliases = $_POST["Aliases"];
$command = "python vhost-creator.py " . $domainName . " " . $aliases;
if ($domainName) system($command);
?>
</h2>
</body>
</html>
