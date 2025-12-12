import httpx
import os

SWAPI_API_URL = os.getenv("SWAPI_API_URL")

class SwapiClient:

    def __init__(self):
        self.base_url = SWAPI_API_URL
        self.session = httpx.Client()

    def get_people(self, person_id):
        return self.get_resource("people", person_id)

    def get_planet(self, planet_id):
        return self.get_resource("planets", planet_id)

    def get_starship(self, starship_id):
        return self.get_resource("starships", starship_id)
    
    def get_vehicle(self, vehicle_id):
        return self.get_resource("vehicles", vehicle_id)
    
    def get_film(self, film_id):
        return self.get_resource("films", film_id)
    
    def get_all_by_resource(self, resource_type):
        url = f"{self.base_url.strip('/')}/{resource_type}/"
        response = self.session.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get('results', [])
    
    def get_resource(self, resource_type, resource_id):
        url = f"{self.base_url}/{resource_type}/{resource_id}/"
        print(f"Fetching URL: {url}")
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()
    
    def fetch_url(self, url):
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.session.close()

