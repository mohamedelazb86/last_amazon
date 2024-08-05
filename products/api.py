from rest_framework import generics
from .models import Product
from .serializers import productListSerializers,ProductDetailSerailizers
from posts.mypagination import MyPagination


class ProductListApi(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=productListSerializers
    pagination_class=MyPagination
  

class ProductDetailApi(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductDetailSerailizers