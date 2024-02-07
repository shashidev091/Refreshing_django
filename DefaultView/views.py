from django.shortcuts import render
from django.views import View
# Create your views here.


class DefaultView(View):
    def get(self, request):
        return render(request, "default_view/index.html")