from external.swapi.client import SwapiClient
from external.swapi.serializer import planet_serializer     

def fetch_planet_data_by_id(planet_id):
    with SwapiClient() as client:
        planet_data = client.get_resource("planets", planet_id)
    return planet_serializer(planet_data)

def fetch_list_by_resource(resource_type):
    with SwapiClient() as client:
        print(f"Fetching list for resource type: {resource_type}")
        planet_data = client.get_all_by_resource(resource_type)
        planet_list = [planet_serializer(planet) for planet in planet_data]
    return planet_list