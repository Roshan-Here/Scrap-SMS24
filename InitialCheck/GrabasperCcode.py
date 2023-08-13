'''
    fuction which grabs all numbers using Ccode
'''

import requests
from bs4 import BeautifulSoup

global GrbNumbers

def GrabAllNo(Ccode="in"): #initally india
    sitelink = f"https://sms24.me/en/countries/{Ccode}"
    
    owk = requests.get(sitelink)

    nice = BeautifulSoup(owk.text,'html.parser')

    body_content = nice.body.contents[1]

    # print(body_content.prettify())

    Cnumbers = body_content.find_all("div",class_="fw-bold text-primary placeholder")

    GrbNumbers = []

    for x in Cnumbers:
        # print(x.string)
        GrbNumbers.append(x.string)
    # print(Cnumbers.string)

    return GrbNumbers

print("['au', 'at', 'be', 'br', 'bg', 'ca', 'cl', 'cn', 'hr', 'cz', 'dk', 'ee', 'fi', 'fr', 'ge', 'de', 'hk', 'in', 'id', 'il', 'it', 'jp', 'kz', 'lv', 'lt', 'mo', 'my', 'mx', 'nl', 'ng', 'ph', 'pl', 'pt', 'pr', 'ro', 'ru', 'es', 'se', 'th', 'ua', 'gb', 'us', 'vn']\n")

Ask = (str(input("give country code from above list: "))).lower()


numz = GrabAllNo(Ask)


print(numz)

# need to move on to Django-SmS24