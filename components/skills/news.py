# Function Def'n
# Separate news headlines and its page from its RSS feed

import sys
sys.path.append(r"C:\Users\Peter\Desktop\IRIS\components\lib")
import header as h

news_url="https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml"
Client=h.urlopen(news_url)
xml_page=Client.read()
Client.close()

soup_page=h.soup(xml_page,"xml")
news_list=soup_page.findAll("item")

# store top 10 news headlines as a list of strings
def news():
    head = []

    # Print news title
    for news in news_list:
        head.append(news.title.text)

    head = head[:10]
    return head

# store top 10 news webpage links as a list of strings
def page():
    page = []

    for news in news_list:
        page.append(news.link.text)

    page = page[:7]
    return page
