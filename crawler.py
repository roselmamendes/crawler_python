import requests
from bs4 import BeautifulSoup, SoupStrainer

def search(word):
    response = requests.get('http://www.google.com/search', params={'q': word})

    soup = BeautifulSoup(response.text)
    li_tags = soup.select('li.g')
    
    for li_tag in li_tags:
        a_tag = li_tag.select('h3.r > a:first-child')

        title = a_tag[0].get_text()
        url = formata_url(a_tag[0].get('href'))
        print(title)
        print(url)

def formata_url(url):
	return url[url.find('http'):url.find('&sa')]

search('python')
