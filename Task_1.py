import requests

url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
resp = requests.get(url)
all_hero = resp.json()


def get_hiro_intelligence_1(name):
    hero_int = 0
    hero_name = None
    for b in name:
        for i in all_hero:
            if b in i['name']:
                stat = (i['powerstats'])
                if int(stat["intelligence"]) > hero_int:
                    hero_int = int(stat["intelligence"])
                    hero_name = i['name']

    print(f'Самый умный {hero_name}, его интеллект составляет {hero_int} единиц.')


get_hiro_intelligence_1(["Hulk", "Captain America", "Thanos"])
