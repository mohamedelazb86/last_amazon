from django.shortcuts import render
from products.models import Product,Brand,Review

def home(request):
    new_product=Product.objects.filter(flag='New')[:10]
    sale_product=Product.objects.filter(flag='Sale')[:10]
    feature_product=Product.objects.filter(flag='Feature')[:6]

    brands=Brand.objects.all()

    context={
        'new_product':new_product,
        'sale_product':sale_product,
        'feature_product':feature_product,
        'brands':brands,
    }
    return render(request,'settings/index.html',context)