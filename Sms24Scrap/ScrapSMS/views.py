from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.views.generic.base import TemplateView
import itertools
# Create your views here. not using any models only views (simple proj)

''''
================
CBV
================
'''

class Main(TemplateView):
    template_name = 'ScrapSMS/home.html'



''' 
=======================
Function based views
=======================
'''

# 1. grab all no: | then grab country name/ no and return cc:no
# 2. need to get country no: check country | then grab all datas for that no
# 2. need to check country code: then grab all no for that country


def GrabAllNumbers(request):
    site = "https://sms24.me/en/numbers"
    grab = requests.get(site)

    soup = BeautifulSoup(grab.text,'html.parser')

    body_content = soup.body.contents[1]
    # print(body_content.prettify())

    grbnum = body_content.find_all('div',class_='fw-bold text-primary placeholder') 
    grabcontry = body_content.find_all('h5',class_='text-secondary placeholder')

    numarry = [(str((x.string).split("+")[1])) for x in grbnum] # figured within one line 
    '''
    for x in grbnum:
        x =(x.string).split("+")
        print(x)
    '''
    cnamearray = [y.string for y in grabcontry]

    print(numarry)

    print(cnamearray)

    # ziping both array into one for grabing simply
    values = zip(numarry,cnamearray)

    # https://django.cowhite.com/blog/numeric-for-loop-in-django-templates/
    return render(request,'ScrapSMs/home.html',{"vals":values})

# need to setup template

# GrabAllNumbers()


