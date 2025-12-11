from external.swapi.client import SwapiClient
from external.swapi.serializer import people_serializer     

def fetch_people_data_by_id(people_id):
    with SwapiClient() as client:
        people_data = client.get_people(people_id)
    return people_serializer(people_data)

def fetch_list_by_resource(resource_type):
    with SwapiClient() as client:
        print(f"Fetching list for resource type: {resource_type}")
        people_data = client.get_all_by_resource(resource_type)
        people_list = [people_serializer(people) for people in people_data]
    return people_list


