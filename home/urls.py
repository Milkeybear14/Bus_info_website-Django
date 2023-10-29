from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="views"),
    path('searchBusCatagory', views.searchBusCatagory, name = "catagory"),
    path('busses/<int:id>', views.busses, name="bus"),
]
