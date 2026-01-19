from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from .models import Comic


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

class ComicView(generic.View):
    def get(self, request, pk, *args, **kwargs):
        obj = get_object_or_404(Comic, id=pk)
        last = get_highest_index()
        context = { 
            "img": "comics/"+obj.img_src,
            "title": obj.title,
            "prev": get_prev(obj.index),
            "next": get_next(obj.index, last),
            "last": "/" + str(last)
            }
        return render(request, "comics/comic.html", context)


# def comic_1(request):
#     context = { 
#         "content": "1",
#         "img": "comics/2018-02-16.png",
#         "title": "First",
#         "prev": "comic_1",
#         "next": "comic_2"
#         }
#     return render(request, "comics/comic.html", context)

# def comic_2(request):
#     context = { 
#         "content": "2",
#         "img": "comics/2018-03-02.png",
#         "title": "Dangerous",
#         "prev": "comic_1",
#         "next": "comic_3"
#         }
#     return render(request, "comics/comic.html", context)

# def comic_3(request):
#     context = { 
#         "content": "3",
#         "img": "comics/2018-04-02.png",
#         "title": "Easter Egg",
#         "prev": "comic_2",
#         "next": "comic_4"
#         }
#     return render(request, "comics/comic.html", context)

# def comic_4(request):
#     context = { 
#         "content": "4",
#         "img": "comics/2018-04-25.png",
#         "title": "Anzac",
#         "prev": "comic_3",
#         "next": "comic_4"
#         }
#     return render(request, "comics/comic.html", context)