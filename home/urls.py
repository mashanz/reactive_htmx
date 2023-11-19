from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("components/", views.components, name="components"),
    path("contents/", views.contents, name="contents"),
    path("reactive/", views.reactive_get, name="reactive_get"),
    path("reactive/add/", views.reactive_add, name="reactive_add"),
    path("reactive/delete/", views.reactive_delete, name="reactive_delete"),
]
