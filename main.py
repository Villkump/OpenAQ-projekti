


from urllib.parse import quote

import requests


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




if __name__ == "__main__":
    bbox = get_bbox("Oulu")
    print(bbox)