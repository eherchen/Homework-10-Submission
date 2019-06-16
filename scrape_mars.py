# Import dependencies
from bs4 import BeautifulSoup as bs
import pymongo
from splinter import Browser
import pandas as pd
from selenium import webdriver
import time

# chrome_path = r"C:\chromedriver_win32\chromedriver.exe"
# driver = webdriver.Chrome(chrome_path)
# driver.get("https://mars.nasa.gov/news/")

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": 'chromedriver.exe'}
    return Browser("chrome", **executable_path, headless=False)

   

def scrape_info():
    mars_data = {}
    browser = init_browser()

    # Scrap Mars.NASA.gov for latest news
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Save latest news title and summary
    mars_data["title"] = soup.find("div", class_="content_title").text
    mars_data["paragraph"] = soup.find("div", class_="article_teaser_body").text

    # Scrap Mars Space Images
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    time.sleep(2)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Parse the link for the featured image
    relative_image_path = soup.find("a", class_="button")["data-link"]
    base_url = "https://www.jpl.nasa.gov"
    mars_img_link = base_url + relative_image_path
    
    # Find the featured image title
    browser.visit(mars_img_link)
    html = browser.html
    soup = bs(html, 'html.parser')
    soup.title.text

    # Parse the link for the image
    mars_image_url = soup.find('figure', class_="lede").a["href"]
    
    # Save Full image link
    mars_data["featured_image_url"] = base_url + mars_image_url

    # Scrap Mars Weather
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    time.sleep(3)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Save weather data
    mars_data["mars_weather"] = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    
    # Scrap Mars Facts
    url = "https://space-facts.com/mars/"
    browser.visit(url)
    time.sleep(4)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Pull Mars table
    mars_facts = pd.read_html("https://space-facts.com/mars/")[0]
    mars_facts.columns = ["Description", "Value"]
    
    # Save Mars Facts table
    mars_facts_html = mars_facts.to_html(classes="table table-striped")
    mars_data["mars_facts_html"] = mars_facts_html

    # Scrap Mars Hemisphere data
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    time.sleep(5)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    xpath = '//div[@class="description"]//a[@class="itemLink product-item"]/h3'
    results = browser.find_by_xpath(xpath)

    hemisphere_img_results = []

    for i in range(4):
        html = browser.html
        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')
        results = browser.find_by_xpath(xpath)
        img_header = results[i].html
    
        scrape_url = results[i]
        scrape_url.click()
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        hemisphere_img_results.append({"title": img_header, "image_url": soup.find("div", class_='downloads').a['href']})

    
    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
    