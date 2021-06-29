from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'dietjournal/index.html', context)