from django.contrib import admin
from .models import Todo

# Register your models here.

@admin.register(Todo)
class AdminTodo(admin.ModelAdmin):
    list_display = ('id','todo_title','todo_desc','created_date')
    search_fields = ('todo_title',)