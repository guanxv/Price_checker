from respondprocess import webRespondProcess
from getURLRespond import getMultiPageRespond


URL = "https://www.bunnings.com.au/our-range/brands/o/ozito-power-x-change"
# URL = "https://www.bunnings.com.au/our-range/brands/r/ryobi-one-"

allThePages = getMultiPageRespond(URL, 5)

# print(allThePages)

allProduct = []

for page in allThePages:

    dictData = webRespondProcess(page)

    allProduct += dictData

print(allProduct)

# price history add key

"""

{
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
        "priceHistory":{20200916 : 179.0, 20200917 : 180.0}
    }

"""

#read and write to a sql lite File
