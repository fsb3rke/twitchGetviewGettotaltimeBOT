import json
with open('pref.json') as f:
    data = json.load(f)
streamUrl = data["informations"]["STREAMURL"]
streamerName = data["informations"]["STREAMERNAME"]