import requests
from bs4 import BeautifulSoup
import itertools

nice = requests.get("https://sms24.me/en/countries")


ok = BeautifulSoup(nice.text, 'html.parser')

body_content = ok.body.contents

print(body_content[1].prettify())

body_content = body_content[1]

# link=body_content.find_all('div',class_="col-sm-12 col-md-6 col-lg-4")
link=body_content.find_all('a')
# print(link[1])

Ccode = [] #country code array
Cname = [] #country name array

for z in link:
    # print(z.get('href')) #grabbing aall links
    Cname.append(z.text)
    y = z.get('href') #grabbing aall links
    code = y.split("/")
    Ccode.append(code[-1])

# print(Ccode)

# print(Cname)
f = open("beautycheck.txt",'w',encoding='utf-8')

for z,y in zip(Cname,Ccode):
    print(z,y)
    f.write(f"{z,y}\n")