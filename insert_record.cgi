#!/usr/bin/perl
#  Project #1 
use strict;
use warnings;
use POSIX qw(strftime);
use JSON; #if not already installed, just run "cpan JSON"
use CGI;
use DBI;
use File::Basename;

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
my ($name,$path,$extension)=fileparse($product_image,qr/\.[^.]*/);
# my ($name,$path,$extension)=fileparse($product_image, '/..*/');
 # my($filename, $dirs, $suffix) = fileparse($product_image);
#  print "1".$filename;
#  print "2".$dirs;
#  print "3".$suffix;
# my $image=$filename;
# $image = untaint($image);

my $filename = $sku.$extension;
$filename = lc($filename);
my $host = "opatija.sdsu.edu";
my $port = "3306";
my $database = "jadrn045";
my $username = "jadrn045";
my $password = "success"; #insert your password here
my $database_source = "dbi:mysql:$database:$host:$port";
	
my $newdbh = DBI->connect($database_source, $username, $password) 
or die 'Cannot connect to db';


my $message = " ";
my $sql = $newdbh->prepare("INSERT INTO product (sku,catID,venID,vendorModel,description,features,cost,retail,image) VALUES 
							('$sku', '$category','$vendor','$vendorModel', '$description', '$features', '$cost', '$retail','$filename');");


if ($sql->execute()) {
  $message = "Success ";
  # print $image;
}
else {
  $message = "error";
  print $message;
  
}
$sql->finish();
$newdbh->disconnect();

#convert  data to JSON
my $op = JSON -> new -> utf8 -> pretty(1);
my $json = $op -> encode({
    result => $message
});
print $json;

# sub untaint {
#     if($image =~ m/^(\w+)$/) { die "Tainted filename!"; }
#     return $1;
#     }
