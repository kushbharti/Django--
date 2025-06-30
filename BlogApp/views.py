from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'blog_allpost.html')

def user_posts(request):
    return render(request,'blog_user_post.html')