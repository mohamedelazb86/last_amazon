from django.urls import path
from .views import Product_List,Product_Detail

urlpatterns = [
    path('',Product_List.as_view()),
    path('<slug:slug>',Product_Detail.as_view()),
]
