from rest_framework import serializers
from postsapp.models import Post

class CreatePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'