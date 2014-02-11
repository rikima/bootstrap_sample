from django.shortcuts import render
from django.template import Context, loader

from lib.http_decorators import http_response

@http_response('index/index.html')
def index(request):
    c = Context(dict())
    return c

