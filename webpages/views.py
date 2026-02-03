from django.shortcuts import render
from comics.models import Comic


def sketchbook(request):
    context = {"content": "Sketchbooks"}
    return render(request, "webpages/index.html", context)

def sketchbook_2017(request):
    context = {"content": "Sketchbook 2017"}
    return render(request, "webpages/index.html", context)

def sketchbook_2018(request):
    context = {"content": "Sketchbook 2018"}
    return render(request, "webpages/index.html", context)

def sketchbook_2019(request):
    context = {"content": "Sketchbook 2019"}
    return render(request, "webpages/index.html", context)


def art(request):
    context = {"content": "Art"}
    return render(request, "webpages/index.html", context)

def about(request):
    context = {"content": "Je ne sais pas"}
    return render(request, "webpages/index.html", context)