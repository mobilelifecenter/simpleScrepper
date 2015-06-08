#!/usr/bin/python

import io
import re
from bs4 import BeautifulSoup

def filter_non_printable(str):
      return ''.join([c for c in str if ord(c) > 31 or ord(c) == 9])



def scrapData( theDir, listing, bVerbose ):
    #import urllib2
    #listing = '4719629';
    #response = urllib2.urlopen('https://www.airbnb.com/rooms/' + listing )
    #html = response.read()
    #soup = BeautifulSoup(open(html))


    print("."),;
    if bVerbose: print( unicode('\n========================== Simple scraper v 0.1 ========================== \n' ) );
    
    soup = BeautifulSoup(open( theDir + listing + '/' + listing + '.html' ))

    f = io.open( theDir + listing + '/' + listing  + '.xml', 'w', encoding='utf8')
    if bVerbose: print('Output => ' + theDir + listing + '/' + listing  + '.xml\n');

    if bVerbose: print( unicode('========================================================================= \n' ) );
    
    f.write( unicode( '<?xml version="1.0" encoding="UTF-8"?>' ) );
    if bVerbose: print( unicode( '<?xml version="1.0" encoding="UTF-8"?>' ) );

    f.write( unicode( '\n<listing>' ) );
    if bVerbose: print( unicode( '<listing>' ) );


    
    # ======================================  Host name and Id
    #  

    f.write( unicode( '\n<!-- Host and users ids -->') )
    if bVerbose: print( unicode( '<!-- Host and users ids -->' ))
    numbersList = [];
    tokens = soup.find_all( 'a' );
    for token in tokens:
          if token.has_attr('href'):
                m = re.search( '/users/show/', token['href'] );
                if m != None:
                     if len( m.group() ) > 0:
		         items = re.findall( '\d*', token['href'] );
			 for item in items:
			      if item != '':
				    numbersList.append( item );
    #print( numbersList );
    listUnique = set( numbersList );
    othersList = [];
    maxval = -1;
    for number in listUnique:
       if numbersList.count( number ) > maxval:
             maxval = numbersList.count( number );
             val = number;
             
    for number in listUnique:
          if number != val:
              othersList.append( number );

    hostID = val;          
    #print('Val' + str( val ) );
    f.write( unicode( '\n<tag type="hostId">' + str( val ) + '</tag>' ) );
    if bVerbose: print( unicode( '<tag type="hostId">' + str( val ) + '</tag>' ) );
 
    #for number in othersList:
    #f.write( unicode( '\n<tag type="userId">' + str( number ) + '</tag>' ) );
    #if bVerbose: print( unicode( '<tag type="userId">' + str( number ) + '</tag>' ) );
				     

    # ======================================  Price
    # ex: <meta content="27" itemprop='price'>
    def has_content_and_itemprop( tag ):
        return tag.has_attr('content') and  tag.has_attr( 'itemprop' );
                                                          
    f.write( unicode( '\n<!-- Price and currency -->') )
    if bVerbose: print( unicode( '<!-- Price and currency -->' ))
    tokens = soup.find_all( 'meta' );
    price = '';
    currency = '';
    for token in tokens:
        if has_content_and_itemprop( token ):
            # if bVerbose: print( token );
            if token['itemprop'] == 'price':
                price = token['content'];
                # if bVerbose: print( token['content'] )
            if token['itemprop'] == 'priceCurrency':    
                currency = token['content'];
                # if bVerbose: print( token['content']);
    f.write( unicode( '\n<tag type="dailyPrice">' + price + '</tag>' ) );
    if bVerbose: print( unicode( '<tag type="dailyPrice">' + price + '</tag>' ) );
    f.write( unicode( '\n<tag type="priceCurrency">' + currency + '</tag>' ) );
    if bVerbose: print( unicode( '<tag type="priceCurrency">' + currency + '</tag>' ) );

    # ======================================  Search metadata
    f.write( unicode( '\n<!-- Metadata -->') )
    if bVerbose: print( unicode( '<!-- Metadata -->' ))
    def has_property_and_content( tag ):
        return tag.has_attr('property') and  tag.has_attr( 'content')

    tokens = soup.find_all( has_property_and_content );
    for token in tokens:
        if token['property'] != 'og:image': 
            #if bVerbose: print( token['property'], token['content'] )
            if  token['property'] != 'og:description':
                if isinstance( token['content'], list ):
                    desc = str( token['content'][0] );
                elif isinstance( token['content'], str ):
                    desc = str( token['content']);
                else:
                     raise('Unexpected instance.')                    

                descr = str( desc );
                descr = descr.replace('&','and' );
                descr = filter_non_printable( descr );
                f.write( unicode( '\n<tag type ="' + token['property'] + '">' + str( descr ) + '</tag>' ) );
                if bVerbose: print( unicode( '<tag type ="' + token['property'] + '">' + str( descr ) + '</tag>' ) );
            else:
                if isinstance( token['content'], list ):
                    desc = str( token['content'][0] );
                elif isinstance( token['content'], str ):
                    desc = str( token['content'] );
                else:
                     raise('Unexpected instance.')
                desc = desc.replace( '&', 'and' );
                desc = filter_non_printable( desc );
                f.write( unicode( '\n<tag type ="' + token['property'] + '">' + str( desc ) + '</tag>' ) );
                if bVerbose: print( unicode( '<tag type ="' + token['property'] + '">' + str( desc ) + '</tag>' ) );
     
    #======================================  Stars
    f.write(unicode( '\n<!-- Stars -->') )
    if bVerbose: print(unicode( '<!-- Stars -->') )
    tokens = soup.find_all('i');
    count = 0;
    stars = [];
    for token in tokens:
        if token.has_attr( 'class' ):
            if token['class'][0] == 'icon' and token['class'][1] == 'icon-beach':
               count += 1;
               if count < 10: continue 
               if token['class'][2] == 'icon-star':
                   stars.append( 1 );
               elif token['class'][2] == 'icon-star-half':
                   stars.append(.5);
               else:
                   stars.append(0);              
               #if bVerbose: print( token )
                   
    scoreReviews        =  sum(stars[0:5]); 
    scoreAccuracy       =  sum(stars[5:10]);
    scoreCommunication  =  sum(stars[10:15]);
    scoreCleaness       =  sum(stars[15:20]);
    scoreLocation       =  sum(stars[20:25]);
    scoreCheckIn        =  sum(stars[25:30]);
    scoreValue          =  sum(stars[30:35]);

    f.write( unicode( '\n<tag type ="scoreReviews">' + str( scoreReviews ) + '</tag>' ) );
    f.write( unicode( '\n<tag type ="scoreAccuracy">' + str( scoreAccuracy ) + '</tag>' ) );
    f.write( unicode( '\n<tag type ="scoreCommunication">' + str( scoreCommunication ) + '</tag>' ) );
    f.write( unicode( '\n<tag type ="scoreCleaness">' + str( scoreCleaness ) + '</tag>' ) );
    f.write( unicode( '\n<tag type ="scoreLocation">' + str( scoreLocation ) + '</tag>' ) );
    f.write( unicode( '\n<tag type ="scoreCheckIn">' + str( scoreCheckIn ) + '</tag>' ) );
    f.write( unicode( '\n<tag type ="scoreValue">' + str( scoreValue ) + '</tag>' ) );


    if bVerbose: print( unicode( '<tag type ="scoreReviews">' + str( scoreReviews ) + '</tag>' ) );
    if bVerbose: print( unicode( '<tag type ="scoreAccuracy">' + str( scoreAccuracy ) + '</tag>' ) );
    if bVerbose: print( unicode( '<tag type ="scoreCommunication">' + str( scoreCommunication ) + '</tag>' ) );
    if bVerbose: print( unicode( '<tag type ="scoreCleaness">' + str( scoreCleaness ) + '</tag>' ) );
    if bVerbose: print( unicode( '<tag type ="scoreLocation">' + str( scoreLocation ) + '</tag>' ) );
    if bVerbose: print( unicode( '<tag type ="scoreCheckIn">' + str( scoreCheckIn ) + '</tag>' ) );
    if bVerbose: print( unicode( '<tag type ="scoreValue">' + str( scoreValue ) + '</tag>' ) );



    # Serch for Amenities
    f.write( unicode( '\n<!-- Amenities -->' ))
    if bVerbose: print( unicode( '<!-- Amenities -->' ))

    amenities = [];
    amenities.append( 'Kitchen' );
    amenities.append( 'Internet' );
    amenities.append( 'TV' );
    amenities.append( 'Essentials' );
    amenities.append( 'Shampoo' );
    amenities.append( 'Heating' );
    amenities.append( 'Air Conditioning' ); 
    amenities.append( 'Washer' ); 
    amenities.append( 'Dryer' ); 
    amenities.append( 'Free Parking on Premises' );
    amenities.append( 'Wireless Internet' ); 
    amenities.append( 'Cable TV' ); 
    amenities.append( 'Breakfast' ); 
    amenities.append( 'Pets Allowed' ); 
    amenities.append( 'Family/Kid Friendly' ); 
    amenities.append( 'Suitable for Events' ); 
    amenities.append( 'Smoking Allowed' ); 
    amenities.append( 'Wheelchair Accessible' ); 
    amenities.append( 'Elevator in Building' ); 
    amenities.append( 'Indoor Fireplace' ); 
    amenities.append( 'Buzzer/Wireless Intercom' ); 
    amenities.append( 'Doorman' ); 
    amenities.append( 'Pool' ); 
    amenities.append( 'Hot Tub' ); 
    amenities.append( 'Gym' ); 
    amenities.append( 'Smoke Detector' ); 
    amenities.append( 'Carbon Monoxide Detector' ); 
    amenities.append( 'First Aid Kit' ); 
    amenities.append( 'Safety Card' ); 
    amenities.append( 'Fire Extinguisher'); 

    tokens = soup.find_all('span');
    for token in tokens:
        if token.has_attr('id') and not token.has_attr('class') :
            if not token.find_all( 'strong' )  and not token.find_all( 'del'):
                if len( token ) > 1:
                    raise NameError('More than one string not expected')
                for string in token.strings:
                    for am in amenities:  
                        res = re.search( am, string )
                        if res:
                            #if bVerbose: print( 'ammenities:', am )
                            f.write( unicode( '\n<tag type = "ammenities">' + am + '</tag>' ) );
                            if bVerbose: print( unicode( '<tag type = "ammenities">' + am + '</tag>' ) );
      
                


    # Serch for Space and Prices

    f.write(unicode( '\n<!-- Space and Prices -->' ));
    if bVerbose: print(unicode( '<!-- Space and Prices -->' ));


    spaceAndPrices = [];
    spaceAndPrices.append( 'Property type:' );
    spaceAndPrices.append( 'Accommodates:' );
    spaceAndPrices.append( 'Bedrooms:' );
    spaceAndPrices.append( 'Bathrooms:' );
    spaceAndPrices.append( 'Beds:' );
    spaceAndPrices.append( 'Check In:' );
    spaceAndPrices.append( 'Check Out:' );
    spaceAndPrices.append( 'Pet Owner:' );

    spaceAndPrices.append( 'Extra people::' );
    spaceAndPrices.append( 'Cleaning Fee' );
    spaceAndPrices.append( 'Cancellation:' );


    spaceAndPricesName = [];
    spaceAndPricesValue = [];

    tokens = soup.find_all('div');                            
    for token in tokens:
        if len( token ) == 2:
            if token.contents[0].string and token.contents[1].string:
                desc = token.contents[1].string;
                desc = desc.replace( '&', 'and' );
                #print ( repr( token.contents[0].string ), repr( token.contents[1].string ) );
                f.write( unicode( '\n<tag type ="' + ( token.contents[0].string )  + '">' + ( desc ) + '</tag>' ) );
                if bVerbose: print( unicode( '<tag type ="' + ( token.contents[0].string ) + '">' + ( desc ) + '</tag>' ) );
                spaceAndPricesName.append( token.contents[0].string );
                spaceAndPricesValue.append( token.contents[1].string );


                    
    # Serch for Description
    f.write( unicode( '\n<!-- Description -->') )
    if bVerbose: print( unicode( '<!-- Description -->') )
    f.write( unicode( '\n<tag type ="description">' ) )
    if bVerbose: print( unicode( '<tag type ="description">' ) )
    tokens = soup.find_all('div'); 
    for token in tokens:
        if token.has_attr('class'):
            if len( token['class'] ) == 2:
                #if bVerbose: print( token['class'] )
                if token['class'][0] == 'row' and  token['class'][1] == 'description':
                    toks = token.find_all( 'p' );
                    count = 1;
                    description = [];
                    for tok in toks:
                        if count == 1:
                            description = tok.contents
                            count += 1;
                        else:
                            description = description +  tok.contents;
                    desc = '';        
                    for string in description:
                        desc = desc + '. ' + unicode( string )
                    desc = desc.replace('&','and');
                    desc = desc.replace('<strong>',' ');
                    desc = desc.replace('<br/>', ' ');
                    desc = desc.replace('</strong>',' ');
                    desc = filter_non_printable( desc );
                    f.write( unicode( desc ) ) ;
                    if bVerbose: print( unicode( desc ) ) ;

    f.write( unicode( '</tag>' ) )
    if bVerbose: print( unicode( '</tag>' ) )


    # House Rules
    f.write( unicode( '\n<!-- House Rules -->' ) )
    if bVerbose: print( unicode( '<!-- House Rules -->' ) )
    f.write( unicode( '\n<tag type ="houseRules">' ) )
    if bVerbose: print( unicode( '<tag type ="houseRules">' ) )
    tokens = soup.find_all('div'); 
    for token in tokens:
        if token.has_attr('class'):
            if len( token['class'] ) == 1:
                #if bVerbose: print( token['class'] )
                if token['class'][0] == 'expandable-content':
                    if token.parent['class'][0] == 'col-md-9':
                        toks = token.find_all( 'p' );
                        count = 1;
                        for tok in toks:
                            #if bVerbose: print( tok )
                            if count == 1:
                                description = tok.contents
                                count += 1;
                            else:
                                description = description +  tok.contents;
                        desc = '';        
                        for string in description:
                            desc = desc + '. ' + unicode( string )
                        desc = desc.replace('&', 'and');
                        desc = desc.replace('<br/>', ' ');
                        desc = filter_non_printable( desc );
                        f.write( unicode( desc ) ) ;
                        if bVerbose: print( unicode( desc ) ) ;

    f.write( unicode( '</tag>' ) )
    if bVerbose: print( unicode( '</tag>' ) )    

    # Availability
    f.write( unicode('\nA<!-- Availability -->') )
    if bVerbose: print( unicode('<!-- Availability -->') )
    tokens = soup.find_all('div'); 
    for token in tokens:
        if token.has_attr('class'):
            if len( token['class'] ) == 1:
                #if bVerbose: print( token['class'] )
                if token['class'][0] == 'col-md-6':
                    if token.parent['class'][0] == 'row':
                        if len( token.contents ) == 3:
                            #if bVerbose: print( token.contents )                       
                            if re.search( 'minimum stay', token.contents[2].string ):
                                    toks = token.find_all( 'strong' );
                                    for tok in toks:
                                        f.write( '\n<tag type="availability">' + unicode( tok.contents[0] ) + "</tag>" )
                                        if bVerbose: print('<tag type="availability">' + unicode( tok.contents[0] ) + "</tag>" );


    # Search number of reviews
    tokens = soup.find_all('h4');

    f.write( unicode( '\n<!-- # Reviews -->') )
    if bVerbose: print( unicode( '<!-- # Reviews -->') )

    numReviews = '0';
    for token in tokens:
        for tok in token.contents:
                string = str( tok )
                if isinstance( string, str ):
                    if len( re.findall( 'Reviews', string ) ) != 0:
                        codes = re.findall( '\d.', string );
                        for c in codes:
                            numReviews = numReviews + c
                        f.write( unicode ( '\n<tag type="numberOfReviews">'  + numReviews  + "</tag>" )  );    
                        if bVerbose: print( unicode ( '<tag type="numberOfReviews">'  + numReviews  + "</tag>" )  );
                    elif len( re.findall( 'Review', string ) ) != 0:
                        numReviews = '1';
                        if bVerbose: print( unicode ( '<tag type="numberOfReviews">'  + numReviews  + "</tag>" )  );
                        f.write( unicode ( '\n<tag type="numberOfReviews">'  + numReviews  + "</tag>" )  );    
                    elif len( re.findall( 'No Reviews Yet', string ) ) != 0:
                        numReviews = '0';
                        if bVerbose: print( unicode ( '<tag type="numberOfReviews">'  + numReviews  + "</tag>" )  );
                        f.write( unicode ( '\n<tag type="numberOfReviews">'  + numReviews  + "</tag>" )  );

    f.close();
    return hostID;


