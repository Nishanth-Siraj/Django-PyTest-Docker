from django.contrib import admin
from postsapp.models import Post


class PostsAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published', 'created_at', 'updated_at']
admin.site.register(Post, PostsAdmin)