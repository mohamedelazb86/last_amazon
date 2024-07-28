from django.urls import path
from .views import Product_List,Product_Detail,add_review

urlpatterns = [
    path('',Product_List.as_view()),
    path('<slug:slug>',Product_Detail.as_view()),
    path('add_review/<slug:slug>',add_review),
]
