import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'http://www.owgr.com/ranking'

# generate request
#headers = {
#    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
#r = requests.get(URL, headers=headers)
#print(r.text)
#soup = BeautifulSoup(r.text, 'html.parser')

#table_body = soup.find('div',attrs = {"class": "table_container"})

#thead = table_body.thead.tr

#for th in thead:
#    print(th.th.text)

df = pd.read_html(URL)[0]

print(df)

df.to_csv('golf.csv')