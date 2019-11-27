import requests
from bs4 import BeautifulSoup
import smtplib
import csv

URL_list = ['https://www.bunnings.com.au/ozito-power-x-change-18v-brushless-impact-wrench-skin-only_p6290566',
            'https://www.bunnings.com.au/ozito-power-x-change-18v-impact-driver-skin-only_p6290472'



            ]

def check_price(URL):

    product_info_dict = {}

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    scrap_text = soup.find('main').find('script')

    product_info_dict = process_respond(scrap_text)

    product_name = product_info_dict['displayName']
    product_price = float(product_info_dict['price'])

    return product_name, product_price

#scraped data process (Bunnings)
def process_respond(text):
    product_info = {}
    new_text = text.get_text()
    product_info_list = new_text.split('{')[1].split('}')[0].split('<')[0].split(',')
    #print(product_info_list)
    for item in product_info_list:
        key = item.split(":")[0].strip('\"')
        value = item.split(":")[1].strip('\"')
        product_info[key] = value
    return product_info

def check_history_price():

    price_history = []

    with open('price_history.csv') as price_csv:
        price_history_reader = csv.DictReader(price_csv, delimiter=',')
        for row in price_history_reader:
            item_price_history = []
            item_price_history.append(row['product_name'])
            item_price_history.append(float(row['product_price']))
            item_price_history.append(row['url'])
            price_history.append(item_price_history)

    return price_history

def price_current(URL_list):

    price_current = []
    product_name = ""
    product_price = 0

    for url in URL_list:
        product_name, product_price = check_price(url)
        item_price_current = []
        item_price_current.append(product_name)
        item_price_current.append(product_price)
        item_price_current.append(url)
        price_current.append(item_price_current)

    return price_current

def write_header(list_to_update):

#    big_list = [{'product_name' : 'a', 'product_price' : 100, 'url' : 'www.abc.com'},
#                {'product_name' : 'b', 'product_price' : 200, 'url' : 'www.bcd.com'},
#               {'product_name' : 'c', 'product_price' : 300, 'url' : 'www.efg.com'}]


    with open('price_history.csv', 'w') as output_csv:
        fields = ['product_name', 'product_price', 'url']
        output_writer = csv.DictWriter(output_csv, fieldnames = fields)


        output_writer.writeheader()
#        for item in big_list:
#            output_writer.writerow(item)

        for item1 in list_to_update:
            dict = {key : value for key, value in zip(fields, item1)}
            output_writer.writerow(dict)


def send_mail():

    p_name, p_price = check_price()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('guanxv@gmail.com', '')

    subject = p_name + "Price Drop to $" + str(p_price)
    body = 'https://www.bunnings.com.au/ozito-power-x-change-18v-brushless-impact-wrench-skin-only_p6290566'

    msg = "Subject: {subject}\n\n{body}".format(subject = subject, body = body)

    server.sendmail('guanxv@gmail.com', 'guanxv@gmail.com', msg)

    server.quit()

def compare_price(URL_list):
    price_current_list = price_current(URL_list)
    price_history_list = check_history_price()


    send_email_list = []

    #check price against history, if current price drops, send email
    for item_cur in price_current_list:

        for item_his in price_history_list:

            if item_cur[0] == item_his[0]:

                if item_cur[1] < item_his[1]:

                    send_email_list.append(item_cur)

    cur_item_name = [x[0] for x in price_current_list]
    history_only_list = [x for x in price_history_list if x[0] not in cur_item_name]

    write_header(price_current_list + history_only_list)

compare_price(URL_list)



























def send_mail():

    p_name, p_price = check_price()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('guanxv@gmail.com', '')

    subject = p_name + "Price Drop to $" + str(p_price)
    body = 'https://www.bunnings.com.au/ozito-power-x-change-18v-brushless-impact-wrench-skin-only_p6290566'

    msg = "Subject: {subject}\n\n{body}".format(subject = subject, body = body)

    server.sendmail('guanxv@gmail.com', 'guanxv@gmail.com', msg)

    server.quit()


