import argparse
import codecs
import json
from os import walk

parser = argparse.ArgumentParser(
    description='Searches the skins json files in the players folder for a given string')
parser.add_argument('searchString', nargs='+',
                    help='the string to search for in the skins json (using .contains())')
parser.add_argument('--players-folder', nargs='*', default=['players'],
                    help='the folder that contains the skins json files')

args = vars(parser.parse_args())

PLAYERS_FOLDER = ' '.join(args['players_folder'])

filenames = next(walk(PLAYERS_FOLDER), (None, None, []))[2]

players = {}
for filename in filenames:
    if not filename.endswith('.json'):
        continue

    jsonData = None

    filePath = PLAYERS_FOLDER + '/' + filename
    try:
        with open(filePath, 'r') as inputFile:
            jsonData = json.load(inputFile)
    except:
        with codecs.open(filePath, 'r', encoding='utf-8-sig') as inputFile:
            jsonData = json.load(inputFile)

    players[filename[:-len('.json')]] = jsonData

SEARCH_STRING = ' '.join(args['searchString']).lower()

filteredSkinsPerPlayer = {playerName: [] for playerName in players}

for playerKey, skins in players.items():
    isLoot = playerKey.endswith('.loot')
    nameKey = 'itemDesc' if isLoot else 'name'
    for skin in skins:
        isSkinAvailable = skin['displayCategories'] == 'SKIN' if isLoot else isLoot and skin['ownership']['owned']
        matchesSearch = SEARCH_STRING in skin[nameKey].lower()
        if (isSkinAvailable) and matchesSearch:
            filteredSkinsPerPlayer[playerKey].append(skin[nameKey])

for playerName, playerSkins in filteredSkinsPerPlayer.items():
    print(playerName)
    if len(playerSkins) == 0:
        print('\t None :(')
    else:
        for playerSkin in playerSkins:
            print('\t'+playerSkin)
