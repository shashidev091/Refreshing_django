from django.shortcuts import render
from django.views import View
# Create your views here.


class MarketPlaceView(View):
    def get(self, request):
        print("Hello World")
        return render(request=request, template_name="marketPlace/index.html", context={
            "name": "Gangaes Hat"
        })