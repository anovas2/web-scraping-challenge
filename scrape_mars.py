
# coding: utf-8

# In[87]:


from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser


# In[88]:



def scrapemarsnews():
    browser = init_browser()
    marsnews = {}

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    alllistings = soup.find_all('div', class_="list_text")
    
    news_title = [x.find(class_='content_title').a.text for x in alllistings]
    news_p = [x.find(class_='article_teaser_body').text for x in alllistings]

#     print(news_title)
#     print(news_p)
    
    marsnews = {
    "news_title": news_title,
    "news_p": news_p
    }
    browser.quit()
#     display(marsnews)
    return marsnews


# In[89]:


def marsweather():
    browser = init_browser()
    marsnews = {}

    url = 'https://twitter.com/marswxreport?lang=en'

    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    mars_weather = soup.find_all('div', class_='js-tweet-text-container')
#     print(mars_weather[0])
    mars_weather = [x.p.text for x in mars_weather if 'InSight sol' in x.p.text ][0]
    
    print(mars_weather)
    browser.quit()
    return mars_weather


# In[90]:


def jpljpg():
    browser = init_browser()
    marsnews = {}

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    url2 ='https://www.jpl.nasa.gov/spaceimages/images/largesize'
    url3 = '_hires.jpg'

    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
#     print(soup)

    featured_image_url = soup.find('div', class_='carousel_items').article['style']

    char1 = '('
    char2 = ')'
    
    featured_image_url = featured_image_url[featured_image_url.find(char1)+1 : featured_image_url.find(char2)].replace("'", '')    .split('/')[-1].split('-')[0]
    featured_image_url = f'{url2}/{featured_image_url}{url3}'

    
    print(featured_image_url)
    browser.quit()
    return featured_image_url


# In[91]:


def marsfacts():
    browser = init_browser()
    marsnews = {}

    url = 'https://space-facts.com/mars/'

    tables = pd.read_html(url)
#     print(tables)[0]
    mars_facts = pd.DataFrame(tables[0])
#     browser.visit(url)
#     html = browser.html
#     soup = BeautifulSoup(html, "html.parser")
    
#     mars_weather = soup.find_all('div', class_='js-tweet-text-container')
#     print(mars_weather[0])
#     mars_weather = [x.p.text for x in mars_weather if 'InSight sol' in x.p.text ][0]
    
#     print(mars_weather)
    browser.quit()
    return mars_facts


# In[92]:


def marshemi():
    browser = init_browser()
    marsnews = {}

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'


    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
#     print(soup)

#     featured_image_url = soup.find_all('div', class_='carousel_items').article['style']

#     char1 = '('
#     char2 = ')'
    
# #     featured_image_url = featured_image_url[featured_image_url.find(char1)+1 : featured_image_url.find(char2)].replace("'", '')\
# #     .split('/')[-1].split('-')[0]
# #     featured_image_url = f'{url2}/{featured_image_url}{url3}'
    url2 = 'https://astrogeology.usgs.gov'
    titlelist = []
    img_url = []
#     links = browser.find_link_by_partial_href('/search/map/Mars/Viking')
    links = soup.find_all('div',class_='description')
    
    for link in links:
        link = link.a['href']
#         print(link)
    
        browser.visit(url2 + link)
        
        html = browser.html
        soup = BeautifulSoup(html, "html.parser")
        img_url.append(soup.find('div', class_='downloads').ul.li.a['href'])
        titlelist.append(soup.find('h2', class_='title').text)
        
#         browser.visit(url)
#         links = browser.find_link_by_partial_text('Hemisphere Enhanced')
        
#         html = browser.html
#         soup = BeautifulSoup(html, "html.parser")
    
#         title = [x.find(class_='content_title').a.text for x in alllistings]
#         img_url = [x.find(class_='article_teaser_body').text for x in alllistings]

#     print(news_title)
#     print(news_p)
    
#     marshemi = pd.DataFrame({
#     "title": titlelist,
#     "img_url": img_url
#     })
    
        marshemi = {
    "title": titlelist,
    "img_url": img_url
    }
    
#     print(marshemi)
    browser.quit()
    return marshemi


# In[95]:


def scrape():
    marsnews_dict = scrapemarsnews()
    marshemi_dict = marshemi()
    mars_facts_df = marsfacts()
    featured_image_url = jpljpg()
    mars_weather_p = marsweather()
    
    allscrape = {
    "marsnews_dict": marsnews_dict,
    "marshemi_dict": marshemi_dict,
            "mars_facts_df": mars_facts_df,
            "featured_image_url": featured_image_url,
            "mars_weather_p": mars_weather_p
        
    }
    return allscrape
    


# In[94]:


# scrape()
# 
