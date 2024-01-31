from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("add-numbers/<int:a>", views.add_numbers, name='add-numbers'),
    path("invalid-request", views.invalid_response),
    path("another-link", views.another_page, name="another-link"),
    path("todo-list", views.get_todos, name="todo-list"),
    path("add-todos", views.add_todos, name="add-todos")
]