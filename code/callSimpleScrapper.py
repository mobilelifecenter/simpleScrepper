#!/usr/bin/python

import simpleScraper

bVerbose = 0;
theDir = '../data/snapshots/06082015/guanajuato/';

f = open( theDir + 'guanajuato_listings_py.txt', 'r' );
listings = list( f );
f.close();

if bVerbose == 0:
    print('Quiet mode');

listing = [];
for listing in listings:
    listing = listing.replace('\n','');

    #listing = '6363636';
    hostID = simpleScraper.scrapData( theDir, listing, bVerbose );
    #print( hostID );
    simpleScraper.scrapReviews( theDir, listing, listing, bVerbose ); 


    
    f = open( theDir + listing + '/' + listing  + '_'  + 'metadata.txt', 'r');
    line = list( f );
    line[0] = line[0].replace('\n','');
    if line[0] > 1:
        for i in range(2, int( line[0] )):
            simpleScraper.scrapReviews( theDir, listing, listing + '_' + str( i ), bVerbose );

    simpleScraper.scrapHostAnswers( theDir, listing, listing, bVerbose );

    if line[0] > 1:    
        for i in range(2, int( line[0] )):
            simpleScraper.scrapHostAnswers( theDir, listing, listing + '_' + str( i ), bVerbose ); 

    simpleScraper.getUsersIds( theDir, listing, listing, hostID, bVerbose );

    if line[0] > 1:    
        for i in range(2, int( line[0] )):
            simpleScraper.getUsersIds( theDir, listing, listing + '_' + str( i ), hostID, bVerbose );

    
    simpleScraper.wrapUp( theDir, listing, bVerbose );
   
 
