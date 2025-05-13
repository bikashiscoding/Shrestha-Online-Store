from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

print('Welcome to my first web page Products')

#/products -> index
#URL -> address

def index(request):
    products = Product.objects.all()
    return render(request,'index.html',
                  {'products': products})


def new(request):
    return HttpResponse('New Products')

def old(request):
    return HttpResponse('Hello mate welcome to old page')