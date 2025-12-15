# external/swapi/serializers.py

from external.swapi.utils import parse_int, format_date_swapi, ensure_http_url, fetch_swapi

def people_serializer(data):
    if not data:
        return None

    # Extraire l'id depuis l'URL
    url = data.get("url", "")
    people_id = _extract_id_from_url(url)

    return {
        "id": people_id,
        "nom": data.get("name"),
        "taille": parse_int(data.get("height")),
        "poids": parse_int(data.get("mass")),
        "couleur_cheveux": data.get("hair_color"),
        "couleur_yeux": data.get("eye_color"),
        "films": [
            fetch_swapi(url).get("title", "Inconnu") 
            for url in data.get("films", [])
        ],
        "genre": data.get("gender"),
        "date_naissance": format_date_swapi(data.get("birth_year")),
        "planete_origine": fetch_swapi(data.get("homeworld")).get("name"),
    }



def planet_serializer(data):
    """
    Transforme les données brutes d'une planète SWAPI en dict simplifié.
    """
    if not data:
        return None
    
    url = data.get("url", "")
    planet_id = _extract_id_from_url(url)

    return {
        "id": planet_id,
        "nom": data.get("name"),
        "climat": data.get("climate"),
        "gravite": data.get("gravity"),
        "terrain": data.get("terrain"),
        "population": data.get("population"),
        "residents": [
            {
                "id": _extract_id_from_url(url),
                "name": fetch_swapi(url).get("name")
            }
            for url in data.get("residents", [])
        ],
        "films": [
            {
                "id": _extract_id_from_url(url),
                "title": fetch_swapi(url).get("title")
            }
            for url in data.get("films", [])
        ],
    }


def _extract_id_from_url(url):
    """
    Extrait l'ID d'une ressource SWAPI à partir de son URL.
    """
    if not url:
        return None
    return url.rstrip('/').split('/')[-1]  # prend le dernier segment après la dernière /