from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Category, Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    categories = Category.objects.all()
    posts = Post.objects.all()

    context = {
        'categories': categories,
        'posts': posts,
    }

    return render(
        request,
        'index.html',
        context,
    )


def post(request, slug):
    p = Post.objects.filter(
        slug=slug,
    ).first()
    context = {
        'post': p,
    }
    return render(
        request,
        'post.html',
        context,
    )


# TODO: Доделать функцию вывода
def get_category(request, slug):
      category = get_object_or_404(Category, slug=slug)  
    posts = Post.objects.filter(category=category, status='published') #
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')  

    try:
        posts_page = paginator.get_page(page_number) 
    except PageNotAnInteger:
        posts_page = paginator.page(1) 
    except EmptyPage:
        posts_page = paginator.page(paginator.num_pages) 
    context = {
        'category': category,
        'posts': posts_page,
    }

    return render(request, 'blog/category_posts.html', context)

