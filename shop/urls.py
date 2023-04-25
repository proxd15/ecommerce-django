from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path("",views.index,name="shopindex"),
   path("about",views.about,name="about"),
   path("contact",views.contact,name="contact"),
   path("product/<int:myid>",views.productview,name="productview"),
   path("tracker",views.tracker,name="tracker"),
]