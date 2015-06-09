README simpleScrapper V 0.1 

With the current version of the scrapper one need to conduct several
steps, which are described below. Few of these steps are not
fully automated. However, future versions that follow could 
achieve a fully automated scrapping procedure.

Some steps are conducted through matlab scripts and functions;
others use scripts written in python. Future versions of
the code should be standardized and written in python.

Three key tools are used to support the scrapper functionality:
1) the BeautifulSoup from the bs4 python module, 2) the re
(regular expressions) python module) and 3) xml and re helper functions
 available in matlab.

These tools allow the scrapper to find unambigous
patterns in the html files that are used to extact data.

The scrapper code and data are stored in a folder named
simpleScrapper which are currently organized as follows:

simpleScrapper -- code
               -- data -- places    -- guanajuato
                                    -- sanmiguel
                                    -- leon
                                    -- .
                                    -- .
                                    -- ... (others)

                       -- snapshots -- 06082015  -- guanajuato
                        			 -- sanmiguel
                        			 -- leon
			                         -- .
                                                 -- .
                                                 -- ... (others)

 
Here we show how to scrap data from Guanajuato
City as a means to illustrate how the scrapper works.

1. Run script scapListingsNumbers.py located in code's folder.
In order to run this script, you should have each of the
html files associated with the pages showing the listings. 
stored in the directory places/guanajuato/ .
	For instance if you look for Guanajuato 
in Aibnb, you get up to html 29 pages showing each of the
available places.  These files should saved into folder
places/guanajuato/ , and  named 1.html, 2.html,..., 8.html.
	A manifest.txt file containing the names these files should 
also be available in places/guanajuato/ .
	After runing the script, scraped data be stored in
guanajuato_listings.txt file. 

2. Copy the file  guanajuato_listings.txt into the folder
snapshots/06082015/guanajuato. Here we are making a snapshot
of the data corresponding to the date 06-08-2015. 
(This is silly but, this is the way things are implemented for now; 
we need to streamline all the procedures in a future version.)

3. Run the script downloadListings.m

4. Run the script callSimpleScrapper.py . 
Folder /snapshots/06082015/guanajuato/ will listings' data.
Look for the .xml files for the scrapped data.

5. Run the script createAirbnbDataStructure.m to create a
matlab data structure array that stores the xml data
in a more redouble form.




