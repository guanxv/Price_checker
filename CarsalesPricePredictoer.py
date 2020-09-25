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

#print(data[0])

print('ok')

cars = pd.DataFrame(data[0],index = [0])


for item in data:

    temp = pd.DataFrame(item,index = [0])
    cars = pd.concat([cars, temp])


cars = cars.reset_index(drop = True)

cars["is_petrol"] = cars.fuelType.apply(lambda x: 1 if x == "Petrol" else 0)
cars["is_private"] = cars.list_type.apply(lambda x: 1 if x == "private" else 0)
cars["is_auto"] = cars.list_type.apply(lambda x: 1 if 'auto' in cars.name.str.lower() else 0)




print(cars.columns)
print(cars.head(10))

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

x = cars[['year', 'odometer', 'is_private', 'engineSize','numberOfCylinder','is_auto','is_petrol']] #power, drive away price , color

y = cars['price']

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, test_size = 0.2, random_state=100)

lm = LinearRegression()

model = lm.fit(x_train, y_train)

y_predict= lm.predict(x_test)

print("Train score:")
print(lm.score(x_train, y_train))

print("Test score:")
print(lm.score(x_test, y_test))

our_golf = [[2010, 168000, 1, 1.4,4,1,1]]
predict = model.predict(our_golf)
print("Predicted car price: $%.2f" % predict)