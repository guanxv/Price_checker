import requests
import json
from bs4 import BeautifulSoup

# with open ('jsonfile') as f:
#    data = json.load(f)

# products = json.dumps(data, indent=2)

# for item in data["data"]:
#    print(item["displayName"])

with open("dd") as file:
    strs = file.read()

print(strs)

strs = strs.replace("\\\\u0026", "d")
print(strs)


"""
a = "abc\\\\u0026"

print(a)

a = a.replace("\\\\u0026", "d")

print (a)
"""

a = "\\u0026"
print(a.encode("byte"))
