from django.shortcuts import render
from django.views.generic import ListView

from .models import Product

class Product_List(ListView):
    model=Product
