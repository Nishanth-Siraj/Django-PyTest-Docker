from rest_framework import serializers
from postsapp.models import Post

class CreatePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

class ListPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class UpdateDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'