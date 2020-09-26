import requests
from datetime import datetime
from random import randint
from time import sleep
from bs4 import BeautifulSoup
import json

from productDataBase import createProductDBwithDict


URL = "https://www.carsales.com.au/cars/used/volkswagen/golf/victoria-state/"


def getMultiPageRespondCarsales(theURL, totalPages):

    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
        }

    print("Start Sending Requests for Multi Pages...")

    allPages = []

    for pageNum in range(1, totalPages + 1):

        waitRandomSec(45)

        # generate request
        payload = {"offset": (pageNum - 1) * 12}
        # payload = {"offset": 548}
        

        r = requests.get(theURL, headers=headers, params=payload)

        the_page = r.content

        allPages.append(the_page)

        print("page", pageNum, "respond received. Total Page Number ", totalPages)

    return allPages


def getSinglePageRespondCarsales(theURL):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
    }

    print("Start Sending Requests for single page...")

    waitRandomSec(45)

    print(theURL)

    r = requests.get(theURL, headers=headers)

    the_page = r.content

    print("page respond received.")

    return the_page


def respondProcessCarsales(the_pages):

    all_json = []

    for page in the_pages:

        soup = BeautifulSoup(page, "html.parser")

        list_car_script = soup.find("script", attrs={"type": "application/ld+json"})

        data_cars_json = json.loads(list_car_script.string)  # load into json format

        for car_list in data_cars_json["mainEntity"]["itemListElement"]:

            car_list = car_list["item"]  # remove not wanted keys

            car_list["year"] = int(
                car_list["name"].split(" ")[0]
            )  # add year in int type

            car_list["engineSize"] = float(
                car_list["vehicleEngine"]["engineDisplacement"]["value"]
                .split(" ")[1]
                .strip("L")
            )  # add engine size in liter in int

            car_list["numberOfCylinder"] = int(
                car_list["vehicleEngine"]["engineDisplacement"]["value"]
                .split(" ")[0]
                .strip("cyl")
            )  # add number of cylinder in num

            if (
                "Petrol".lower()
                in car_list["vehicleEngine"]["engineDisplacement"]["value"].lower()
            ):  # add fuel type

                car_list["fuelType"] = "Petrol"

            else:

                car_list["fuelType"] = "Diesel"

            car_list["odometer"] = int(
                car_list["mileageFromOdometer"]["value"]
            )  # move odometer key in top level for easier access, change to int type

            try:

                if (
                    "private" in car_list["image"][0]["url"]
                ):  # is it private or dealer car , add list type in 'string'

                    car_list["list_type"] = "private"

                else:

                    car_list["list_type"] = "dealer"

            except:

                car_list["list_type"] = "private"

            all_json.append(car_list)  # append to json,

    return all_json


def getCarDetailPageData(
    productsJason,
):  # send request to url of each cars to get more details like, color, price_type, motor Kw etc...

    for carData in productsJason:

        page = getSinglePageRespondCarsales(carData["url"])

        soup = BeautifulSoup(page, "html.parser")

        the_script = "" 
        
        all_script = soup.find_all(lambda tag : tag.name == "script" )  # find all scripts

        for scr in all_script:

            try:
                
                if 'window.CsnInsights.metaData' in scr.string and 'isdealerbranding' in scr.string:

                    a = scr.string  # find the scipt section contain the json for the car details
                    
                    a = a[a.index('"')-1:]  #buchter the string , prepare for json
                    a = a[:a.index('}')+1]

                    the_script = a
  
            except:

                pass

        car_jason = json.loads(the_script)

        # print(car_jason)

        #update the original json

        
        carData['fuelType'] = car_jason['fuelType']
        carData['colour'] = car_jason['colour']
        carData['bodyStyle'] = car_jason['bodystyle']
        carData['badge'] = car_jason['badge']
        carData['make'] = car_jason['make']
        carData['ad_type'] = car_jason['contentGroup3']
        carData['priceType'] = car_jason['pricetype']
        #carData['priceIndicator'] = car_jason['priceindicator']
        carData['state'] = car_jason['state']

        # find more info

            #rego expire date        

        try:

            regoExpTag = soup.find('div', attrs={'class' : "col features-item-value features-item-value-registration-expiry" })

            regoExpDateStr = regoExpTag.text

            # regoExpDateObj = datetime.strptime(regoExpDateStr, '%b %Y' )

            # regoDaysToExp = (datetime.now() - date_obj).days

            carData['regoDaysToExp'] = regoExpDateStr

            # print(regoExpTag)
        
        except :

            carData['regoDaysToExp'] = 'Check with seller'
       
        enginePower = soup.find('div', attrs={'class' : "col features-item-value features-item-value-power" }).string
        carData['enginePower'] = enginePower

        engineTorque = soup.find('div', attrs={'class' : "col features-item-value features-item-value-torque" }).string
        carData['engineTorque'] = engineTorque

    return productsJason


        


def waitRandomSec(maxSec):

    waitSec = randint(1, maxSec)

    print("Wait for ", waitSec, "s...")

    sleep(waitSec)


# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#- END OF FUNCTIONS #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-


# ------------ stage 1 ---------------------

# get request form carsales search page, return serach list result.

# pages = getMultiPageRespondCarsales(URL, 45)  # max page 46, get all the respond, and merge them into a big long string.

# all_jsons = respondProcessCarsales(pages) # process the respond string, into jason  type of dictionary

# print(all_jsons)

# createProductDBwithDict(all_jsons)

# -------------- stage 2 --------------------

# get more detail of each car from dedicate page.

from Sample_pages.Carsales.itemlist import data_list

updatedCarDetail = getCarDetailPageData(data_list)

print(updatedCarDetail)