from django.shortcuts import render
from django.core.cache import cache

# Create your views here.
from django.http import JsonResponse
from .services import fetch_people_data_by_id, fetch_list_by_resource

def people_detail(request, people_id):
    cache_key = "people_detail_{}".format(people_id)

    people = cache.get(cache_key)
    if people is None:
        print("🔴 Appel API SWAPI")
        people = fetch_people_data_by_id(people_id)

        if not people:
            return JsonResponse(
                {"error": "People not found"},
                status=404
            )

        cache.set(cache_key, people, timeout=60 * 60) # Cache for 1 hour
    else:
        print("🟢 Données depuis Redis")
    
    return render(request, "people_detail.html", {"people": people})

def people_list(request):
    cache_key = "people_list"

    people_list = cache.get(cache_key)

    if people_list is None:
        print("🔴 Appel API SWAPI")
        people_list = fetch_list_by_resource("people")

        if not people_list:
            return JsonResponse(
                {"error": "People list not found"},
                status=404
            )

        cache.set(cache_key, people_list, timeout=60 * 60) # Cache for 1 hour
    else:
        print("🟢 Données depuis Redis")

    return render(request, "people_list.html", {"people_list": people_list})