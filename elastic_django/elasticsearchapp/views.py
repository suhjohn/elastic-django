from django.shortcuts import render

# Create your views here.
from elasticsearchapp import search
from elasticsearchapp.models import BlogPost


def post_list(request):
    posts = BlogPost.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'elasticsearchapp/post_list.html', context)

def search_post(request):
    query = request.GET.get('search_box')
    result = search.search(query)
    context = {
        'posts':result
    }
    return render(request, 'elasticsearchapp/post_list.html', context)