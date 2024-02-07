from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.DefaultView.as_view(), name="default-view")
]