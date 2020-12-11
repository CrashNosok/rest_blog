from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from django.urls import reverse

from django.http import JsonResponse

from posts.models import Post


# @login_required
def index(request):
    return HttpResponse('hello')


class PostsListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/posts.html'


def json_list_published_posts(request):
    posts = Post.objects.filter(status='published')

    # json_dumps_params - кодировка
    return JsonResponse(
        {
        'posts': [
            {
                'title': p.title,
                'slug': p.slug,
                'id': p.id,
                'published': p.when_published,
            }
            for p in posts
        ],
    }, 
    json_dumps_params={'ensure_ascii': False})

