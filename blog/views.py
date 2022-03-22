# from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# ListView를 상속받아 만든 PostList 클래스


class PostList(ListView):
    model = Post
    # 우선순위
    ordering = '-pk'
    # template_name = 'blog/index.html'


# def index(request):
#     posts = Post.objects.all().order_by('-pk')  # order_by('-pk') => 최신순 정렬

#     return render(
#         request,
#         'blog/index.html',
#         {'posts': posts, }
#     )


# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)

#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'post': post,
#         }
#     )
