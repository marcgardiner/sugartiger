# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from httplib import HTTP
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html', {'books': books, 'query': q})
    return render(request, 'search_form.html', {'error': error})

def search_results(request):
    return render(request, 'search_results.html', {})

def stapp_home_view(request):
    return HttpResponse("Sugar Tiger Landing")

def hello(request):
    #return HttpResponse("Hello world")
    return render(request, 'hello.html', {})

