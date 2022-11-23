import time
from requests import request
from tabulate import tabulate


def get_places_table(place_coordinates: str, place_radius, keyword: str, limit: int):
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={place_coordinates}&radius={place_radius}&keyword={keyword}&key=AIzaSyAuFlBfY0G-N7voGx7ckRwlWuGWShRyDz4"

    response = request("GET", url).json()
    result = response['results']
    next_page_token = response["next_page_token"]
    full_results = [result]
    time.sleep(2)
    while True:
        next_url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken={next_page_token}&key=AIzaSyAuFlBfY0G-N7voGx7ckRwlWuGWShRyDz4'
        next_request = request("GET", next_url).json()
        if 'next_page_token' in next_request:
            full_results.append(next_request['results'])
            next_page_token = next_request["next_page_token"]
            time.sleep(2)
        else:
            break
    table = []
    count = 0
    for i in range(len(full_results)):
        for index, item in enumerate(full_results[i]):
            count += 1
            table.append([item['name'], item['vicinity'], item['rating']])
            print(count, item['name'])
            if count >= int(limit):
                break

    table.sort(key=lambda x: x[2])
    table.reverse()

    return tabulate(table, tablefmt="html", headers=["Business's name", "Address", "Rating"])
