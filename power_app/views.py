from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    context = {'language': 'Python'}
    return render(request, 'power_app/index.html', context)
