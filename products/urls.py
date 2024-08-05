from django.urls import path
from .views import Product_List,Product_Detail,add_review,Brand_Detail,Brand_List
from .api import ProductDetailApi,ProductListApi

urlpatterns = [
    path('brands',Brand_List.as_view()),
    path('brands/<slug:slug>',Brand_Detail.as_view()),


    path('',Product_List.as_view()),
    path('<slug:slug>',Product_Detail.as_view()),
    path('add_review/<slug:slug>',add_review),

    # api 
    path('api/productlist',ProductListApi.as_view()),
    path('api/productdetail/detail/<int:pk>',ProductDetailApi.as_view()),
]
