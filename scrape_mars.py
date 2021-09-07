from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
from webdriver_manager.chrome import ChromeDriverManager

def update():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    all_results ={}

    url = "https://redplanetscience.com/"
    browser.visit(url)

    time.sleep(1)

    html = browser.html
    soup = bs(html, 'html.parser')


    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text

    image_url = 'https://spaceimages-mars.com/'
    browser.visit(image_url)

    time.sleep(1)

    image_html = browser.html
    soup = bs(image_html, 'html.parser')

    image = soup.find('img', class_="headerimage fade-in")

    image

    featured_image_url = image_url + image['src']
    
    # Mars Facts

    facts_url = 'https://galaxyfacts-mars.com/'
    browser.visit(facts_url)

    time.sleep(1)


    facts_html = browser.html
    soup = bs(facts_html, 'html.parser')


    table = pd.read_html(facts_html)
    fact_df = table[0]
    fact_df.columns = ['', 'Mars', 'Earth']
    html_table = fact_df.to_html(index=False, header="Mars Facts", border=1)

    # Mars Hemispheres

    hemi_url = 'https://marshemispheres.com/'
    browser.visit(hemi_url)

    time.sleep(1)


    hemi_html = browser.html
    soup = bs(hemi_html, 'html.parser')


    hemi_items = soup.find_all('div', class_= 'item')
    hemisphere_urls = []

    for item in hemi_items:
        hemisphere_urls.append(f"{hemi_url}{hemi_items.a['href']}")

    print(hemisphere_urls)


    import requests


    host = "https://marshemispheres.com/"
    html = requests.get(hemisphere_urls[0]).text
    image_soup = bs(html, 'html.parser')
    images = host+image_soup.find('img', class_='wide-image')['src']
    title = image_soup.find('h2', class_='title').text

    print(title, images)


    hemisphere_titles = []

    for url in hemisphere_urls:
        html = requests.get(url).text
        image_soup = bs(html, 'html.parser')
        image = host+image_soup.find('img', class_='wide-image')['src']
        # print(image)
        # hemi_img_url = soup.find('img', class_='wide-image')['src']
        title = image_soup.find('h2', class_='title').text

        hemisphere_titles.append({'title': title,
                                    'img': f"{image}"})

    print(hemisphere_titles)


    browser.quit()

    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured img": featured_image_url,
        "mars_facts": html_table,
        "hemi_images": hemisphere_titles
    }

    return mars_data
