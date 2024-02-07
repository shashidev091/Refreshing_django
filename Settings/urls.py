from django.urls import path
from . import views

urlpatterns = [
    path(route="", view=views.SettingsView.as_view(), name='setting-page')
]