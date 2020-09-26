import re
import pandas as pd
from Sample_pages.Carsales.itemlist import data_list

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)

data = data_list.copy()  # make a copy of the dict

for item in data:
    item["price"] = int(item["offers"]["price"])


key_to_del = [
    "@type",
    "url",
    "model",
    "vehicleEngine",
    "image",
    "offers",
    "brand",
    "mileageFromOdometer",
    "bodyType",
]

for item in data:
    for key in key_to_del:
        item.pop(key, None)

# print(data[0])

print("ok")

cars = pd.DataFrame(data[0], index=[0])


for item in data:

    temp = pd.DataFrame(item, index=[0])
    cars = pd.concat([cars, temp])


cars = cars.reset_index(drop=True)
cars = cars.drop([0])


# add engine power and torque

engPowerPattern = re.compile(r"([0-9]{2,3})kW")
cars["power"] = cars.enginePower.apply(
    lambda x: int(engPowerPattern.search(x).group(1))
)

engTorquePattern = re.compile(r"([0-9]{3})Nm")
cars["torque"] = cars.engineTorque.apply(
    lambda x: int(engTorquePattern.search(x).group(1))
)

# add colour
color_list = cars.colour.unique()

for color in color_list:

    cars["is_" + color] = cars.colour.apply(lambda x: 1 if x == color else 0)

#add body style

bodyStyle_list = cars.bodyStyle.unique()

for bodyStyle in bodyStyle_list:

    cars["is_" + bodyStyle] = cars.bodyStyle.apply(lambda x: 1 if x == color else 0)


# add price type ( drive away)

cars["is_driveaway"] = cars.priceType.apply(lambda x: 1 if x == "Drive Away" else 0)

# add rego expire rate
# cars['regoDaysToExp'] = cars['regoDaysToExp'].str.split('\\n')

cars.to_csv("cars.csv")


# do the prediction

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

x = cars[
    [
        "year",
        "odometer",
        "is_private",
        "engineSize",
        "numberOfCylinder",
        "is_auto",
        "is_petrol",
        "power",
        "torque",
        "is_Pure White",
        "is_Indium Grey",
        "is_Deep Black",
        "is_Night Blue",
        "is_Sunset Red",
        "is_driveaway",
    ]
]  # body type, rego expire date.

y = cars["price"]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, train_size=0.8, test_size=0.2, random_state=3
)

lm = LinearRegression()

model = lm.fit(x_train, y_train)

y_predict = lm.predict(x_test)

print("Train score:")
print(lm.score(x_train, y_train))

print("Test score:")
print(lm.score(x_test, y_test))

our_golf = [[2010, 168000, 1, 1.4, 4, 1, 1,90,200,0,0,1,0,0,0]]
predict = model.predict(our_golf)
print("Predicted car price: $%.2f" % predict)
