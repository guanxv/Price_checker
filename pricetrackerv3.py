import urllib.parse
import urllib.request
from respondprocess import webRespondProcess

import json

# URL = "https://www.bunnings.com.au/our-range/brands/o/ozito-power-x-change"
# URL = "https://www.google.com"#
URL = "https://www.bunnings.com.au/our-range/brands/o/ozito-pxc?facets=CategoryIdPath%3D2a021706-07d5-4648-bf26-2ea8fea049df"

headers = {"User-Agent": "Mozilla/5.0"}

req = urllib.request.Request(URL, headers=headers)
the_page = urllib.request.urlopen(req).read()

data = webRespondProcess(the_page)

print(data)

#print(type(data))

"""
# generate request
values = {
    "facets": "CategoryIdPath%3D2a021706-07d5-4648-bf26-2ea8fea049df",
    "page": 1,
}

data = urllib.parse.urlencode(values)
req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)
the_page = response.read()


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
}
r = requests.get(URL, headers=headers, params=payload)
#r = requests.get(URL, headers=headers)
#print(r.headers)

soup = BeautifulSoup(r.content, "html.parser")

soup.prettify()

#a = str(soup).encode("utf8", errors = "ignore").decode("utf8")
#print(type(a))

#with open ("sample.html","w") as f:
#    f.write(str(soup))
"""
