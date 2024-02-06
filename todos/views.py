from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404
from django.template.loader import render_to_string
from datetime import date
from django.views.decorators.http import require_POST

from .models import Todo, Author
from .todo_form import TodoForm

# Create your views here.


def get_todos(request):
    todos = Todo.objects.all().order_by("-completed_at")[:10]
    todo_form = TodoForm()
    return HttpResponse(render(request=request,
                               template_name="todos/todo_list.html",
                               context={"todos_list": todos, 
                                        "selected_nav": 1, 
                                        "name": "Todo App", 
                                        "todo_form": todo_form,
                                        "todo_status": Todo.TASK_STATUSES}))


@require_POST
def add_todos(request):
    todo_form = TodoForm(request.POST)
    author = Author.objects.get(pk=1)
    if todo_form.is_valid():
        print(todo_form.cleaned_data)
        todo = Todo(**todo_form.cleaned_data, author=author)
        todo.save()
    return redirect("todo_list")


def add_numbers(request, a):
    if a > 10:
        return JsonResponse({"result": a})
    else:
        return HttpResponseRedirect("/todos/invalid-request")


def invalid_response(request):
    return JsonResponse({"Result": "Invlid key passed"})


@require_POST
def update_task(request, task_id):
    todo = get_object_or_404(klass=Todo, pk=task_id)
    todo.updated_at = date.today()
    todo_form = TodoForm(request.POST)
    print(todo_form)
    return redirect("todo_list")


def delete_task(request, task_id):
    todo = get_object_or_404(klass=Todo, pk=task_id)
    print(todo.author.get_full_name())
    # todo.delete()
    return redirect("todo_list")


def mark_completed(request, task_id):
    todo = get_object_or_404(klass=Todo, pk=task_id)
    # mark todo completed
    if todo.progress >= 80:
        todo.status = 'C'
    else:
        print("first complete the task progress and update it")

    return redirect("todo_list")
