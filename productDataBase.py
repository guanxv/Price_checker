import sqlite3
from temp import tempList

# using this method for testing
#conn = sqlite3.connect(":memory:")
conn = sqlite3.connect("bunningsProduct.db")

c = conn.cursor()

# create database


def createDB():
    c.execute(
        """CREATE TABLE products (fineline text, displayname text, producturl text, brandname text, brandlogo text, categorynamepath text, forhire text, unitofmeasure text, price real, hascomparisonprice text, comparisonpriceunits real, comparisonpriceuom text, isspecialorder text ,availablefororderonline text, availableforpickup text, availablefordelivery text, istradingrestricted text, isthirdparty text, isbundle text, iscustommade text, haspoadelivery text, productimage text, checkstoreforprice text, stockstatus text, isfeatured text, sellername text, ismarketplaceproduct text, showstocklevel text, isinstore text)"""

    )

    print("Database Created...")


def insert_product(productDict):
    with conn:
        c.execute(
            """INSERT INTO products VALUES (:fineline, :displayname, :producturl, :brandname, :brandlogo, :categorynamepath, :forhire, :unitofmeasure, :price, :hascomparisonprice, :comparisonpriceunits, :comparisonpriceuom, :isspecialorder, :availablefororderonline, :availableforpickup, :availablefordelivery, :istradingrestricted, :isthirdparty, :isbundle, :iscustommade, :haspoadelivery, :productimage, :checkstoreforprice, :stockstatus, :isfeatured, :sellername, :ismarketplaceproduct, :showstocklevel, :isinstore)""",
            {
                "fineline": productDict["fineLine"],
                "displayname": productDict["displayName"],
                "producturl": productDict["productUrl"],
                "brandname": productDict["brandName"],
                "brandlogo": productDict["brandLogo"],
                "categorynamepath": productDict["categoryNamePath"],
                "forhire": productDict["forHire"],
                "unitofmeasure": productDict["unitOfMeasure"],
                "price": productDict["price"],
                "hascomparisonprice": productDict["hasComparisonPrice"],
                "comparisonpriceunits": productDict["comparisonPriceUnits"],
                "comparisonpriceuom": productDict["comparisonPriceUom"],
                "isspecialorder": productDict["isSpecialOrder"],
                "availablefororderonline": productDict["availableForOrderOnline"],
                "availableforpickup": productDict["availableForPickUp"],
                "availablefordelivery": productDict["availableForDelivery"],
                "istradingrestricted": productDict["isTradingRestricted"],
                "isthirdparty": productDict["isThirdParty"],
                "isbundle": productDict["isBundle"],
                "iscustommade": productDict["isCustomMade"],
                "haspoadelivery": productDict["hasPOADelivery"],
                "productimage": productDict["productImage"],
                "checkstoreforprice": productDict["checkStoreForPrice"],
                "stockstatus": productDict["stockStatus"],
                "isfeatured": productDict["isFeatured"],
                "sellername": productDict["sellerName"],
                "ismarketplaceproduct": productDict["isMarketplaceProduct"],
                "showstocklevel": productDict["showStockLevel"],
                "isinstore": productDict["isInStore"],
            },
        )
    
    print('One Product inserted...')

def insert_products(producstDict):
    
    for product in producstDict:

        insert_product(product)


def get_product_by_fineline(fineline):
    c.execute(
        "SELECT * FROM products WHERE fineline = :fineline", {"fineline": fineline}
    )  # SELECT command dont need to be commited. so dont need with:.
    return c.fetchall()


productsample = {
    "fineLine": "0013581",
    "displayName": "Ryobi 18V One+ 2.5/5.0Ah Lithium+ Battery Combo",
    "productUrl": "/ryobi-18v-one-2-5-5-0ah-lithium-battery-combo_p0013581",
    "brandName": "Ryobi",
    "brandLogo": "https://media.bunnings.com.au/Brand-62x40/549a79f0-2f37-4915-9c33-b8746491748e.png",
    "categoryNamePath": "Our Range > Tools > Power Tools > Batteries & Chargers",
    "forHire": False,
    "unitOfMeasure": "Each",
    "price": 179.0,
    "hasComparisonPrice": False,
    "comparisonPriceUnits": 0.0,
    "comparisonPriceUom": "",
    "isSpecialOrder": False,
    "availableForOrderOnline": True,
    "availableForPickUp": True,
    "availableForDelivery": True,
    "isTradingRestricted": False,
    "isThirdParty": False,
    "isBundle": False,
    "isCustomMade": False,
    "hasPOADelivery": False,
    "productImage": "https://media.bunnings.com.au/Product-190x190/c4b04c8b-52ea-4223-a327-fd7f12a74d41.jpg",
    "checkStoreForPrice": False,
    "stockStatus": None,
    "isFeatured": False,
    "sellerName": "",
    "isMarketplaceProduct": False,
    "showStockLevel": True,
    "isInStore": True,
    "productRatings": {"averageOverallRating": 5.0, "totalReviewCount": 5},
    "priceHistory": {20200916: 179.0, 20200917: 180.0},
}


def get_keys(the_dict):

    keys = []

    for key in the_dict:

        key = key.lower()

        keys.append(key)

    return keys


# createDB(productsample)

# for product in tempList:
    
#     insert_product(product)



#print(get_product_by_fineline("0208112"))

#conn.close()
