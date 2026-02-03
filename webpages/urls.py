from django.urls import path

from . import views

urlpatterns = [
    path("sketchbook", views.sketchbook, name="sketchbook"),
    path("sketchbook/2017", views.sketchbook_2017, name="sketchbook_2017"),
    path("sketchbook/2018", views.sketchbook_2018, name="sketchbook_2018"),
    path("sketchbook/2019", views.sketchbook_2019, name="sketchbook_2019"),
    path("art", views.art, name="art"),
    path("about", views.about, name="about"),
]