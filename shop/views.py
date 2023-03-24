from django.shortcuts import render
from django.http import HttpResponse
from .models import products
from math import ceil

# Create your views here.

def index(request):
    Products = products.objects.all()
    # n = len(Products)
    allprods = []
    catsprod = products.objects.values('category','id')
    cats = {item['category'] for item in catsprod}
    for cat in cats:
        prod = products.objects.filter(category=cat)
        n = len(prod)
        allprods.append([prod,range(n)])
    # allprods = [[Products,range(n)],[Products,range(n)]]
    params={"allprods":allprods}
    print(Products)
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')
