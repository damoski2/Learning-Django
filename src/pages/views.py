from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {}) #String of html code


def contact_view(request,*args, **kwargs):
    return render(request,'contact.html',{})


def about_view(request,*args, **kwargs):
    my_context = {
        "title": "this is about me",
        "my_number": 123,
        "my_list": [123,456,222,312,"ABC"],
        "this_is_true": True,
        "my_html": "<h1>Hello World</h1>"
    }
    return render(request,'about.html',my_context)
