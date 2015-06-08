#!/usr/bin/python

from listingsScraper import listScraper

prefix = 'guanajuato'; # guanajuato, sanmiguel, leon, london
                      # use batchGetListings2 for riodejaneiro

theDir = '../data/places/' + prefix + '/'; 
bVerbose = 0;

f = open( theDir + 'manifest.txt', 'r' );
filenames = list( f )
f.close();

if bVerbose == 0: print('Quiet mode ...');

listings = listScraper( theDir, filenames, bVerbose );

f = open( theDir + prefix + '_listings.txt', 'w' );
for listing in listings:
    f.write( listing + '\n' );
f.close();
