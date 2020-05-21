from django.shortcuts import render
from django.utils import timezone

from .models import Post

# Create your views here.


def item_debug(*args):
    for a in args:
        print(type(a))


def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    A = render(request, 'blog/home.html', {'posts': posts})  # post_list.html
    item_debug(request, A, posts)
    return A
