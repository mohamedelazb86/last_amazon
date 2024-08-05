from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .serializers import PostListSerializers,PostDetailSerializesrs
from .models import Post
from .mypagination import MyPagination
from rest_framework.permissions import IsAuthenticated

class PostListApi(generics.ListAPIView):
    serializer_class=PostListSerializers
    queryset=Post.objects.all()
    pagination_class=MyPagination

    permission_classes = [IsAuthenticated]
    

    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['category',]
    
    search_fields = ['title', 'content']

    
    ordering_fields = ['publish_date',]

   

class PostDetailApi(generics.RetrieveAPIView):
    serializer_class=PostDetailSerializesrs
    queryset= Post.objects.all()