import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://www.bunnings.com.au/our-range/brands/o/ozito-power-x-change'

def create_df(URL, i):

    #Prepare for Dataframe
    df_name = ['fineLine', 'displayName', 'productUrl', 'brandName', 'brandLogo', 'forHire', 'unitOfMeasure', 'price', 'isSpecialOrder', 'availableForOrderOnline', 'availableForPickUp', 'availableForDelivery', 'isTradingRestricted', 'isThirdParty', 'isBundle', 'isCustomMade', 'hasPOADelivery', 'productImage', 'checkStoreForPrice', 'stockStatus', 'isFeatured', 'sellerName', 'isMarketplaceProduct', 'showStockLevel', 'isInStore', 'productRatings', 'totalReviewCount']
    df = pd.DataFrame([],columns = df_name)
    df_row = []

    #generate request
    payload = {'facets':'CategoryIdPath%3D2a021706-07d5-4648-bf26-2ea8fea049df', 'page':i}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
    r = requests.get(URL, headers=headers, params=payload)
    #print(r.text)
    soup = BeautifulSoup(r.content, 'html.parser')

    #process respond html
    scrap_text = soup.find_all('div', attrs = {"class":"js-product-tile-container"})

    #Butcher respond info
    for container in scrap_text:

        a = container.get('data-options').split('[')[1].split(']')[0]
        b = a.split(',{')

        for item in b:
            c = item.lstrip('{').strip('}')
            d = c.split(',')
            d[-1] = d[-1]+"}" # Each Ozito item in list format

            #print(d)
            df_row = []

            for e in d:

                df_row.append(e.split(':')[1].lstrip('\"').strip('\"'))

            df1 = pd.DataFrame([df_row],columns = df_name)
            #print(df1)
            df = df.append(df1, ignore_index=True) #why append not working
            #df = pd.concat([df,df1])


    return(df)



df_name = ['fineLine', 'displayName', 'productUrl', 'brandName', 'brandLogo', 'forHire', 'unitOfMeasure', 'price', 'isSpecialOrder', 'availableForOrderOnline', 'availableForPickUp', 'availableForDelivery', 'isTradingRestricted', 'isThirdParty', 'isBundle', 'isCustomMade', 'hasPOADelivery', 'productImage', 'checkStoreForPrice', 'stockStatus', 'isFeatured', 'sellerName', 'isMarketplaceProduct', 'showStockLevel', 'isInStore', 'productRatings', 'totalReviewCount']
df = pd.DataFrame([],columns = df_name)

for i in range(1,4):
    df = df.append(create_df(URL, i))



df['Price_int'] = df.apply(lambda row: float(row['price']), axis = 1)
df = df.drop(columns = 'price')
df.rename(columns = {'Price_int' : 'price'})


df.to_csv('ozito.csv')

print(df)


