import HeroMatchups
import json

num = int(input("Enter a heroID: "))
matchups = HeroMatchups.get_hero_matchups(num)
print(matchups[:5])
