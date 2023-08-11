import requests
from bs4 import BeautifulSoup


wow = str(input("enter the number"))

site =  f"https://sms24.me/en/numbers/{wow}"

try:
    goto = requests.get(site)
except SystemError as e:
    print(e)
else:
    print("Noot valid number")


soup = BeautifulSoup(goto.text, 'html.parser')

blank = soup.prettify()

# print(soup.body)
j = soup.body

# y = j.prettify()

# print(y)

f = j.find_all('span',class_="placeholder text-break") # return complete data as string


# print(f[0])

# span_tag = soup.span.extract()
# span_string = span_tag.string.extract()

# print(span_string)


for z in f:
    if z is not None:
        print(z.string)
    else:
        print('#None')