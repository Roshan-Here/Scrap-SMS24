from django.urls import path,include
from . import views


urlpatterns = [
    # path('<slug>/<int:pk>/',), # countrycode/number grab all code from choosen number
    # path('<slug>/',) # to show all country code numbers
    path('all',views.GrabAllNumbers,name="getallnumbers") 
]