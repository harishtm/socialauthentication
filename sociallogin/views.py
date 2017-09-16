# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth import logout

# Create your views here.

def home(request):
    return render(request, 'home.html', locals())


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
