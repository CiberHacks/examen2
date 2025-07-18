from django.contrib import admin
from .models import ToDo

@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'is_completed', 'created_at')
    list_filter = ('is_completed', 'created_at')
    search_fields = ('title', 'user__username')
    ordering = ('-created_at',)
