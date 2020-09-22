import requests
from random import randint
from time import sleep
from bs4 import BeautifulSoup
import json

from productDataBase import createProductDBwithDict


URL = "https://www.carsales.com.au/cars/used/volkswagen/golf/victoria-state/"


def getMultiPageRespondCarsales(theURL, totalPages):

    print('Start Sending Requests...')

    allPages = []

    for pageNum in range(1, totalPages + 1):

        waitSec = randint(5, 40)

        print("Wait for ", waitSec, "s...")

        sleep(waitSec)

        # generate request
        payload = {"offset": (pageNum - 1) * 12}
        #payload = {"offset": 548}
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
        }

        r = requests.get(theURL, headers=headers, params=payload)

        the_page = r.content

        allPages.append(the_page)

        print("page", pageNum, "respond received. Total Page Number ", totalPages )

    return allPages


def respondProcessCarsales(the_pages):

    all_json = []

    for page in the_pages:

        soup = BeautifulSoup(page, "html.parser")

        list_car_script = soup.find("script", attrs={"type": "application/ld+json"})

        data_cars_json = json.loads(list_car_script.string)  # load into json format

        for car_list in data_cars_json["mainEntity"]["itemListElement"]:

            car_list = car_list["item"] #remove not wanted keys

            car_list["year"] = int(car_list["name"].split(" ")[0]) # add year in int type

            car_list['engineSize'] = float(car_list['vehicleEngine']['engineDisplacement']['value'].split(" ")[1].strip("L")) # add engine size in liter in int 

            car_list['numberOfCylinder'] = int(car_list['vehicleEngine']['engineDisplacement']['value'].split(" ")[0].strip("cyl")) # add number of cylinder in num

            if "Petrol".lower() in car_list['vehicleEngine']['engineDisplacement']['value']:  # add fuel type
                
                car_list['fuelType'] = "Petrol"

            else:

                car_list['fuelType'] = "Diesel"

            
            car_list['odometer'] = int(car_list['mileageFromOdometer']['value']) # move odometer key in top level for easier access, change to int type

            if "private" in car_list['image'][0]['url']:   # is it private or dealer car , add list type in 'string'

                car_list['list_type'] = "private"

            else:

                car_list['list_type'] = "dealer"


            all_json.append(car_list)  # append to json,

    return all_json


pages = getMultiPageRespondCarsales(URL, 1)  # max page 46


all_jsons = respondProcessCarsales(pages)

# createProductDBwithDict(all_jsons)

print(all_jsons)