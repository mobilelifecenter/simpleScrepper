clc
clear

%%
clear
theDir = '../data/snapshots/06082015/sanmiguel/';
listings = textread( [ theDir 'sanmiguel_listings.txt' ] );


for l = 1 : numel( listings )
    
    listing =  num2str( listings( l ) ) ;
    fprintf('>>listing: %s (%d) \n', listing, l);
    lstruct( l )  = createAirbnbStruct( theDir, listing );
end

save( 'sanmiguel_lstruct', 'lstruct' );


