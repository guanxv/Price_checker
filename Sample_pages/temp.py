a = {
    "ecommerce": {
        "email": "",
        "click": {
            "actionField": {
                "list": "Search Results"
            },
            "products": [
                {
                    "id": "540635",
                    "name": "Nulon C2 Fuel Conserving Diesel Engine Oil - 0W-30 6 Litre",
                    "variant": "",
                    "category": "SCA01070403",
                    "brand": "Nulon",
                    "price": 50,
                    "quantity": "",
                    "position": 15,
                    "coupon": ""
                }
            ]
        }
    },
    "event": "productClick"
}

print(a["ecommerce"]['click']['products'])