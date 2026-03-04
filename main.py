


from urllib.parse import quote

import requests
from dotenv import load_dotenv

load_dotenv()


def get_bbox(city):
    osm_url = f"https://nominatim.openstreetmap.org/search?q={quote(city)}&format=json"
    headers = {'User-Agent': 'OpenAQCityBBox'}

    response = requests.get(osm_url, headers=headers).json()

    if not response:
        return None

    # boundingbox sisältää löydetyn kaupungin rajat
    # siinä on 4 koordinaattipisettä
    osm_bbox = response[0]['boundingbox']

    # OpenStreetMapin bounding boxin koordinaatit ovat ao järjestyksessä
    # min_y, max_y, min_x, max_x
    min_lat, max_lat, min_lon, max_lon = osm_bbox

    # järjestetään uudelleen openAQ:lle sopivaan muotoon: min_x, min_y, max_x, max_y
    openaq_bbox = f"{min_lon},{min_lat},{max_lon},{max_lat}"

    return openaq_bbox

API_KEY = 'OMA API KEY'

# tämä funktio saa parametrinaan kaupungin bounding boxin get_bbox-funktiolta
def get_openaq_locations_by_bbox(_bbox):
    response = requests.get(
        f'https://api.openaq.org/v3/locations?limit=1000&page=1&order_by=id&sort_order=asc&bbox={_bbox}',
        headers={'X-API-Key': API_KEY})
    _locations = []
    # muista, että http-statuskoodi 200 on OK
    # voit myös heittää poikkeuksen,
    # jos statuskoodi on jotakin muuta kuin 200
    if response.status_code == 200:
        _locations = response.json()['results']

    return _locations




if __name__ == "__main__":
    bbox = get_bbox("Oulu")
    print(bbox)