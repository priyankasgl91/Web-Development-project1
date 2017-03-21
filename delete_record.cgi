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
# my $category = $cgi->param('category');
# my $vendor = $cgi->param('vendor');
# my $vendorModel = $cgi->param('vendorModel');
# my $description = $cgi->param('description');
# my $features = $cgi->param('features');
# my $cost = $cgi->param('cost');
# my $retail = $cgi->param('retail');
# my $product_image = $cgi->param('product_image');
my $host = "opatija.sdsu.edu";
my $port = "3306";
my $database = "jadrn045";
my $username = "jadrn045";
my $password = "success"; #insert your password here
my $database_source = "dbi:mysql:$database:$host:$port";
	
my $newdbh = DBI->connect($database_source, $username, $password) 
or die 'Cannot connect to db';

my $response = " ";
my $sql = $newdbh->prepare("delete from product where sku='$sku';");


if ($sql->execute()) {
  $response = "Record Deleted";
}
else {
  $response = "Error";
}
$sql->finish();
$newdbh->disconnect();

#convert  data to JSON
my $op = JSON -> new -> utf8 -> pretty(1);
my $json = $op -> encode({
    result => $response
});
print $json;
