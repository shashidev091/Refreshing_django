from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template.loader import render_to_string

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
    return HttpResponse(render(request=request,
                               template_name="todos/todo-list.html",
                               context={"todos_list": demo_data, "selected_nav": 1}))


def add_todos(request):
    return HttpResponse(render(request=request,
                               template_name="todos/create_todos.html",
                               context={"todos_list": demo_data, "selected_nav": 2}))


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

