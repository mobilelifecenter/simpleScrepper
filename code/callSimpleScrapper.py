#!/usr/bin/python


import simpleScraper

bVerbose = 1;

prefix = 'sanmiguel'

theDir = '../data/snapshots/08112015/' + prefix + '/';

f = open( theDir + prefix + '_listings_py.txt', 'r' );
listings = list( f );
f.close();

if bVerbose == 0:
    print('Quiet mode');

listing = [];
for listing in listings:
    listing = listing.replace('\n','');

    #listing = '6363636';
    hostID = simpleScraper.scrapData( theDir, listing, listing + '_1',  bVerbose );
    #print( listing );
    simpleScraper.scrapReviews( theDir, listing, listing + '_1', bVerbose ); 

    
    f = open( theDir + listing + '/' + listing  + '_'  + 'metadata.txt', 'r');
    line = list( f );
    line[0] = line[0].replace('\n','');
    #print(line[0])
    if int( line[0] ) > 1:
        for i in range(2, int( line[0] )):
            simpleScraper.scrapReviews( theDir, listing, listing + '_' + str( i ), bVerbose );

    simpleScraper.scrapHostAnswers( theDir, listing, listing + '_1', bVerbose );

    if int( line[0] ) > 1:    
        for i in range(2, int( line[0] )):
            simpleScraper.scrapHostAnswers( theDir, listing, listing + '_' + str( i ), bVerbose ); 

    simpleScraper.getUsersIds( theDir, listing, listing + '_1', hostID, bVerbose );

    if int( line[0] ) > 1:    
        for i in range(2, int( line[0] )):
            simpleScraper.getUsersIds( theDir, listing, listing + '_' + str( i ), hostID, bVerbose );

    
    simpleScraper.wrapUp( theDir, listing, bVerbose );
   
 
