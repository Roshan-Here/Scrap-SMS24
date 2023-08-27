from django.urls import path,include
from . import views


urlpatterns = [
    # path('<slug>/<int:pk>/',), # countrycode/number grab all code from choosen number
    # path('<slug>/',) # to show all country code numbers
    path('',views.GrabAllNumbers,name="getallnumbers"), 
    path('numbers/<int:num>',views.GetNumberData,name="grabnumbdetails"),
    path('countries',views.GrabCountryNames,name='grabcountries')
]