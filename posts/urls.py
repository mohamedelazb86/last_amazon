from django.urls import path
from .views import post_list,post_detail,create_post,update_post,delete_post
from .api import PostListApi,PostDetailApi

urlpatterns = [
    path('',post_list),
    path('create_post',create_post),
    path('<slug:slug>',post_detail),
    path('<slug:slug>/update',update_post),
    path('<slug:slug>/delete',delete_post),

    # api

    path('api/postlist',PostListApi.as_view()),
    path('api/postdetail/<int:pk>',PostDetailApi.as_view()),

    
]
