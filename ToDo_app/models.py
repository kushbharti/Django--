from django.db import models
from datetime import datetime
from autoslug import AutoSlugField


class Todo(models.Model):
    todo_title = models.CharField(max_length=100)
    todo_desc = models.TextField(default='')
    slug = AutoSlugField(populate_from = 'todo_title',unique=True,null=False,blank=True)
    created_date = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return self.todo_title