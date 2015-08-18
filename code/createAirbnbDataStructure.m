clc
clear

%%
clear
prefix = 'sanmiguel';

theDir = [ '../data/snapshots/08112015/' prefix '/'];
listings = textread( [ theDir prefix '_listings.txt' ] );


for l = 1 : numel( listings )
    
    listing =  num2str( listings( l ) ) ;
    fprintf('>>listing: %s (%d) \n', listing, l);
    lstruct( l )  = createAirbnbStruct( theDir, listing );
end

filename = [ 'lstruct_' prefix '.mat' ];
save( ['../data/snapshots/08112015/'  prefix '/'  filename ], 'lstruct' );



