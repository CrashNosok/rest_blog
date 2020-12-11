from rest_framework import serializers
from django.contrib.auth.models import User
from posts.models import Post, Category


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['slug', 'title']
    

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=False, read_only=True)
    category = CategorySerializer(many=False, read_only=False)

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'category', 'author', 'status']
