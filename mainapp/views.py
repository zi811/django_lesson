from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.

class HelloWorldView(View):
    def get(self, *args, **kwargs):
        return HttpResponse('hello world')


def check_kwargs(request, **kwargs):
    return HttpResponse('kwatgs:<br>{kwargs}')