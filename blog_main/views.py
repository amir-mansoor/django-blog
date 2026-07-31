from django.shortcuts import render
from blogs.models import Category,Blog

def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True,status=1).order_by("-created_at")
    list_posts = Blog.objects.filter(is_featured=False,status=1).order_by('-created_at')
    context = {
        'categories': categories,
        'featured_posts': featured_posts,
        'list_posts':list_posts
    }


    return render(request,"index.html",context)