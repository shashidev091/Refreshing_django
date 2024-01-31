from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404
from django.template.loader import render_to_string

from .models import Todo

# Create your views here.
demo_data = [
    {
        "title": "Spend 10 min on yourself",
        "progress": "10%",
        "status": False,
        "desc": "It is required to sit silently and plan or think about the task and what you want to achive in future."
    },
    {
        "title": "Spend 3 hour on learning something",
        "progress": "10%",
        "status": False,
        "desc": "It is required to learn new technology and polish something to be in the industry."
    }, {
        "title": "Learn mathamatics",
        "progress": "1%",
        "status": False,
        "desc": "It is required to solve few mathamatics problems to keep you mind fresh"
    }, {
        "title": "Add a new hobbie",
        "progress": "10%",
        "status": True,
        "desc": "It is required to have a healthy hobbie."
    },
]

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


def index(request):
    return HttpResponse(render(request=request,
                               template_name="todos/index.html",
                               context={
                                   "name": "shashi bhagat",
                                   "active_page": 1,
                                   "selected_nav": 3
                               }))


def add_numbers(request, a):
    if a > 10:
        return JsonResponse({"result": a})
    else:
        return HttpResponseRedirect("/todos/invalid-request")


def invalid_response(request):
    return JsonResponse({"Result": "Invlid key passed"})


def another_page(request):
    return HttpResponse(render(request=request,
                               template_name="todos/index.html",
                               context={
                                   "selected_nav": 4
                               }))


def update_task(request, task_id):
    todo = get_object_or_404(klass=Todo, pk=task_id)
    return HttpResponse(render(request=request,
                               template_name="todos/create_todos.html",
                               context={
                                   "task_detail": todo,
                                   "selected_nav": 2
                               }))