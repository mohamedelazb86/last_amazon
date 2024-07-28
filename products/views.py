from django.shortcuts import render
from django.views.generic import ListView,DetailView

from .models import Product

class Product_List(ListView):
    model=Product
    paginate_by=28

class Product_Detail(DetailView):
    model=Product
