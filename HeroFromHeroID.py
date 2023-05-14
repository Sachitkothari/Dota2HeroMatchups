import requests
import json

def hero_from_heroID(hero_id):
    with open('heroes.json', 'r') as f:
    # Load the JSON data
        hero_data = json.load(f)
    for hero in hero_data:
        if hero['id'] == hero_id:
            # Found the hero with ID 129
            return hero["localized_name"]
            break
        else:
            # Hero with ID 129 not found
            if(hero['id']>hero_id):
                break
    return "Not Found"