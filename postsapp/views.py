from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from postsapp.models import Post
from postsapp.serializers import CreatePostSerializer

class CreatePostApi(generics.CreateAPIView):
    serializer_class    = CreatePostSerializer
    queryset            = Post.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                response = serializer.save()

                return Response({
                    "data": serializer.data
                },status=status.HTTP_201_CREATED)
            
            return Response({
                "error": serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                "error": str(e)
            },status=status.HTTP_400_BAD_REQUEST)
