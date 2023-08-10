import requests
from bs4 import BeautifulSoup
# StackOverFlow


# get all data in text format
wow = requests.get("https://sms24.me/en/numbers")

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

# k = body_content.find_all("div",class_="fw-bold text-primary placeholder")
# print(k[0])

k = body_content.find_all(string=True)
# print(k)

for z in k:
    if z.startswith('+'):
        z = z.split("+")
        print(z[1])



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

