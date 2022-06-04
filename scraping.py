# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as bs
#changed from soup to bs for ease with assignment
import pandas as pd
import datetime as dt
import time
from webdriver_manager.chrome import ChromeDriverManager

# from Booth help, class ScraperHelper
class ScraperHelper
    def __init__(self):
        pass
    def init_browser(self):
        executable_path = {'executable_path': ChromeDriverManager().install()}
        browser = Browser('chrome', **executable_path, headless=True)

    def scrape_info(self):
        browser = self.init_brower()
             # Scrape Mars News
       
        # Visit the mars nasa news site
        url = 'https://redplanetscience.com'
        browser.visit(url)
    
        # Optional delay for loading the page
        browser.is_element_present_by_css('div.list_text', wait_time=1)

        html = browser.html
        news_soup = bs(html, 'html.parser')

        slide_elem = news_soup.select_one('div.list_text')
        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    # ## JPL Space Images Feature Image

        # Visit URL
        url = 'https://spaceimages-mars.com'
        browser.visit(url)
        time.sleep(1)

        # Find and click the full image button
        full_image_elem = browser.find_by_tag('button')[1]
        full_image_elem.click()

        # Parse the resulting html with soup
        html = browser.html
        img_soup = bs(html, 'html.parser')

        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
        featured_img_url = f'https://spaceimages-mars.com/{img_url_rel}'
        
    # ## Mars Facts
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
   # Assign columns and set index of dataframe
        df.columns=['Description', 'Mars', 'Earth']
        df.set_index('Description', inplace=True)
        table__html = df.to_html()

# hemis
        url = 'https://marshemispheres.com/'
        browser.visit(url)
        time.sleep(1)

        # Parse the resulting html with soup
        html = browser.html
        img_soup = bs(html, 'html.parser')

        items = soup.find("div", {"class":"results"}).find_all("div", {"class", "item"})
# init return 
        hemisphere_image_urls = []

        # for each hemi on the main page
        for item in items:
            # grab the link out of it
            link = item.find("a", {"class": "itemLink"})["href"]
            full_url = url + link
            
            # visit the link
            browser.visit(full_url)
            time.sleep(1)
            
            # soupify
            html = browser.html
            soup = bs(html, 'html.parser')
            
            # grab the data we want
            img = soup.find("img", {"class", "wide-image"})["src"]
            img_url = url + img
            
            title = soup.find("h2", {"class": "title"}).text
            title = title.split("Enhanced")[0].strip()
            
            data = {"img_url" : img_url, "title":title}
            
            hemisphere_image_urls.append(data)

        # Store data in a dictionary
        mars_data = {
            "news_title": news_title,
            "news_paragraph": news_p,
            "featured_image": featured_img_url,
            "facts": table_html,
            "hemispheres": hemisphere_image_urls
        }

        # Quite the browser after scraping
        browser.quit()

        # Return results
        return mars_data

