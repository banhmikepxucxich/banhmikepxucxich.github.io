import requests

request = requests.get('https://pokeapi.co/api/v2/pokemon/umbreon')
data = request.json()

print('\npokemon emerald\n')

print('---------- name ----------')
print(f'name: {data["name"]}')

print('---------- base stats -----------')
base_stats = data['stats']
total_stat = 0
for stat in base_stats:
    print(f'{stat["stat"]["name"]}: {stat["base_stat"]}')
    total_stat += stat["base_stat"]

print(f'total: {total_stat}')

print('---------- types -----------')
for _type in data['types']:
    print(_type['type']['name'])

print('---------- abilities ----------')
for ability in data['abilities']:
    if ability['is_hidden'] == False:
        print(ability['ability']['name'])
    else:
        print(f'hidden ability: {ability["ability"]["name"]}')

print('---------- moves ----------')
moves = data['moves']
moves_in_emerald = []
for move in moves:
    for version in move['version_group_details']:
        if version['version_group']['name'] == 'emerald':
            moves_in_emerald.append(move)

for move in moves_in_emerald:
    print(move['move']['name'])

print('---------- sprites ----------')
print(f'official artwork: {data["sprites"]["other"]["official-artwork"]["front_default"]}')
print(f'emerald front sprite: {data["sprites"]["versions"]["generation-iii"]["emerald"]["front_default"]}')
print(f'emerald shiny front sprite: {data["sprites"]["versions"]["generation-iii"]["emerald"]["front_shiny"]}')

print('---------- misc ----------')
print(f'id: {data["id"]}')
print(f'height: {data["height"]}')
print(f'base experience: {data["base_experience"]}')
print(f'order: {data["order"]}')
print(f'weight: {data["weight"]}')