from django.contrib import admin
from .models import Category, Task


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin): 
    # Display the title, category, due date, and completion status in the admin list view
    list_display = ['title', 'category', 'due_date', 'completed']
    list_filter = ['category', 'completed', 'due_date']
    search_fields = ['title']
