import json

def loadJson(dir):
    with open(dir) as f:
        players = json.load(f)

    return players

def saveJson(dict, filename):
    """
    Function to save the players dictionary to a json file.
    """
    with open(filename, 'w') as f:
        json.dump(dict, f, ensure_ascii=False, indent=4)
