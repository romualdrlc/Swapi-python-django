from django.shortcuts import render
from django.core.cache import cache
from django.http import JsonResponse
from .services import fetch_vehicle_data_by_id, fetch_list_by_resource

# Create your views here.
def vehicle_detail(request, vehicle_id):
    cache_key = "vehicle_detail_{}".format(vehicle_id)

    vehicle = cache.get(cache_key)
    if vehicle is None:
        print("🔴 Appel API SWAPI")
        vehicle = fetch_vehicle_data_by_id(vehicle_id)

        if not vehicle:
            return JsonResponse(
                {"error": "Vehicle not found"},
                status=404
            )

        cache.set(cache_key, vehicle, timeout=60 * 60) # Cache for 1 hour
    else:
        print("🟢 Données depuis Redis")

    return render(request, "vehicle_detail.html", {"vehicle": vehicle})

def vehicle_list(request):
    cache_key = "vehicle_list"

    vehicle_list = cache.get(cache_key)

    if vehicle_list is None:
        print("🔴 Appel API SWAPI")
        vehicle_list = fetch_list_by_resource("vehicles")

        if not vehicle_list:
            return JsonResponse(
                {"error": "Vehicle list not found"},
                status=404
            )

        cache.set(cache_key, vehicle_list, timeout=60 * 60) # Cache for 1 hour
    else:
        print("🟢 Données depuis Redis")

    return render(request, "vehicle_list.html", {"vehicle_list": vehicle_list})