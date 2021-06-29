from django.urls import path
from . import views

app_name = 'dietjournal'
urlpatterns = [
    path('', views.index, name='index')
]