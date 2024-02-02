from django.contrib import admin

from .models import Todo
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ("completed_at",)
    list_filter = ("completed_at", "progress", "status")
    list_display = ("title", "description", "progress", "updated_at", "completed_at")

admin.site.register(Todo, TodoAdmin)