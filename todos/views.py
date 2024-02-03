from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404
from django.template.loader import render_to_string
from datetime import date
from django.views.decorators.http import require_POST

from .models import Todo, Author

# Create your views here.


def get_todos(request):
    todos = Todo.objects.all().order_by("-completed_at")[:10]
    return HttpResponse(render(request=request,
                               template_name="todos/todo_list.html",
                               context={"todos_list": todos, "selected_nav": 1, "name": "Todo App"}))


@require_POST
def add_todos(request):
    title = request.POST.get("title")
    desc = request.POST.get("desc")
    progress = request.POST.get("progress")
    status = request.POST.get("status")

    todos = Todo.objects.all()
    author = Author.objects.get(pk=1)
    todo = Todo(title=title, description=desc, progress=progress, status="P", author=author)
    todo.save()
    todos = Todo.objects.all().order_by("-created_at")[:10]
    return HttpResponse(render(request=request,
                               template_name="todos/todo_list.html",
                               context={"todos_list": todos, "selected_nav": 1, "name": "Todo App"}))


def add_numbers(request, a):
    if a > 10:
        return JsonResponse({"result": a})
    else:
        return HttpResponseRedirect("/todos/invalid-request")


def invalid_response(request):
    return JsonResponse({"Result": "Invlid key passed"})


def update_task(request, task_id):
    todo = get_object_or_404(klass=Todo, pk=task_id)
    todo.updated_at = date.today()
    return HttpResponse(render(request=request,
                               template_name="todos/create_todos.html",
                               context={
                                   "task_detail": todo,
                                   "selected_nav": 2
                               }))


def delete_task(request, task_id):
    todo = get_object_or_404(klass=Todo, pk=task_id)
    print(todo.author.get_full_name())
    # todo.delete()
    return redirect("todo_list")
