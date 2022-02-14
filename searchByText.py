import json
import sys
import codecs
from os import walk

PLAYERS_FOLDER = 'players'

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

SEARCH_STRING = ' '.join(sys.argv[1:]).lower()

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
