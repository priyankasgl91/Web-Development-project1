#!/usr/bin/perl
use DBI;
use CGI;

my $host = "opatija.sdsu.edu";
my $port = "3306";
my $database = "jadrn045";
my $username = "jadrn045";
my $password = "success";
my $database_source = "dbi:mysql:$database:$host:$port";
my $response = "";
my $data = "";

my $dbh = DBI->connect($database_source, $username, $password)
or die 'Cannot connect to db';

my $q = new CGI;
my $sku = $q->param("sku");

my $query = "select sku from product where sku='$sku'";

            
my $sth = $dbh->prepare($query);
$sth->execute();

$count = $sth->rows;

while(my @row=$sth->fetchrow_array()) {    
    $data = $row[0];
    }

if($data) {
    	$newQuery = "select catID, venID, vendorModel, description, features, cost, retail,image from product where sku='$sku'";
    	my $newSth = $dbh->prepare($newQuery);
    	$newSth->execute();
    	while(my @newrow=$newSth->fetchrow_array()) {
    		foreach $item (@newrow) { 
        	$response .= $item."|";
        	}       
    		$response .= ";";    
    	}
    }    
else {
    $response = "ok";
    }  

#$sth->finish();  
#$newSth->finish();
$dbh->disconnect();
    
print "Content-type: text/html\n\n";
print $response;               
