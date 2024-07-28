from django.urls import path
from .views import Product_List

urlpatterns = [
    path('',Product_List.as_view()),
]
