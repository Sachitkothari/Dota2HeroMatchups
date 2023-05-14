import HeroMatchups
import HeroFromHeroID
import json
import string

hero_name = input("Enter a hero: ")
num = HeroFromHeroID.heroID_from_hero(hero_name)
matchups = HeroMatchups.get_hero_matchups(num)
print(matchups[:5])
