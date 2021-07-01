from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'message': 'Index Page'
    }
    return render(request, 'dietjournal/index.html', context)
