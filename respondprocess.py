import json
from bs4 import BeautifulSoup


def webRespondProcess(webRespondByte):

    # webRespondStr is respond = urllib.request.urlopen(req).read()

    # replace error and illigal charactor in the string
    a = webRespondByte.decode(
        "utf8", errors="replace"
    )  # .replace("\\\\u003e", ">" ).replace("\\\\u0026", "&").encode("utf8", errors="replace")
    b = a.replace("\\\\u003e", ">")
    c = b.replace("\\\\u0026", "&")
    d = c.encode("utf8", errors="replace")

    # the \\u003e and u0026 can not be replace by the str.replace() method, so i have to convert it to byte and replace in byte.
    e = (
        d.replace(b"u0026", b"&")
        .replace(b"u003e", b">")
        .replace(b"\\", b"")
        .replace(b"\u203a", b"")
    )

    # take the converted html byte respon into soup
    soup = BeautifulSoup(e, "html.parser")

    # print(soup.prettify().encode("utf8"))

    # find the div with json container.
    div_json = soup.find_all("div", attrs={"class": "js-product-tile-container"})

    all_data = []

    for container in div_json:
        # print(container)
        data = json.loads(container.get("data-options"))  # use get() to get the text
        data = data["data"]
        for dictionary in data:
            all_data.append(dictionary)

    return all_data
