function crawlForImages( listing, theDir )
readUrl = true;

%% Read input file
%dir = '../data/';
%mkdir( [ dir listing ] )
%mkdir( [ dir listing '/images' ] );


if ~readUrl
    sourceFile = 'w.html';
    strContents = fileread( sourceFile ); 
else
    strContents = urlread( ['https://www.airbnb.com/rooms/' listing ]);    
end

%%
tokens = regexp( strContents, 'https://a([0123456789]).muscache.com/ic/pictures[^\?]*', 'match');
tokens = unique( tokens );
for t = 1 : numel( tokens )
   imagen = imread( char(unicode2native(tokens{ t })) );
   imwrite( imagen, [ theDir listing '/images/' listing '_image_' num2str(t) '.jpeg' ] );  
end

%%

end
