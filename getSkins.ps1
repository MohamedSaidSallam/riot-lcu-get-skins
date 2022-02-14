$wmicOutput = wmic PROCESS WHERE name=`'LeagueClientUx.exe`' GET commandline
$port = ($wmicOutput  | Select-String -Pattern '--app-port=([0-9]*)').matches.groups[1].Value
$token = ($wmicOutput | Select-String -Pattern '--remoting-auth-token=([\w-]*)').matches.groups[1].Value

$summonerId = (curl.exe --insecure -H "Accept: application/json" -u riot:$token https://127.0.0.1:$port/lol-summoner/v1/current-summoner | ConvertFrom-json).summonerId

$PSDefaultParameterValues['Out-File:Encoding'] = 'utf8'
curl.exe --insecure -H "Accept: application/json" -u riot:$token https://127.0.0.1:$port/lol-champions/v1/inventories/$summonerId/skins-minimal > skins.json
curl.exe --insecure -H "Accept: application/json" -u riot:$token https://127.0.0.1:$port/lol-loot/v1/player-loot > skinsLoot.json

curl.exe --insecure -H "Accept: application/json" -u riot:$token https://127.0.0.1:$port/lol-champions/v1/inventories/$summonerId/champions > champs.json