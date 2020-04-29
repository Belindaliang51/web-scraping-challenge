
# Dependencies
import requests
from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd

## Latest news to scrape
# URL for page to be scraped
url = 'https://mars.nasa.gov/news/'

# Retrieve page with requrests module
response = requests.get(url)

# Create BeautifulSoup Object; parse with 'html.parser'
soup = bs(response.text, 'html.parser')

# Retrieve title and paragraph
news_title = soup.find('div', class_="content_title").text.strip()
news_p = soup.find('div', class_ = 'rollover_description_inner').text.strip()
print(f'Latest news: {news_title}')
print(f'News Paragraph: {news_p}')

## Featured Image
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(jpl_url)

# Click the 'full image'
browser.click_link_by_id('full_image')

html = browser.html
soup = bs(html, "html.parser")
img_url = soup.find('img', class_ = 'fancybox-image')['src']

base_url='https://www.jpl.nasa.gov/'
featured_img_url = base_url+img_url
featured_img_url

## Mars Weather
weather_url = 'https://twitter.com/marswxreport?lang=en'
response = requests.get(weather_url)

# Create beautifulSoup object 
mars_weather_soup = bs(response.text, 'html.parser')
type(mars_weather_soup)

#Scraping
mars_weather_tweet = mars_weather_soup.find('span', class_ = "css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0")
print(mars_weather_tweet)

## Spcae Facts
mars_facts_url = 'https://space-facts.com/mars/'
# To read html by pandas
tables = pd.read_html(mars_facts_url)

# Retrieve the desired table 
mars_df = tables[0]
mars_df.columns=['Description','Value']
mars_df.set_index('Description')
# Convert the table to html 
html_table = mars_df.to_html()
html_table = html_table.replace('\n','')
html_table
mars_df.to_html('mars_table.html')

## Mars Hemispheres
Mars_Hemispheres_url='https://www.planetary.org/blogs/guest-blogs/bill-dunford/20140203-the-faces-of-mars.html'
response = requests.get(Mars_Hemispheres_url)
soup=bs(response.text, 'html.parser')

hemisphere_image_urls = []

items = soup.find_all('img', class_='img840')
for item in items:
    #title = item.h5.text
    title = item['alt']
    image_url = item['src']
    
    post = {
        'title':title,
        'image_url': image_url
    }
    
    hemisphere_image_urls.append(post)

hemisphere_image_urls