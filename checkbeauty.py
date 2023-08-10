import requests
from bs4 import BeautifulSoup


wow = str(input("enter the number"))

site =  f"https://sms24.me/en/numbers/{wow}"

goto = requests.get(site)

soup = BeautifulSoup(goto.text, 'html.parser')

blank = soup.prettify()

# print(soup.body)
j = soup.body

# y = j.prettify()

# print(y)

f = j.find_all('span',class_="placeholder text-break")


for z in f:
    print(z.split(""))