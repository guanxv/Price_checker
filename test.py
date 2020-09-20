import requests
import json

a = "%7B%22ecommerce%22%3A%7B%22email%22%3A%22%22%2C%22promoClick%22%3A%7B%22promotions%22%3A%5B%7B%22id%22%3A%22sitewide-header-victoria-covid%22%2C%22name%22%3A%22Sitewide%20Header%20-%20Victoria%20Covid%20Messaging%22%2C%22creative%22%3A%22%22%2C%22position%22%3A%22header-banner%22%7D%5D%7D%7D%2C%22event%22%3A%22promotionClick%22%7D"

unquoted = requests.utils.unquote(a)
data = json.loads(unquoted)

print(unquoted)
print(data)
