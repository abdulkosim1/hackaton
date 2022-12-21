import requests
import csv
from bs4 import BeautifulSoup as BS


def get_html(url):
    response = requests.get(url)
    return response.text

def get_soup(html):
    soup = BS(html, 'html.parser')
    return soup

def get_data(soup):
    global list_
    global list__
    global dict_
    global dict__
    list_ = []
    list__ = []
    news = soup.find_all('div', class_ = 'Tag--article') 
    c = 1
    dict_ = {}
    dict__ = {}
    for i in news:
        if c == 21:
            break
        title = i.find('a', class_ = 'ArticleItem--name').text.strip()
        dict_.update({str(c):title})
        
        list_.append(title)
        urls = i.find('a', class_='ArticleItem--name').get('href')
        list__.append(urls)
        image = i.find('img').get('src')
        dict__.update({str(c):image})
        c+=1


def main():
    BASE_URL = "https://kaktus.media/?lable=8&date=2022-12-21&order=time"
    html = get_html(BASE_URL)
    soup = get_soup(html)
    get_data(soup)
    global zip1
    zip1 = dict(zip(list_,list__))
    # print(dict__)
main()
