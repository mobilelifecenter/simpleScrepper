function airbnbStruct = createAirbnbStruct( theDir, listing )

    title = '';
    hostId = ' ';
    usersId = {};
    pricePerNight = '';
    priceCurrency = '';
    type = '';
    url = '';
    shortDescription = '';
    locality = '';
    region = '';
    country = '';
    city = '';
    rating = '';
    latitude = '';
    longitude = '';
    scoreReviews = '';
    scoreAccuracy = '';
    scoreCommunication = '';
    scoreCleaness = '';
    scoreLocation = '';
    scoreCheckIn = '';
    ammenities = {};
    propertyType  = '';
    accommodates = '';
    bedrooms = '';
    bathrooms = '';
    beds = '';
    checkIn = '';
    checkOut = '';
    petOwner = '';
    extraPeople = '';
    cancellation = '';
    description = '';
    houseRules  = '';
    availability = '';
    numberOfReviews = '';
    guestReviews = {};
    hostAnswers = {};
    numAmmenities = 0;
    numGuestReviews = 0;
    numHostAnswers =  0;
    numUsers = 0;
    
    
    xmlSoup = xml2struct( [ theDir listing '/' listing '.xml' ] );
    for tag = 1 : numel ( xmlSoup.listing.tag ),
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'hostId' )
            
            hostId =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'userId' )
            %
            numUsers = numUsers + 1;
            usersId{ numUsers }  =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'og:title' )
            % og:title
            title =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'og:type' )
            
            type =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'og:url' )
            
            url =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'og:description' )
            
            shortDescription =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'airbedandbreakfast:locality' )
            
            locality =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'airbedandbreakfast:region' )
            
            region =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'airbedandbreakfast:country' )
            
            country =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'airbedandbreakfast:city' )
            
            city =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'airbedandbreakfast:rating' )
            
            rating =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'airbedandbreakfast:location:latitude' )
            
            latitude =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'airbedandbreakfast:location:longitude' )
            
            longitude =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'scoreReviews' )
            
            scoreReviews =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'scoreAccuracy' )
            
            scoreAccuracy =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'scoreCommunication' )
            
            scoreCommunication =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'scoreCleaness' )
            %
            scoreCleaness =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'scoreLocation' )
            %
            scoreLocation =  xmlSoup.listing.tag{ tag }.Text ;
        end  
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'scoreCheckIn' )
            %
            scoreCheckIn =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'ammenities' )
            %
            numAmmenities = numAmmenities + 1;
            ammenities{ numAmmenities }  =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'Property type: ' )
            %
            propertyType =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'Accommodates: ' )
            %
            accommodates =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'Bedrooms: ' )
            %
            bedrooms =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'Bathrooms: ' )
            %
            bathrooms =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'Beds: ' )
            %
            beds =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'Check In: ' )
            %
            checkIn =  xmlSoup.listing.tag{ tag }.Text ;
        end
          if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'Check In: ' )
            %
            checkIn =  xmlSoup.listing.tag{ tag }.Text ;
          end
          if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'Check In: ' )
            %
            checkIn =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'Check Out: ' )
            %
            checkIn =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'Pet Owner: ' )
            %
            petOwner =  xmlSoup.listing.tag{ tag }.Text ;
        end 
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'Check Out: ' )
            %
            checkIn =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'Pet Owner: ' )
            %
            petOwner =  xmlSoup.listing.tag{ tag }.Text ;
        end 
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'Extra people: ' )
            %
            extraPeople =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'Cancellation: ' )
            %
            cencellation =  xmlSoup.listing.tag{ tag }.Text ;
        end   
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'description' )
            %
            description =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'houseRules' )
            %
            houseRules =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'availability' )
            %
            availability =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'guestReview' )
            %
            flag = 0;
            numGuestReviews = numGuestReviews + 1;
            guestReviews{ numGuestReviews } = '';
            id = '';
            try 
                rawtext  =  xmlSoup.listing.tag{ tag }.Text ;
                flag = 1;
            catch 
                display([ 'Warning: empty message listing number ' num2str(listing) ] );
            end
          
            if flag
                m = regexp( rawtext, 'review-id::\d*::id-review', 'match' );
                id = regexp( m, '\d+', 'match' );
                numid =  str2num( char ( id{1} ) ) ;
                newtext = strrep (rawtext, [ 'review-id::' num2str(numid) '::id-review' ], ' ' );
                guestReviews{ numGuestReviews }.text = newtext;
                guestReviews{ numGuestReviews }.reviewId = id;
            end
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'hostAnswer' )
            %
            numHostAnswers = numHostAnswers + 1;
              
            flag = 0;
            id = '';
            try 
                rawtext  =  xmlSoup.listing.tag{ tag }.Text ;
                flag = 1;
            catch 
                display([ 'Warning: empty answer listing number ' num2str(listing) ] );
            end
          
            if flag
                m = regexp( rawtext, 'review-id::\d*::id-review', 'match' );
                id = regexp( m, '\d+', 'match' );
                numid =  str2num( char ( id{1} ) ) ;
                newtext = strrep (rawtext, [ 'review-id::' num2str(numid) '::id-review' ], ' ' );
                hostAnswers{ numHostAnswers }.text = newtext;
                hostAnswers{ numHostAnswers }.reviewId = id;
            end
          
            
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'dailyPrice' )
            %
            pricePerNight  =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'priceCurrency' )
            %
            priceCurrency  =  xmlSoup.listing.tag{ tag }.Text ;
        end
        if strcmp( xmlSoup.listing.tag{ tag }.Attributes.type, 'numberOfReviews' )
            %
            numberOfReviews  =  xmlSoup.listing.tag{ tag }.Text ;
        end
    end
    
    airbnbStruct =  struct( 'hostId', hostId, ...
                            'title', title, ...
                            'pricePerNight', pricePerNight, ...
                            'priceCurrency', priceCurrency, ...
                            'type', type,  ...
                            'url',url,  ...
                            'shortDescription', shortDescription, ...
                            'locality' ,locality, ...
                            'region' ,region, ...
                            'country' ,country, ...
                            'city' ,city, ... 
                            'rating' ,rating, ...
                            'latitude' , latitude, ...
                            'longitude' , longitude, ...
                            'scoreReviews', scoreReviews, ...
                            'scoreAccuracy' ,scoreAccuracy, ...
                            'scoreCommunication' , scoreCommunication, ...
                            'scoreCleaness', scoreCleaness, ...
                            'scoreLocation', scoreLocation, ...
                            'scoreCheckIn', scoreCheckIn, ...
                            'properTytype', propertyType, ...
                            'accommodates', accommodates, ...
                            'bedrooms', bedrooms, ...
                            'bathrooms', bathrooms, ...
                            'beds', beds, ...
                            'checkIn', checkIn, ...
                            'checkOut', checkOut, ...
                            'petOwner', petOwner, ...
                            'extraPeople', extraPeople, ...
                            'cancellation', cancellation, ...
                            'description', description, ...
                            'houseRules', houseRules, ...
                            'availability', availability, ...
                            'numberOfReviews', numberOfReviews);
                             airbnbStruct.usersId = usersId;
                             airbnbStruct.ammenities = ammenities;
                             airbnbStruct.guestReviews = guestReviews;
                             airbnbStruct.hostAnswers = hostAnswers; 
            
                             
                                
    if numel( airbnbStruct.guestReviews ) > 0

        for rev = 1 : numel( airbnbStruct.guestReviews ),
            id(rev) = airbnbStruct.guestReviews{ rev }.reviewId{ 1 };
        end
        airbnbStruct.reviewIdsMap = containers.Map( id, 1 : numel( airbnbStruct.guestReviews ) );

    else
        airbnbStruct.reviewIdsMap = containers.Map('-1',0);
    end
        
                            
end