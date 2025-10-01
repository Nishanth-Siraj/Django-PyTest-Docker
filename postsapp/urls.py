from django.urls import path
from postsapp.views import *

urlpatterns = [
    path('create-posts/',
         CreatePostApi.as_view(),
         name="create-posts")
]