import re
from unicodedata import category
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


def website():
    categories = []
    url_base = 'https://www.diffordsguide.com'
    url = Request(f"{url_base}/beer-wine-spirits/spirits")
    webpage = urlopen(url).read()
    bs = BeautifulSoup(webpage, 'html.parser')
    #print (webpage)
    category = bs.find("div",{'class':'grid-x grid-margin-x grid-margin-y landing-page-grid'})
    category_link = category.findChildren('a')
    
    spirits = ['vodka','gin','rum','tequila','whiskey']
    for i in category_link:
        #category_name = re.findall(r'[0-9]+', i['href'])
        category_name = re.split(r'[0-9]+', i['href'])[1]
        #if 
        # url = Request(f"{url_base}{i['href']}")
        # webpage = urlopen(url).read()
        # bs = BeautifulSoup(webpage, 'html.parser')
        categories.append(category_name)
    return categories
print(website())


