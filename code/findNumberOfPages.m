function numPages = findNumberOfPage( listing, theDir )

%% Read input file
strContents = urlread( ['https://www.airbnb.com/rooms/' listing ]);

numbers = [];
reviewsPages = regexp( strContents, 'reviews_page=\d*', 'match');
for revs = 1 : numel( reviewsPages );
    pages( revs ) = regexp( reviewsPages{ revs }, '\d*', 'match');
    numbers( revs ) = str2num( pages{ revs } );
end

if ~isempty( numbers )
    numPages = max( numbers );
else
    numPages = 1;
end

end
