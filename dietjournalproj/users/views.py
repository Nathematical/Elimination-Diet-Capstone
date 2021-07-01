from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import User
import django.contrib.auth

def register(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        photo = request.FILES.get('photo')
        print(request.FILES)
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.photo = photo
        user.save()
        django.contrib.auth.login(request, user)
        return HttpResponseRedirect(reverse('dietjournal:index'))

    return render(request, 'users/register.html')

        