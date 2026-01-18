from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def search(request):
    context = {"content": "Search comics"}
    return render(request, "comics/comic.html", context)

def comic_1(request):
    img = "comics/2018-02-16.png"
    title = "First"
    context = { 
        "content": "1",
        "img": img,
        "title": title
        }
    return render(request, "comics/comic.html", context)

def comic_2(request):
    context = {"content": "2"}
    return render(request, "comics/comic.html", context)

def comic_3(request):
    context = {"content": "3"}
    return render(request, "comics/comic.html", context)