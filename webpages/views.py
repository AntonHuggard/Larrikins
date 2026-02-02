from django.shortcuts import render

# def index(request):
#     context = {"content": "Larrikins fun times"}
#     return render(request, "webpages/index.html", context)


def archive(request):
    context = {"content": "Archive"}
    return render(request, "webpages/index.html", context)

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


def other(request):
    context = {"content": "Other stuff"}
    return render(request, "webpages/index.html", context)

def about(request):
    context = {"content": "Je ne sais pas"}
    return render(request, "webpages/index.html", context)