def scrapReviews( theDir, listing, name, bVerbose ):
    
    soup = BeautifulSoup(open( theDir + listing + '/' + name + '.html' ))

    f = io.open( theDir + listing + '/' + listing  + '.xml', 'a', encoding='utf8') # append data
    
    tokens = soup.select( ".expandable-content" )

    f.write( unicode( '\n<!-- Reviews -->') )
    if bVerbose: print( unicode( '<!-- Reviews -->') )

    for token in tokens:
	  #print(token)
	  if token.parent.has_attr( 'class' ):
		if token.parent['class']:
		    if len( token.parent['class'] ) == 3:
			  toquenParentClass = token.parent['class'];
			  if ( toquenParentClass[0] == 'review-text' ) & \
			     ( toquenParentClass[1] == 'expandable' ) & \
			     ( toquenParentClass[2] == 'expandable-trigger-more' ):
				toks = token.find_all( 'p' );
				comment = '';
				for tok in toks:
				    if len( tok.contents ) > 0:
					  for tc in range( len( tok.contents ) ):
						desc = str(tok.contents[ tc ]); #tok.contents[0];
						desc = desc.replace('&', 'and');
						comment = comment + desc;
					  comment = filter_non_printable( comment );
				f.write( '\n<tag type="guestReview">' + unicode( comment )  )
				if bVerbose: print( '<tag type="guestReview">' + unicode( comment )  )
				if token.parent.has_attr('data-review-id'):
                                      f.write( ' review-id::' + unicode( token.parent['data-review-id'] ) + '::id-review' + '</tag>' )
				      if bVerbose: print(  ' review-id::' + unicode( token.parent['data-review-id'] ) + '::id-review' + '</tag>' )


    f.close();
    return;

