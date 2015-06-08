#!/usr/bin/python

import io
import re
from bs4 import BeautifulSoup

def listScraper( theDir, filenames, bVerbose ):



    listings = [];
    for fn in filenames:
        if bVerbose == 0: print("."),;
        filename = fn[0:len(fn)-1]
        if bVerbose: print( unicode('\n========================== Scrapping listings number ================== \n' ) );
        
        soup = BeautifulSoup(open( theDir + filename  ) );

        #f = io.open( theDir + filename + '.txt', 'w', encoding='utf8');
        #if bVerbose: print('Output => ' + theDir + filename + '.txt\n');

        if bVerbose: print( unicode('========================================================================= \n' ) );



        def has_class( tag ):
            return  tag.has_attr('class');


        tokens = soup.find_all( 'div' );
        for token in tokens:
            if token.has_attr( 'class' ):
                #if bVerbose: print( token[ 'class' ][0] ) 
                if re.search( 'listing-description', token[ 'class' ][0] ):
                    m = re.search( '(?<=wl-data-)\d+', token[ 'class' ][1] )
                    #if bVerbose: print( m.group(0), token['class' ][1] )
                    listings.append( m.group(0) );
                    if bVerbose: print( '... ' + m.group(0) + '.html' )
            
        
    return listings;
