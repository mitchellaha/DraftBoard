import json
import requests
from datetime import datetime as dt
from datetime import timedelta as td
import pandas as pd
from pprint import pprint as pp
from data import keepers
from common import saveJson, loadJson

df = pd.read_excel('./data/Top 300.xlsx')


def mainCopy():
    players = {}

    for index, row in df.iterrows():  # for each row in the dataframe
        name = row["Player Name"]
        pWar = row["WAR"]
        pPos = row["Position"]

        pDict = {
            "WAR": pWar,
            "Position(s)": pPos
        }

        players[name] = pDict  # adds the player to the dictionary

    pp(players)
    # print a count of the total players
    print("Total Players: {}".format(len(players)))

    with open('players.json', 'w') as f:
        json.dump(players, f, ensure_ascii=False, indent=4)


def removeKeepers(players, keeperList):
    """
    Function To Remove Keepers from the players list.
    """
    # print a count of the total players before removing keepers
    print("Total Players Before Removing Keepers: {}".format(len(players)))
    removed = 0
    for k in keeperList:
        if k in players:
            removed += 1
            del players[k]
    # Print a Count Of Players
    print("Players Count After:", len(players))
    # Print a Count of Players Removed
    print("Players Removed:", removed)
    return players

def returnByPosition(players, position):
    """
    Function to return a list of players by position.
    """
    positionList = []
    for k, v in players.items():
        player = {}
        if position in v["Position(s)"]:
            playerDic = {}
            playerDic["Name"] = k
            playerDic["WAR"] = v["WAR"]
            positionList.append(playerDic)
    return positionList

# for each position in the json file create a new file for each position
def createPositionFiles(players):
    for k, v in players.items():
        position = v["Position(s)"]
        positionList = returnByPosition(players, position)
        saveJson(positionList, "./data/positions/{}.json".format(position))

if __name__ == "__main__":
    x = loadJson('./data/nonKeepers.json')
    # pp(returnByPosition(x, "OF"))
    createPositionFiles(x)
