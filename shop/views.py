from django.shortcuts import render
from django.http import HttpResponse
from .models import products , Contacts
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

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        desc = request.POST.get('desc','')
        number = request.POST.get('number','')

        Contact = Contacts(name = name , email = email , desc = desc , number = number)
        Contact.save()
    return render(request,'shop/contact.html')

def tracker(request):
    return render(request,'shop/tracker.html')

def productview(request,myid):
    # Fetch the product from the database
    product = products.objects.filter(id=myid)

    return render(request,'shop/prodview.html',{'product':product[0]})

def checkout(request):
    return render(request,'shop/checkout.html')
