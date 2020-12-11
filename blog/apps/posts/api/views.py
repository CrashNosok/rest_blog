from rest_framework import generics
from posts.models import Post
from posts.api.serializers import PostSerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoriesPostsView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self, *args, **kwargs):
        # print(self.kwargs)
        return Post.objects.filter(category__id=self.kwargs['pk'])
