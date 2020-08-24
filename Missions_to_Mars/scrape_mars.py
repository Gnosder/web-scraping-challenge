# Imports
from splinter import Browser
from bs4 import BeautifulSoup as bs

# init Browser
def init_browser():
    #from webdriver_manager.chrome import ChromeDriverManager
    executable_path = {"executable_path": "/Users/Patri/chromebrowser/chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

# Scrape Mars news
def news_get():
    # Return latest news title and story
    browser = init_browser()
    news_title = ""
    news_p = ""
    url = "https://mars.nasa.gov/news/"

    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")
    
    try:
        news_title = soup.find("div", class_="content_title").text
    except:
        news_title = sys.exc_info()[0]

    try:
        news_p = soup.find("div", class_="article_teaser_body").text
    except:
        news_p = sys.exc_info()[0]

    return news_title, news_p

# Scrape JPL images
def feat_img():
    # Return featured image
    import cssutils

    browser = init_browser()
    featured_image_url = ""

    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")

    dirty_img_url = cssutils.parseStyle(soup.find('article')['style'])['background-image']
    clean_url = dirty_img_url.replace('url(','').replace(')','')
    featured_image_url = "https://www.jpl.nasa.gov" + clean_url
    return featured_image_url

# Scrape mars facts
def mars_facts():
    # Return table of mars facts
    import pandas as pd
    import lxml
    url = "https://space-facts.com/mars/"
    mars_table = ""

    df_list = pd.read_html(url)

    mars_table = df_list[0].to_html

    return mars_table