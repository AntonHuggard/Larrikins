from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path("search", views.search, name="search"),
    path("<int:pk>/", ComicView.as_view(), name="comics"),
    path("random", RandomView.as_view(), name="random"),
]