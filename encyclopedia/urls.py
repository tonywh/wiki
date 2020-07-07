from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("random", views.random, name="random"),
    path("wiki/<title>", views.wiki, name="wiki"),
    path("edit/<title>", views.edit, name="edit"),
]
