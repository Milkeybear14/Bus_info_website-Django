from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="views"),
    path('searchBusCatagory', views.searchBusCatagory, name = "catagory"),
    path('busses<slug:slug>', views.busses, name="bus"),
]
