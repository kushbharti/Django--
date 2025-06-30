from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'blog_home'),
    path('user_posts/',views.user_posts, name= 'user_posts'),
]