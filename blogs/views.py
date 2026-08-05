from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog,Category

# Create your views here.
def posts_by_category(request,category_id):
    posts = Blog.objects.filter(status=1,category=category_id)
    try:
        category = get_object_or_404(Category,pk=category_id)
        
    except:
        return redirect("home")

    context = {
        'posts':posts,
        'category':category
    }

    
    return render(request,'posts_by_category.html',context)