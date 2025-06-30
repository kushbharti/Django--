from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    if request.method =='POST':
        title = request.POST['title']
        desc = request.POST['desc']
        Todo.objects.create(todo_title = title, todo_desc = desc)
 
        return redirect('todo')
    todos = Todo.objects.all()
    
    paginator = Paginator(todos,4)
    page_no = request.GET.get('page')
    page_obj = paginator.get_page(page_no)
    total_page = page_obj.paginator.num_pages
    return render(request,'todo_home.html',{'todos':todos,'page_obj':page_obj,'total_page':[n+1 for n in range(total_page)]})

def update_todo(request,slug):
    todo = Todo.objects.get(slug=slug)
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        
        todo.todo_title = title
        todo.todo_desc = desc
        todo.save()
        return redirect('todo')
    return render(request,'update_todo.html',{'todo':todo})

def delete_todo(request,slug):
    del_todo = Todo.objects.get(slug=slug)
    del_todo.delete()
    return redirect('todo')

