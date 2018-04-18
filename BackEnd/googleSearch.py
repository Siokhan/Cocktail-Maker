import json
import requests
from time import sleep
from bs4 import BeautifulSoup

url = "https://www.google.co.uk/search?q="
selector = '#resultStats'
results = open('popularity.csv', 'a')
# results.write('name, popularity \n')
with open('cocktailList.json') as json_data:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
    }
    cocktails = json.load(json_data)
    for cocktail in cocktails[242:]:
        r = requests.get(
            url + '"' + cocktail['strDrink'] + '"' + ' cocktail',
            headers=headers 
            )
        data = r.text
        soup = BeautifulSoup(data, 'html.parser')
        stats = soup.select(selector)
        print(stats)
        value = int(stats[0].text.split(' ')[1].replace(',','')) 
        print(cocktail['strDrink'], value)
        results.write('{}, {}\n'.format(cocktail['strDrink'], value))
        sleep(1)
        


# r  = requests.get(url)
# data = r.text

# soup = BeautifulSoup(data)
# for link in soup.select( 'html body div.non-overlay.gray-trans-back div.container div.row div.span8 div#eh-1748056798.events-horizontal div.eh-container.row ul.eh-slider li.h-item div.h-meta div.title a[href]'):
#     print link.get('href')