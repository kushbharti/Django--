from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='todo'),
    path('update_todo/<slug:slug>',views.update_todo, name = 'update_todo'),
    path('delete_todo/<slug:slug>', views.delete_todo,name ='delete_todo'),
]