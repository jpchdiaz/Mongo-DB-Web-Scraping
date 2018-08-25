from splinter import Browser
from bs4 import BeautifulSoup

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

#Mars News
def mars_news():
    
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    for x in range(1, 2):
    
        html = browser.html
        soup = bs(html, 'html.parser')

        titles = soup.find_all('div', class_='list_text')

        for title in titles:
            return print('-----')
            news_title = title.find('div', class_='content_title').find('a').text
            news_print = title.find('div', class_='article_teaser_body').text
            return news_title
            return news_print
    
#JPL Featured Image
def featured_img():
    
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    
    for x in range(1, 2):

        html = browser.html
        soup = bs(html, 'html.parser')

        featured_image = soup.find('article')['style']
        url_extract = re.search("'.*'", featured_image).group(0).replace("'", "")
        featured_image_url = (f'https://www.jpl.nasa.gov{url_extract}')

    return featured_image_url
#Mars Weather
def mars_weather():
    
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    
    for x in range(1, 2):
    
        html = browser.html
        soup = bs(html, 'html.parser')

        tweets = soup.find_all('div', class_='js-tweet-text-container')

        mars_weather = tweet.find('p').text

    return mars_weather
    

#Mars Facts
def mars_facts():
    url = 'http://space-facts.com/mars/'
    
    tables = pd.read_html(url)
    df = tables[0]
    df.columns = ['', 'Mars']
    df.set_index('', inplace=True)
    html_table = df.to_html()
    html_table.replace('\n', '')
    
    return html_table
#Mars Hemispheres
def mars_hemis():
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

    return hemisphere_image_urls