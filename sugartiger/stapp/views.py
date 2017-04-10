# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from httplib import HTTP
from django.shortcuts import render
from django.http import HttpResponse

def stapp_home_view(request):
    return HttpResponse("Sugar Tiger Landing")

def hello(request):
    #return HttpResponse("Hello world")
    return render(request, 'hello.html', {})

