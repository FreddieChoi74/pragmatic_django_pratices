# Create your views here.
from django.shortcuts import HttpResponse

def hello_world(request):
    return HttpResponse('hello_world')