from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_todos, name="todo_list"),
    path("add-numbers/<int:a>", views.add_numbers, name='add-numbers'),
    path("invalid-request", views.invalid_response),
    path("add-todos", views.add_todos, name="add-todos"),
    path("update-task/<int:task_id>", views.update_task, name="update-task"),
    path("delete-task/<int:task_id>", views.delete_task, name="delete-task"),
    path("mark-completed/<int:task_id>", views.mark_completed, name="mark_completed")
]