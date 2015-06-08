function readHTML( listing, theDir )

%% Read input file
mkdir( [ theDir listing ] )
mkdir( [ theDir listing '/images' ] );
strContents = urlread( ['https://www.airbnb.com/rooms/' listing ]);

fid = fopen( [ theDir listing '/' listing '.html'], 'w');
fprintf( fid, '%s', strContents );
fclose( fid );

end
