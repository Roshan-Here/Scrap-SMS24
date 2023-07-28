import requests
from bs4 import BeautifulSoup
# StackOverFlow


# get all data in text format
wow = requests.get("https://djangokatya.com")

# print(wow.text)
# converting into objects
soup = BeautifulSoup(wow.text, 'html.parser')
# print(soup)
black = soup.prettify()

# writing into a txt file error handled (encoding using utf-8) 
# https://stackoverflow.com/questions/51230307/scraping-error-in-python-charmap-codec-cant-encode-character-cant-concat

f = open('beautycheck.txt', 'a',encoding='utf-8')
f.write(black)
f.close()


print(soup.title.string)

print("..........Bieeee........")