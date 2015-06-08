#!/usr/bin/python

import io
import re
from bs4 import BeautifulSoup

def listScraper2( theDir, filenames ):

    listings = [];
    for fn in filenames:
        filename = fn[0:len(fn)-1]
        print( unicode('\n========================== Scrapping listings number ================== \n' ) );
        
        soup = BeautifulSoup(open( theDir + filename  ) );

        f = io.open( theDir + filename + '.txt', 'w', encoding='utf8');
        print('Output => ' + theDir + filename + '.txt\n');

        print( unicode('========================================================================= \n' ) );



        def has_href_and_target( tag ):
            return  tag.has_attr('href') and tag.has_attr('target');


        tokens = soup.find_all( 'a' );
        for token in tokens:
            if has_href_and_target( token ):
                if re.search( 'listing', token[ 'target' ] ):
                    #print(token['target'])
                    m = re.search( '(?<=listing_)\d+', token[ 'target' ] )
                    #print( m.group(0), token['target' ] )
                    if m.group(0) not in listings:
                        listings.append( m.group(0) );
                        print( '... ' + m.group(0) + '.html' )
    return listings;
