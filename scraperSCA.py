import requests
from random import randint
from time import sleep
from bs4 import BeautifulSoup
import json


URL = "https://www.supercheapauto.com.au/shop-by-category/oils-fluids-and-filters/engine-oil/full-synthetic-oils?start=60&sz=60"

def getMultiPageRespondSCA(theURL, totalPages):

    allPages = []

    for pageNum in range(1, totalPages + 1):

        sleep(randint(1, 5))

        # generate request
        payload = {
            "start": (pageNum -1) * 60,
            "sz": 60
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
        }

        r = requests.get(theURL, headers=headers, params=payload)

        the_page = r.content

        allPages.append(the_page)

        print("page respond received...")

    return allPages




def respondProcessSCA(the_pages):

    all_divs_json = []
    
    for page in the_pages: 

        soup = BeautifulSoup(page, "html.parser")

        product_tiles = soup.find_all("div", attrs={"class": "product-tile"}) # find all the divs with class = 'product tile'

        for tile in product_tiles:

            unquoted = requests.utils.unquote(tile["data-gtm"])              # decode url to text 
            data_json = json.loads(unquoted)                                 #load into json format
            product_dict = data_json['ecommerce']['click']['products'][0]   #removed not requried upper json structure

            #add the one more key for the link of the pictures.
            
            all_divs_json.append(product_dict)                  #append to json,

    unique_product_json = list({ x['id'] : x for x in all_divs_json }.values())       # remove duplicated products

    return unique_product_json


pages = getMultiPageRespondSCA(URL, 5)

# print(pages)

all_jsons = respondProcessSCA(pages)

print(len(all_jsons))

print(json.dumps(all_jsons, indent = 2))

