from django.shortcuts import render
from django.http import HttpResponse
from .models import User
import json

def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(request.body)
        user = User.objects.create_user(
            username=data['username'], 
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'], 
            password=data['password'])
        user.photo = data['photo']
        user.save()
        return render(request, 'users/register.html')
    else:
        return render(request, 'users/register.html')