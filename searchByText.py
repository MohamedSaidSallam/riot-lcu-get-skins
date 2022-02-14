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

LOOT_EXT = '.loot'

players = {}
playersLoot = {}
for filename in filenames:
    if not filename.endswith('.json'):
        continue

    with codecs.open(PLAYERS_FOLDER + '/' + filename, 'r', encoding='utf-8-sig') as inputFile:
        jsonData = json.load(inputFile)
        fileNameWithoutExt = filename[:-len('.json')]
        if fileNameWithoutExt.endswith(LOOT_EXT):
            playersLoot[fileNameWithoutExt[:-len(LOOT_EXT)]] = jsonData
        else:
            players[fileNameWithoutExt] = jsonData

SEARCH_STRING = ' '.join(args['searchString']).lower()

filteredSkinsPerPlayer = {playerName: [] for playerName in players}


def doesSkinMatchSearch(skinName):
    return SEARCH_STRING in skinName.lower()


for playerKey, skins in players.items():
    for skin in skins:
        if skin['ownership']['owned'] and doesSkinMatchSearch(skin['name']):
            filteredSkinsPerPlayer[playerKey].append(skin['name'])

for playerKey, skins in playersLoot.items():
    nameKey = 'itemDesc'
    for skin in skins:
        if skin['displayCategories'] == 'SKIN' and doesSkinMatchSearch(skin[nameKey]):
            filteredSkinsPerPlayer[playerKey].append(skin[nameKey] + ' (loot)')

for playerName, playerSkins in filteredSkinsPerPlayer.items():
    print(playerName)
    if len(playerSkins) == 0:
        print('\t None :(')
    else:
        for playerSkin in playerSkins:
            print('\t'+playerSkin)
