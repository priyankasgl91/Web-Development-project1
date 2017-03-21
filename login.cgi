#!/usr/bin/perl

use CGI;
use Crypt::SaltedHash;
use JSON;

##---------------------------- MAIN ---------------------------------------
print "Content-type: text/html\n\n";
my $q;

###########################################################################

###########################################################################

    $q = new CGI;
    my $user = $q->param("username");
    my $password = $q->param("password");    
    open DATA, "</srv/www/cgi-bin/jadrn045/proj1/passwords.dat" 
            or die "Cannot open file.";
    @file_lines = <DATA>;
    close DATA;

    $OK = 0; #not authorized

    foreach $line (@file_lines) {
        chomp $line;
        ($stored_user, $stored_pass) = split /=/, $line;    
        if($stored_user eq $user && Crypt::SaltedHash->validate($stored_pass, $password)) {
            $OK = 1;
            last;
            }
        }
print $OK;
