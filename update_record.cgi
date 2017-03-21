#!/usr/bin/perl
use strict;
use warnings;
use POSIX qw(strftime);
use JSON; #if not already installed, just run "cpan JSON"
use CGI;
use DBI;

my $cgi = CGI->new;

print $cgi->header('application/json;charset=UTF-8');
my $sku = $cgi->param('sku');
my $category = $cgi->param('category');
my $vendor = $cgi->param('vendor');
my $vendorModel = $cgi->param('vendorModel');
my $description = $cgi->param('description');
my $features = $cgi->param('features');
my $cost = $cgi->param('cost');
my $retail = $cgi->param('retail');
my $product_image = $cgi->param('product_image');
my $image_state= $cgi->param('image_state');

my $host = "opatija.sdsu.edu";
my $port = "3306";
my $database = "jadrn045";
my $username = "jadrn045";
my $password = "success"; #insert your password here
my $database_source = "dbi:mysql:$database:$host:$port";
	
my $newdbh = DBI->connect($database_source, $username, $password) 
or die 'Cannot connect to db';
my $sql;
my $message = " ";
if ($image_state == 1){
	my ($name,$path,$extension)=fileparse($product_image,qr/\.[^.]*/);
	my $filename = $sku.$extension;
	$filename = lc($filename);
	$sql = $newdbh->prepare("update product set catID='$category',venID='$vendor',vendorModel='$vendorModel',description='$description',features='$features',cost='$cost',retail='$retail' , image = '$filename' where sku='$sku';");
}
else{
	 $sql = $newdbh->prepare("update product set catID='$category',venID='$vendor',vendorModel='$vendorModel',description='$description',features='$features',cost='$cost',retail='$retail'  where sku='$sku';");
}


if ($sql->execute()) {
  $message = "Success";
}
else {
  $message = "Error";
}
$sql->finish();
$newdbh->disconnect();

#convert  data to JSON
my $op = JSON -> new -> utf8 -> pretty(1);
my $json = $op -> encode({
    result => $message
});
print $json;