def scrapHostAnswers( theDir, listing, name, bVerbose ):
       
    soup = BeautifulSoup(open( theDir + listing + '/' + name + '.html' ))
    f = io.open( theDir + listing + '/' + listing  + '.xml', 'a', encoding='utf8') # append data
                        
    # Search host responses
    f.write( unicode( '\n<!-- Responses -->') )
    if bVerbose: print( unicode( '<!-- Responses -->') )

    tokens = soup.select( ".media-body" )
    for token in tokens:
        #if bVerbose: print( token)
        toks = token.find_all( 'p' );
        answer = '';
        bGo = 0;
        for tok in toks:
             #print('+' , tok) 
             if len( tok ) > 0:
                   bGo = 1;
                   desc = tok.contents[0];
                   desc = desc.replace('&', 'and');
                   answer = answer + desc;
 
                   
        if bGo == 1:                       
              f.write( '\n<tag type="hostAnswer">' + unicode( answer  ) )
              if bVerbose: print( '<tag type="hostAnswer">' + unicode( answer )  )
              toks = token.find_all( 'div' )

              for tok in toks:
                  #print( 'Tpk:', tok );  
                  if tok.has_attr('data-review-id'):
                      reviewId = tok['data-review-id'];
                      f.write( ' review-id::' + unicode( reviewId ) + '::id-review'  )
                      if bVerbose: print(' review-id::' + unicode( reviewId ) + '::id-review' );

              f.write( unicode( "</tag>" ) )
              if bVerbose: print( unicode( "</tag>" ));
                 

    f.close();
    return;


