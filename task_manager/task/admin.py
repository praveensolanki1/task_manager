from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'due_date', 'completed')  # Columns to display
    list_filter = ('completed', 'due_date')  # Filters on the sidebar
    search_fields = ('title', 'description')  # Searchable fields
