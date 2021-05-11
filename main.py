import requests
from bs4 import BeautifulSoup
from functions import parse_cards
import time
import pandas as pd

url = f'https://dominos.by/'
r = requests.get(url)
result = pd.DataFrame()
soup = BeautifulSoup(r.text, features='html.parser')
divs = soup.find_all('div', {'class': 'product-card'})

for item in divs:
    res = parse_cards(item)
    result = result.append(res, ignore_index=True)
start = time.time()
result.to_excel('result.xlsx')
end = time.time()

print(f'time: {end - start:.4f}')



