from splinter import Browser
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():

    #empty dictionary
    mars_scrape = {}

    #Mars News
    browser = init_browser()
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    for x in range(1, 2):

        html = browser.html
        soup = bs(html, 'html.parser')

        titles = soup.find_all('div', class_='list_text')

        for title in titles:
            news_title = title.find('div', class_='content_title').find('a').text
            news_print = title.find('div', class_='article_teaser_body').text
            mars_scrape['news_title'] = news_title
            mars_scrape['news_print'] = news_print

    #JPL Featured Image
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    for x in range(1, 2):

        html = browser.html
        soup = bs(html, 'html.parser')

        featured_image = soup.find('article')['style']
        url_extract = re.search("'.*'", featured_image).group(0).replace("'", "")
        featured_image_url = (f'https://www.jpl.nasa.gov{url_extract}')

    mars_scrape['featured_image_url'] = featured_image_url


    #Mars Weather
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    for x in range(1, 2):

        html = browser.html
        soup = bs(html, 'html.parser')

        tweets = soup.find_all('div', class_='js-tweet-text-container')

        for tweet in tweets:
            mars_weather = tweet.find('p').text

    mars_scrape['mars_weather'] = mars_weather

    #Mars Facts
    url = 'http://space-facts.com/mars/'

    tables = pd.read_html(url)
    df = tables[0]
    df.columns = ['', 'Mars']
    df.set_index('', inplace=True)
    html_table = df.to_html()
    html_table = html_table.replace('\n', '')

    mars_scrape['html_table'] = html_table

    #Mars Hemispheres
    cerberus_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    schiaparelli_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    syrtis_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    marineris_url ='https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'

    def image_scraper(url):
        browser.visit(url)
        html = browser.html
        soup = bs(html, 'html.parser')

        downloads = soup.find_all('div', class_='downloads')

        for images in downloads:
            scraped_imgs = images.find('a')['href']

        return scraped_imgs

    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": image_scraper(cerberus_url)},
        {"title": "Cerberus Hemisphere", "img_url": image_scraper(schiaparelli_url)},
        {"title": "Schiaparelli Hemisphere", "img_url": image_scraper(syrtis_url)},
        {"title": "Syrtis Major Hemisphere", "img_url": image_scraper(marineris_url)},
    ]

    mars_scrape['hemisphere_image_urls'] = hemisphere_image_urls

    return mars_scrape
