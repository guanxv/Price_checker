import requests
from random import randint
from time import sleep


def getMultiPageRespond(theURL, totalPages):

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