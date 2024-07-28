from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView

from .models import Product,Review,ProductImage

class Product_List(ListView):
    model=Product
    paginate_by=28

class Product_Detail(DetailView):
    model=Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object()).order_by('-id')[:3]
        context["related"] = Product.objects.filter(brand=self.get_object().brand)
        context["images"] = ProductImage.objects.filter(product=self.get_object())
        return context


def add_review(request,slug):
    user=request.user
    product=Product.objects.get(slug=slug)
    rate=int(request.POST['rating'])
    review=request.POST['myreview']
    Review.objects.create(
        user=user,
        product=product,
        rate=rate,
        review=review
    )
    return redirect(f'/products/{slug}')


    
