from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'welcome.html')


def current(request):
    return render(request, 'welcome.html')


def expanses(request):
    return render(request, 'welcome.html')
