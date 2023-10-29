from django.shortcuts import render
from .models import Bus, busCatagory
from django.core.paginator import Paginator, Page

# Create your views here.
def home(request):

    
    catagory = busCatagory.objects.all()
    paginator = Paginator(catagory, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj':page_obj
    }
    return render(request, 'home.html', context)

def searchBusCatagory(request):

    searched = request.GET['searched']
    catagory = busCatagory.objects.filter(Name__contains = searched)
    paginator = Paginator(catagory, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'catagory':catagory,
        'page_obj':page_obj 
    }
    return render(request, 'home.html', context)

def busses(request, slug):
    bus = Bus.objects.filter(Mame__exact = slug)
    context = {
        'busses':bus
    }