def getUsersIds( theDir, listing, name, hostID, bVerbose ):

    # ======================================  Users Ids
    #  

    #print( hostID )  

    soup = BeautifulSoup(open( theDir + listing + '/' + name + '.html' ))
    f = io.open( theDir + listing + '/' + listing  + '.xml', 'a', encoding='utf8') # append data

    f.write( unicode( '\n<!-- Users ids -->') )
    if bVerbose: print( unicode( '<!-- Users sers ids -->' ))
    numbersList = [];
    reviewName = [];
    tokens = soup.find_all( 'a' );
    for token in tokens:
	    if token.has_attr('href') and token.has_attr('name') :
		    m = re.search( '/users/show/', token['href'] );
		    if m != None:
			  if len( m.group() ) > 0:
				  items = re.findall( '\d*', token['href'] );
				  for item in items:
					if item != '':
                                             #print( item, token['name']) 
					     numbersList.append( item + '::' + token['name']);
					     
    #print( numbersList );
    listUnique = set( numbersList );
    othersList = [];
    #maxval = -1;
    #for number in listUnique:
    #     if numbersList.count( number ) > maxval:
    #         maxval = numbersList.count( number );
    #         val = number;
               
    for number in listUnique:
          if number != hostID:
              othersList.append( number );

    # f.write( unicode( '\n<tag type="hostId">' + str( val ) + '</tag>' ) );
    # if bVerbose: print( unicode( '<tag type="hostId">' + str( val ) + '</tag>' ) );
 
    for number in othersList:
        f.write( unicode( '\n<tag type="userId">' + str( number ) + '</tag>' ) );
        if bVerbose: print( unicode( '<tag type="userId">' + str( number ) + '</tag>' ) );
        #print( str( number  ) )

    return;


def wrapUp( theDir, listing, bVerbose ):

    
    f = io.open( theDir + listing + '/' + listing  + '.xml', 'a', encoding='utf8') # append data

    f.write( unicode( '\n</listing>' ) );
    if bVerbose: print( unicode( '</listing>' ) );

    f.close();

    if bVerbose: print( unicode('\n========================================================================= \n' ) );
    return;

