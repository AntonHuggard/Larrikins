from django.urls import path

from . import views

urlpatterns = [
    path("search", views.search, name="search"),
    path("1", views.comic_1, name="comic_1"),
    path("2", views.comic_2, name="comic_2"),
    path("3", views.comic_3, name="comic_3"),
]