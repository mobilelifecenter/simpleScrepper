clc
clear

%%
clear
prefix = 'guanajuato';

theDir = [ '../data/snapshots/06082015/' prefix '/'];
listings = textread( [ theDir prefix '_listings.txt' ] );


for l = 1 : numel( listings )
    
    listing =  num2str( listings( l ) ) ;
    fprintf('>>listing: %s (%d) \n', listing, l);
    lstruct( l )  = createAirbnbStruct( theDir, listing );
end

save( 'sanmiguel_lstruct', 'lstruct' );


