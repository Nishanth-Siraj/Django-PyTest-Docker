from django.shortcuts import render
from rest_framework import filters

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from postsapp.models import Post
from postsapp.serializers import CreatePostSerializer, ListPostSerializer,UpdateDeleteSerializer

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

class ListPostApi(generics.ListAPIView):
    serializer_class    = ListPostSerializer
    queryset            = Post.objects.all()

    filter_backends     = [filters.SearchFilter, filters.OrderingFilter]
    search_fields       = [
                                "title",
                                "content",]
    def get(self, request, *args, **kwargs):
        queryset    = self.filter_queryset(self.get_queryset())
        page        = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            paginted_data = self.get_paginated_response(serializer.data).data

            current_page = self.request.query_params.get(
                self.pagination_class.page_query_param,1
                )
            
            return Response({
                "count"     : paginted_data["count"],
                "previous"  : paginted_data["previous"],
                "next"      : paginted_data["next"],
                "data"      : paginted_data["results"]
            },status=status.HTTP_200_OK)
        
        return Response({
            "data": {}
        },status=status.HTTP_204_NO_CONTENT)
    
class LeadUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = UpdateDeleteSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            "provided_by": "Alliance CRM",
            "message": "Lead deleted successfully",
            "status": "200"
        }, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        # tells DRF this is a PATCH
        kwargs['partial'] = True   
        serializer = self.get_serializer(
            self.get_object(), 
            data=request.data, 
            partial=True
        )
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response({
                "provided_by": "Alliance CRM",
                "message": "Lead updated successfully",
                "status": "200",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            "provided_by": "Alliance CRM",
            "message": "Lead not updated",
            "status": "400",
            "data": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
