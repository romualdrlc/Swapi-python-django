# external/swapi/serializers.py

from external.swapi.utils import parse_int, format_date_swapi, ensure_http_url

def people_serializer(data):
    if not data:
        return None

    # Extraire l'id depuis l'URL
    url = data.get("url", "")
    people_id = None
    if url:
        people_id = url.rstrip('/').split('/')[-1]  # prend le dernier segment après la dernière /

    return {
        "id": people_id,
        "nom": data.get("name"),
        "taille": parse_int(data.get("height")),
        "poids": parse_int(data.get("mass")),
        "couleur_cheveux": data.get("hair_color"),
        "couleur_yeux": data.get("eye_color"),
        "genre": data.get("gender"),
        "date_naissance": format_date_swapi(data.get("birth_year")),
        "planete_origine": ensure_http_url(data.get("homeworld")),
    }



def planet_serializer(data):
    """
    Transforme les données brutes d'une planète SWAPI en dict simplifié.
    """
    if not data:
        return None

    return {
        "nom": data.get("name"),
        "climat": data.get("climate"),
        "terrain": data.get("terrain"),
        "population": data.get("population"),
    }
