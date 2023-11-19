from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("components/", views.components, name="components"),
    path("contents/", views.contents, name="contents"),
    path("reactive/", views.reactive, name="reactive"),
]
