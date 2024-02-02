from django.contrib import admin

from .models import Todo, Author, Address
# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ("completed_at",)
    list_filter = ("completed_at", "progress", "status")
    list_display = ("title", "description", "progress",
                    "updated_at", "completed_at", 'author')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'address')


class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'city', 'postal_code', 'country')


admin.site.register(Todo, TodoAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address, AddressAdmin)
