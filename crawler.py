import requests
from bs4 import BeautifulSoup, SoupStrainer

def search(word):
    response = requests.get('http://www.google.com/search', params={'q': word})

    soup_strainer = SoupStrainer('li.g')
    soup = BeautifulSoup(response.text)
    print(soup.select('li.g'))
    
    for li_tag in soup:
        # a_tag = li_tag.select('h3.r > a:first-child')
        print(li_tag)

search('python')
