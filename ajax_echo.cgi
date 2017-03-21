#!/usr/bin/perl 
#	Ajax script for confirmation of receipt
#	CS645 Spring 2017
#	Code by Alan Riggins
#
# Sehgal, Priyanka Account: Jadrn045
#  CS645,Spring 2017
#  Project #1 
use CGI;

my $q = new CGI;


		
my ($answer, $key, $value);

                
foreach $key ($q->param) {
    $answer .= $key."=";
    $answer .= $q->param($key);
    $answer .= "<br />";
}

print "Content-type:  text/html\n\n";
print $answer;

