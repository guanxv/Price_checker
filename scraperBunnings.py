#import productDataBase as pdb
import sqlite3
import json
from bs4 import BeautifulSoup
import requests
from random import randint
from time import sleep


URL = "https://www.bunnings.com.au/our-range/brands/o/ozito-power-x-change"
# URL = "https://www.bunnings.com.au/our-range/brands/r/ryobi-one-"


# -------------------- get respond bunnings ------------------------------


def getMultiPageRespondBunnings(theURL, totalPages):

    allPages = []

    for pageNum in range(1, totalPages + 1):

        sleep(randint(1, 5))

        # generate request
        payload = {
            "facets": "CategoryIdPath%3D2a021706-07d5-4648-bf26-2ea8fea049df",
            "page": pageNum,
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
        }

        r = requests.get(theURL, headers=headers, params=payload)

        the_page = r.content

        allPages.append(the_page)

        print("page respond received...")

    return allPages


# -------------- respond process bunnings ----------------------------


def RespondProcessBunnings(webRespondByte):

    # webRespondStr is respond = urllib.request.urlopen(req).read()

    # replace error and illigal charactor in the string
    a = webRespondByte.decode(
        "utf8", errors="replace"
    )  # .replace("\\\\u003e", ">" ).replace("\\\\u0026", "&").encode("utf8", errors="replace")
    b = a.replace("\\\\u003e", ">")
    c = b.replace("\\\\u0026", "&")
    d = c.encode("utf8", errors="replace")

    # the \\u003e and u0026 can not be replace by the str.replace() method, so i have to convert it to byte and replace in byte.
    e = (
        d.replace(b"u0026", b"&")
        .replace(b"u003e", b">")
        .replace(b"\\", b"")
        .replace(b"\u203a", b"")
    )

    # take the converted html byte respon into soup
    soup = BeautifulSoup(e, "html.parser")

    # print(soup.prettify().encode("utf8"))

    # find the div with json container.
    div_json = soup.find_all("div", attrs={"class": "js-product-tile-container"})

    all_data = []

    for container in div_json:
        # print(container)
        data = json.loads(container.get("data-options"))  # use get() to get the text
        data = data["data"]
        for dictionary in data:
            all_data.append(dictionary)

    print("Page content processed...")

    return all_data


allThePages = getMultiPageRespondBunnings(URL, 5)

# print(allThePages)

allProduct = []

for page in allThePages:

    dictData = RespondProcessBunnings(page)

    allProduct += dictData

print(json.dumps(allProduct, indent = 2))

# pdb.createDB()

# pdb.insert_products(allProduct)

# pdb.conn.close()
