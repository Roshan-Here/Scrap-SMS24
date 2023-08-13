import requests
from bs4 import BeautifulSoup
from time import sleep


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

    # y = j.prettify()

    # print(y)

    f = j.find_all('span',class_="placeholder text-break") # return complete data as string
    global array
    array = []

    # print(f[0])

    # span_tag = soup.span.extract()
    # span_string = span_tag.string.extract()

    # print(span_string)


    for z in f:
        if z is not None:
            array.append(z.string)
        else:
            print('#None')

    print(array)
    print("Options:Whatsapp | Telegram | Apple | Google")
    choose = str(input("Choose options..."))

    for x in array:
        if choose in x:
            print(x)
    else:
        print("Not yet ! wait")
        Recheck(array)



def Recheck(incomming):
    while array != incomming:
        GetNumberData()
    else:
        TSec = str(input("No new datas, wanna wait for 30sec to grab new datas (Y/S)?"))
        if TSec.upper() == "Y":
            print("Sleeping for 30 ssecc...")
            sleep(10)
            GetNumberData()

GetNumberData()