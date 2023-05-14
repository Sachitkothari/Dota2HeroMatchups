import requests
import json

# Code I ran one time to get the heroes.json file
r = requests.get("https://api.opendota.com/api/heroes")
with open('heroes.json', 'w') as out:
                json.dump(r.json(), out, sort_keys=True, indent='\t')   