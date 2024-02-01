from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404
from django.template.loader import render_to_string

from .models import Todo

# Create your views here.


def get_todos(request):
    todos = Todo.objects.all()
    return HttpResponse(render(request=request,
                               template_name="todos/todo_list.html",
                               context={"todos_list": todos, "selected_nav": 1}))


def add_todos(request):
    todos = Todo.objects.all()
    return HttpResponse(render(request=request,
                               template_name="todos/create_todos.html",
                               context={"todos_list": todos, "selected_nav": 2}))


def add_numbers(request, a):
    if a > 10:
        return JsonResponse({"result": a})
    else:
        return HttpResponseRedirect("/todos/invalid-request")


def invalid_response(request):
    return JsonResponse({"Result": "Invlid key passed"})


def update_task(request, task_id):
    todo = get_object_or_404(klass=Todo, pk=task_id)
    return HttpResponse(render(request=request,
                               template_name="todos/create_todos.html",
                               context={
                                   "task_detail": todo,
                                   "selected_nav": 2
                               }))


def delete_task(request, task_id):
    todo = get_object_or_404(klass=Todo, pk=task_id)
    return redirect("todo_list")
