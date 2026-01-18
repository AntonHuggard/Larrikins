from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("comics.urls")),
    path("", include("webpages.urls")),
]