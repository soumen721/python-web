from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Welcome to WEB APP')


def new(request):
    return HttpResponse('New Product Page')

