#!/usr/bin/python

from listingsScraper2 import listScraper2

prefix = 'riodejaneiro'

theDir = '../data/places/'


f = open( theDir + 'manifest.txt', 'r' );
filenames = list( f )
f.close();

listings = listScraper2( theDir, filenames );

f = open( theDir + prefix + '_listings.txt', 'w' );
for listing in listings:
    f.write( listing + '\n' );
f.close();
