import requests
from bs4 import BeautifulSoup
from inflection import titleize

def title_gen(links):
    titles = []

    def post_format(url):
        if 'posts' in url:
            url = url.split('/')[-1]
            url = url.replace('-', ' ')
            url = titleize(url)
            titles.append(url)

    for link in links:
        if link.get('href') == None:
            continue
        else:
            post_format(link.get("href"))
            
    return titles

r = requests.get('http://www.dailysmarty.com/topics/python')
soup = BeautifulSoup(r.text, 'html.parser')
links = soup.find_all('a')
titles = title_gen(links)

for title in titles:
    print(title)

