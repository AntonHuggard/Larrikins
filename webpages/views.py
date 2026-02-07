from django.shortcuts import render


def about(request):
    context = {"content": "Je ne sais pas"}
    return render(request, "webpages/index.html", context)