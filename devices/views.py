from django.shortcuts import render
from django.http import HttpResponse
# import json
from django.http import JsonResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json

def hello_world(request):
    return render(request, 'hello.html', {'name': 'Corey'})


def profile(request):
    print("--------------")
    print(request)
    print("--------------")
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    return JsonResponse(data)

@csrf_exempt
def post_test(request):
    

    if request.method == "POST":
        json_data = json.loads(request.body)
        data = json_data['name']
        print('*'*50)
        print(data)
        print('*'*50)
    else:
        print('*'*50)
        print("not post")
        print('*'*50)
        
