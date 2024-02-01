from django.shortcuts import render

# Create your views here.

def setting_page(request):
    return render(request=request,
                  template_name="settings.html",
                  context={
                      
                  })