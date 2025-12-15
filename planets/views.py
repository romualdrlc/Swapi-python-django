from django.shortcuts import render
from django.core.cache import cache
from django.http import JsonResponse
from .services import fetch_planet_data_by_id, fetch_list_by_resource

# Create your views here.
def planet_detail(request, planet_id):
    cache_key = "planet_detail_{}".format(planet_id)

    planet = cache.get(cache_key)
    if planet is None:
        print("🔴 Appel API SWAPI")
        planet = fetch_planet_data_by_id(planet_id)

        if not planet:
            return JsonResponse(
                {"error": "Planet not found"},
                status=404
            )

        cache.set(cache_key, planet, timeout=60 * 60) # Cache for 1 hour
    else:
        print("🟢 Données depuis Redis")
    
    return render(request, "planet_detail.html", {"planet": planet})

def planet_list(request):
    cache_key = "planet_list"

    planet_list = cache.get(cache_key)

    if planet_list is None:
        print("🔴 Appel API SWAPI")
        planet_list = fetch_list_by_resource("planets")

        if not planet_list:
            return JsonResponse(
                {"error": "Planet list not found"},
                status=404
            )

        cache.set(cache_key, planet_list, timeout=60 * 60) # Cache for 1 hour
    else:
        print("🟢 Données depuis Redis")

    return render(request, "planet_list.html", {"planet_list": planet_list})