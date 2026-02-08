from django.shortcuts import render, get_object_or_404, redirect 
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from .models import Comic
import random
from django.db.models import Q


def get_highest_index():
    return Comic.objects.all().count()


def get_prev(i):
    # the first comic is 1 so you can't go beyond that
    return "/1" if i == 1 else "/" + str(i - 1)


def get_next(i, last):
    return "/" + str(min(i + 1, last))


def get_context(obj):
    last = get_highest_index()
    return { 
        "img": "comics/"+obj.img_src,
        "alt_text": obj.alt_text,
        "title": obj.title,
        "uploaded": obj.pub_date,
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



def get_archive_context(object_list, query):
    '''
    Helper function for the archive page view
    
    :param object_list: comics to show
    :param query: Did the user search for something?

    Returns a list of dictionaries
    
    If there was a search query, it gives [{'header': 'results', 'objects': [comics matching search term]}]
    If there wasn't a search query, it gives [{'header': '2018', 'objects': [2018 comics]}, {'header': '2019', 'objects': [2019 comics]}]
    '''

    page_content = []

    if query: # if someone did a keyword search only show matching comics
        content_dict = {'header': 'Search results'}
        objs = []

        for obj in object_list:
            objs.append({
                "img": "comics/"+obj.img_src,
                "id" :obj.index,
                })
        content_dict['objects'] = objs
        page_content.append(content_dict)

    else: # if nothing was searched, show all comics separated by year
        content_dict = {}
        years = []
        
        for obj in object_list:
            upload_year = obj.pub_date.year # get the year of this comic

            # is this year already in the page_content list? If no, create a new dictionary

            if upload_year not in years:
                years.append(upload_year)
                new_dict = {
                    'header': upload_year,
                    'objects': []
                    }
                page_content.append(new_dict)

            year_dict = next((d for d in page_content if d['header'] == upload_year), None)
            
            year_dict['objects'].append({
                "img": "comics/"+obj.img_src,
                "id" :obj.index,
                })

    return page_content


def archive(request):

    # show comics by newest to oldest (exocomics and xkcd work like this)
    object_list = Comic.objects.all().order_by('index').reverse() 
    
    query = request.GET.get("search", None)
    if query:
        object_list= object_list.filter(
            Q(title__icontains=query)
            | Q(text__icontains=query)
            | Q(alt_text__icontains=query)
        )
       
    objs = get_archive_context(object_list, query)

    context = {
        "content": "Archive",
        "object_list": objs
        }
    return render(request, "comics/archive.html", context)