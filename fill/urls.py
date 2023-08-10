from django.urls import path
from . import views

app_name = "fill"

urlpatterns = [
    path("", views.home, name="home"),
]
