# Homework-10-Submission
Web-scrapping Assignment

Step 1 - Scraping

Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.


Create a Jupyter Notebook file called mission_to_mars.ipynb and use this to complete all of your scraping and analysis tasks. The following outlines what you need to scrape.



1. NASA Mars News
Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

2. JPL Mars Space Images - Featured Image
Visit the url for JPL Featured Space Image here.
Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.

3. Mars Weather
Visit the Mars Weather twitter account here and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called mars_weather.

4. Mars Facts
Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
Use Pandas to convert the data to a HTML table string.

5. Mars Hemispheres
Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.


Step 2 - MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
