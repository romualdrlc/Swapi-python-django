from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .services import fetch_people_data_by_id, fetch_list_by_resource

def people_detail(request, people_id):
    people = fetch_people_data_by_id(people_id)
    if not people:
        return JsonResponse({'error': 'People not found'}, status=404)
    return render(request, "people_detail.html", {"people": people})

def people_list(request):
    people_list = fetch_list_by_resource("people")
    if not people_list:
        return JsonResponse({'error': 'People list not found'}, status=404)
    return render(request, "people_list.html", {"people_list": people_list})

