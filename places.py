import requests
from tabulate import tabulate


def get_places_table(place_coordinates: str, place_radius, keyword: str, limit: int):
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken=nextPageToken&location={place_coordinates}&radius={place_radius}&keyword={keyword}&key=AIzaSyAuFlBfY0G-N7voGx7ckRwlWuGWShRyDz4"

    response = requests.request("GET", url).json()
    print(response)

    table = []
    for index, item in enumerate(response['results']):
        table.append([item['name'], item['vicinity'], item['rating']])
        if index >= int(limit):
            break

    table.sort(key=lambda x: x[2])
    table.reverse()

    return tabulate(table, tablefmt="html", headers=["Business's name", "Address", "Rating"])
