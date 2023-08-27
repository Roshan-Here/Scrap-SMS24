import requests
from bs4 import BeautifulSoup
from time import sleep
import itertools

def GetNumberData():
    wow = str(input("enter the number"))

    if wow.startswith("+"):
        wow = wow.split("+")
        wow = wow[1]
        print(wow)

    site =  f"https://sms24.me/en/numbers/{wow}"

    try:
        goto = requests.get(site)
    except SystemError as e: # need to add new exeception
        print(e)
    # else:
    #     print("Noot valid number")


    soup = BeautifulSoup(goto.text, 'html.parser')

    blank = soup.prettify()

    # print(soup.body)
    j = soup.body

    y = j.prettify()

    print(y)

    f = j.find_all('span',class_="placeholder text-break") # return complete data as string
    # placeholder ms-1
    k = j.find_all('a',class_='placeholder ms-1')
    i = j.find('h2',class_='text-secondary d-block placeholder')



    global dataarray,titlearray
    dataarray = []
    titlearray = []

    # print(f[0])

    # span_tag = soup.span.extract()
    # span_string = span_tag.string.extract()

    # print(span_string)


    for z,y in zip(f,k):
        if z is not None:
            dataarray.append(z.string)
            titlearray.append(y.string)
        else:
            print('#None')

    print(dataarray)
    print(titlearray)
    print(i.string)
    print("Options:Whatsapp | Telegram | Apple | Google")
    choose = str(input("Choose options..."))

    for x in dataarray:
        if choose in x:
            print(x)
    else:
        print("Not yet ! wait")
        Recheck(dataarray)



def Recheck(incomming):
    while dataarray != incomming:
        GetNumberData()
    else:
        TSec = str(input("No new datas, wanna wait for 30sec to grab new datas (Y/S)?"))
        if TSec.upper() == "Y":
            print("Sleeping for 30 ssecc...")
            sleep(10)
            GetNumberData()

GetNumberData()