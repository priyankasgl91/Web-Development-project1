#!/usr/bin/perl

#     This code uses the SHA2 algorithm, which uses a 256 or 512 bit key, 
#     which then generates a 512 or 1024 bit block.  The longer key makes 
#     this algorithm better, as does the fact that it appears to be 
#     impervious to collisions, which makes it more resistant to hacking.  
#     This is the algorithm generally used by the US government.  
#     This algorithm is still not widely used in industry, though it should be.
#     CS645, Spring 2017
#     Alan Riggins
# Sehgal, Priyanka Account: Jadrn045
#  CS645,Spring 2017
#  Project #1 

use Crypt::SaltedHash;

my @users = ('cs645','priyanka','jsmith','jadrn000');
my @passwords = ('sp2017','sehgal','abc','abc');
my @encrypted_passwords;
my $arr_len = @users;

for($i=0; $i < $arr_len; $i++) {
    my $encryption_object = Crypt::SaltedHash->new(algorithm => 'SHA-2');
    $encryption_object->add($passwords[$i]);
    push(@encrypted_passwords, $encryption_object->generate);
}

open(DATA,">passwords.dat") or die "Cannot open file";


for($i=0; $i < $arr_len; $i++) {
    print DATA $users[$i]."=".$encrypted_passwords[$i]."\n";
    }
    
close(DATA);    
