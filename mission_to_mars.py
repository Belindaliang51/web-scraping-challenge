#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import requests
from bs4 import BeautifulSoup as bs
from splinter import Browser


# In[2]:


# URL for page to be scraped
url = 'https://mars.nasa.gov/news/'


# In[3]:


# Retrieve page with requrests module
response = requests.get(url)


# In[4]:


# Create BeautifulSoup Object; parse with 'html.parser'
soup = bs(response.text, 'html.parser')


# In[5]:


# Display the html
#print(soup.prettify())


# In[6]:


news_title = soup.find('div', class_="content_title").text.strip()
news_p = soup.find('div', class_ = 'rollover_description_inner').text.strip()
print(f'Latest news: {news_title}')
print(f'News Paragraph: {news_p}')


# In[29]:


# JPL Mars Space Images - Featured Image
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[30]:


# Browse the url
jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(jpl_url)


# In[31]:


# Click the 'full image'
browser.click_link_by_id('full_image')


# In[35]:


html = browser.html
soup = bs(html, "html.parser")
img_url = soup.find('img', class_ = 'fancybox-image')['src']


# In[36]:


img_url


# In[37]:


base_url='https://www.jpl.nasa.gov/'
featured_img_url = base_url+img_url
featured_img_url


# In[137]:


# Mars Weather
weather_url = 'https://twitter.com/marswxreport?lang=en'
response = requests.get(weather_url)


# In[140]:


mars_weather_soup = bs(response.text, 'html.parser')
type(mars_weather_soup)


# In[149]:


mars_weather_tweet = mars_weather_soup.find('span', class_ = "css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0")
print(mars_weather_tweet)


# In[150]:


import pandas as pd


# In[15]:


mars_facts_url = 'https://space-facts.com/mars/'


# In[29]:


tables = pd.read_html(mars_facts_url)
tables[0]


# In[33]:


mars_df = tables[0]
mars_df.columns=['Description','Value']
mars_df.set_index('Description')


# In[43]:


html_table = mars_df.to_html()
html_table = html_table.replace('\n','')
html_table
mars_df.to_html('mars_table.html')


# In[125]:


# Mars Hemispheres
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


# In[126]:


hemisphere_image_urls


# In[ ]:





# In[ ]:





# In[ ]:




