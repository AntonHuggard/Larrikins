from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def search(request):
    context = {"content": "Search comics"}
    return render(request, "comics/comic.html", context)

def comic_1(request):
    context = { 
        "content": "1",
        "img": "comics/2018-02-16.png",
        "title": "First",
        "prev": "comic_1",
        "next": "comic_2"
        }
    return render(request, "comics/comic.html", context)

def comic_2(request):
    context = { 
        "content": "2",
        "img": "comics/2018-03-02.png",
        "title": "Dangerous",
        "prev": "comic_1",
        "next": "comic_3"
        }
    return render(request, "comics/comic.html", context)

def comic_3(request):
    context = { 
        "content": "3",
        "img": "comics/2018-04-02.png",
        "title": "Easter Egg",
        "prev": "comic_2",
        "next": "comic_3"
        }
    return render(request, "comics/comic.html", context)