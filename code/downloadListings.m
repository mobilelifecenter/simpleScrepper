clc
clear
%% This script may take sometime to finish depending on the
%% network bandwidth and the number of pages associated with each listing 

prefix = 'guanajuato';
theDir = [ '../data/snapshots/06082015/' prefix '/' ];


listings = textread( [ theDir  prefix '_listings.txt' ] );

%%

for l = 1 : numel( listings ) %169
   
    listing =  num2str( listings( l ) ) ;
    %listing = '42817';

    fprintf('%d %s\n', l, listing );
    try
        readHTML( listing, theDir );
    catch %retry
        readHTML( listing, theDir );
    end
    
    numPages = findNumberOfPages( listing, theDir );
    fprintf('pages: %d\n', numPages );
    
    fid = fopen( [ theDir listing '/' listing  '_metadata.txt' ], 'w');
    fprintf( fid, '%d', numPages );
    fclose( fid );

    strContents = '';

    if numPages > 1
        for i = 2 : numPages,

            for j = 1 : 5 % try five times
                try
                    strContents = urlread( ['https://www.airbnb.com/rooms/' listing '?reviews_page=' num2str( i )  ]);
                    break;
                catch e
                    fprintf('.\n');
                end    
                    
            end
            fid = fopen( [ theDir listing '/' listing  '_' num2str( i )  '.html'], 'w');
            fprintf( fid, '%s', strContents );
            fclose( fid );
        end
    end
    
end

%%
fid = fopen( [ theDir  prefix '_listings_py.txt' ], 'w');
for l = 1 : numel( listings ) - 1
   
    listing =  num2str( listings( l ) ) ;
    fprintf( fid, '%s\n', listing );
    
end
listing =  num2str( listings( l + 1 ) ) ;
fprintf( fid, '%s', listing );

fclose( fid );

%% It takes a long time to download all the images


for l = 1 : numel( listings )
   
    listing =  num2str( listings( l ) ) ;
    crawlForImages( listing, theDir );
end