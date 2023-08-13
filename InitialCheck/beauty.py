'''
    Grabbing alll latest numbers/country from sms24
'''

import requests
from bs4 import BeautifulSoup
import itertools #https://www.geeksforgeeks.org/python-iterate-multiple-lists-simultaneously/
# StackOverFlow


# get all data in text format
wow = requests.get("https://sms24.me/en/countries")
# wow = requests.get("https://sms24.me/en/countries/in")
# wow = requests.get("https://sms24.me/en/countries/us")
# [india,us,australia,austria,belgium,brazil,bulgaria,canada,chile,china,croatia,]
#[in,us,au,at,be,br,bg,ca,cl,cn,hr,]

# print(wow.text)
# converting into objects
soup = BeautifulSoup(wow.text, 'html.parser')
# print(soup)
black = soup.prettify()

# writing into a txt file error handled (encoding using utf-8) 
# https://stackoverflow.com/questions/51230307/scraping-error-in-python-charmap-codec-cant-encode-character-cant-concat

#f = open('beautycheck.txt', 'w',encoding='utf-8')


# get title (name)
print(soup.title.string)
# get <head></head> content
# print(soup.head)

# get <b></b> tag content
# print(soup.body.b)


# get all tag attributee 
# print(soup.find_all('h5'))

# get all datas inside <body></body>
# print(soup.body)

body_tag = soup.body

# print(body_tag.contents[1])
body_content = body_tag.contents[1]

# print(body_content.prettify()) #checking current data

# k = body_content.find_all("div",class_="fw-bold text-primary placeholder")
num = body_content.find_all("div",class_="fw-bold text-primary placeholder") #grabbing number 
cname = body_content.find_all("h5",class_="text-secondary placeholder") #grabbing country name

numarray = []
cnamearray =[]

for x in num:
    # print(x.string)
    numarray.append(x.string)

for y in cname:
    # print() 
    cnamearray.append(y.string)

for (x,y) in zip(cnamearray,numarray):
    print(x,y)


# k = body_content.find_all(string=True)
# print(k)

# for z in k:
#     if z.startswith('+'):
#         z = z.split("+")
#         print(z[1])



# print(body_content)
# for child in body_content:
#     # print(child.contents[1])
#     # j = str(child.contents[1])
#     j = child.contents[1]
#     j = j.find_all("div","fw-bold text-primary placeholder")
#     f.write(f"{j}\n")
#     print(j[1])    
#     # f.write("\n")
# print("..........Bieeee........")

