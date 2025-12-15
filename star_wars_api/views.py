# star_wars_api/views.py
from django.shortcuts import render
from django_redis import get_redis_connection
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    return render(request, "home.html")

def clear_swapi_cache(request):
    redis_client = get_redis_connection("default")
    keys = redis_client.keys("swapi:*")
    if keys:
        redis_client.delete(*keys)
    return HttpResponseRedirect(reverse('home'))
