# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'insert_me':"Now I'm from firstAp/index.html!"}
    return render(request,'firstAp/index.html',context=my_dict)
