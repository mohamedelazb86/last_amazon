from django.urls import path
from .views import order_list,checkout,add_cart

urlpatterns = [
    path('',order_list),
    path('checkout',checkout),
    path('add_to_cart',add_cart),
]
