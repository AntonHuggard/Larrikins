from django.shortcuts import render, get_object_or_404, redirect 
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from .models import Comic
import random


def search(request):
    context = {"content": "Search comics"}
    return render(request, "comics/comic.html", context)


def get_highest_index():
    comic_count = Comic.objects.all().count()
    return comic_count

def get_prev(i):
    if i == 1:
        return "/1"
    return "/" + str(i - 1)

def get_next(i, last):
    return "/" + str(min(i + 1, last))

def get_context(obj):
    last = get_highest_index()
    return { 
        "img": "comics/"+obj.img_src,
        "alt_text": obj.alt_text,
        "title": obj.title,
        "prev": get_prev(obj.index),
        "next": get_next(obj.index, last),
        "last": "/" + str(last)
    }

class IndexView(generic.View):
    def get(self, request, *args, **kwargs):
        last = get_highest_index()
        obj = Comic.objects.get(id=last)
        context = get_context(obj)
        return render(request, "comics/comic.html", context)
    

class ComicView(generic.View):
    def get(self, request, pk, *args, **kwargs):
        obj = get_object_or_404(Comic, id=pk)
        context = get_context(obj)
        return render(request, "comics/comic.html", context)
    
class RandomView(generic.View):
    def get(self, request, *args, **kwargs):
        upper_limit = get_highest_index()
        random_index = random.randrange(1, upper_limit) # there is no comic 0
        return redirect("comics", pk=random_index)
