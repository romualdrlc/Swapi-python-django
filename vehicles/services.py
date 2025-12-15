from external.swapi.client import SwapiClient
from external.swapi.serializer import vehicle_serializer     

def fetch_vehicle_data_by_id(vehicle_id):
    with SwapiClient() as client:
        vehicle_data = client.get_resource("vehicles", vehicle_id)
    return vehicle_serializer(vehicle_data)

def fetch_list_by_resource(resource_type):
    with SwapiClient() as client:
        print(f"Fetching list for resource type: {resource_type}")
        vehicle_data = client.get_all_by_resource(resource_type)
        vehicle_list = [vehicle_serializer(vehicle) for vehicle in vehicle_data]
    return vehicle_list