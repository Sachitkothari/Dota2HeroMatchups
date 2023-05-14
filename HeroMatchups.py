import requests
import json
import HeroFromHeroID

# Avg number of games invoker has played vs another is 70. Assuming 70 for all
# For invoker, <10 games vs 3 heroes, <15 vs 5 and <20 vs 7. 
# At this point I pick <15 for non trivial number of games
def get_hero_matchups(hero_id):
    url = f"https://api.opendota.com/api/heroes/{hero_id}/matchups"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")
    data = response.json()
    matchups = []
    for item in data:
        if(item['games_played']>15):
            dict = {
                "winrate": item['wins']/item['games_played'],
                "hero": HeroFromHeroID.hero_from_heroID(item['hero_id'])
            }
            if(dict['hero']!="Not Found"):
                matchups.append(dict)

    sorted_matchups = sorted(matchups, key=lambda x: x['winrate'], reverse=False)
    return sorted_matchups