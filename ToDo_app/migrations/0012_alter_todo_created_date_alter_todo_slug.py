# Generated by Django 5.2.2 on 2025-06-22 19:07

import autoslug.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo_app', '0011_todo_slug_alter_todo_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 6, 23, 0, 37, 57, 373224)),
        ),
        migrations.AlterField(
            model_name='todo',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='todo_title'),
        ),
    ]
