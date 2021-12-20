from django.shortcuts import render
from django.http import HttpResponse
# import json
from django.http import JsonResponse
# Create your views here.

def hello_world(request):
    return render(request, 'hello.html', {'name': 'Corey'})


def profile(request):
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    return JsonResponse(data)
