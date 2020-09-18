from respondprocess import webRespondProcess
from getURLRespond import getMultiPageRespond
import productDataBase as pdb
import sqlite3


URL = "https://www.bunnings.com.au/our-range/brands/o/ozito-power-x-change"
# URL = "https://www.bunnings.com.au/our-range/brands/r/ryobi-one-"

allThePages = getMultiPageRespond(URL, 5)

# print(allThePages)

allProduct = []

for page in allThePages:

    dictData = webRespondProcess(page)

    allProduct += dictData

#print(allProduct)

pdb.createDB()

pdb.insert_products(allProduct)

pdb.conn.close()
