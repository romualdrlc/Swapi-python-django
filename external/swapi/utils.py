# external/swapi/utils.py

def parse_int(value):
    """
    Essaie de convertir une chaîne en entier, sinon retourne None.
    Utile pour gérer les valeurs comme 'unknown' retournées par SWAPI.
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def format_date_swapi(date_str):
    """
    Transforme la notation de date SWAPI (ex: '19BBY') en texte lisible.
    """
    if not date_str:
        return None
    return date_str.replace("BBY", " avant la bataille de Yavin").replace("ABY", " après la bataille de Yavin")

def ensure_http_url(url):
    if not url:
        return None
    if url.startswith("http://") or url.startswith("https://"):
        return url
    return "https://" + url  # ou "http://" si tu préfères
