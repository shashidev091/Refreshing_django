from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.MarketPlaceView.as_view(), name="market-index")
]