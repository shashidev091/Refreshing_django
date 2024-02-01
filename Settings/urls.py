from django.urls import path
from . import views

urlpatterns = [
    path(route="", view=views.setting_page, name='setting-page')
]