import json
import requests
from datetime import datetime as dt
from datetime import timedelta as td
import pandas as pd
from pprint import pprint as pp
from data import keepers
from common import saveJson, loadJson
from tabulate import tabulate

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

# Find the maximum WAR in the json file
def findMaxWAR(fileName):
    with open(fileName) as f:
        positions = json.load(f)
    maxWAR = 0.0
    for player in positions:
        if player["WAR"] > maxWAR:
            maxWAR = player["WAR"]
    return float(maxWAR)

# Find 2nd highest WAR in the json file
def find2ndMaxWAR(fileName):
    with open(fileName) as f:
        positions = json.load(f)
    maxWAR = 0.0
    for player in positions:
        if player["WAR"] > maxWAR:
            maxWAR = player["WAR"]
    secondMaxWAR = 0.0
    for player in positions:
        if player["WAR"] > secondMaxWAR and player["WAR"] < maxWAR:
            secondMaxWAR = player["WAR"]
    return float(secondMaxWAR)

# Find the 5 highest WARs in the json file
def find5MaxWAR(fileName):
    with open(fileName) as f:
        positions = json.load(f)
    maxWAR = 0
    for player in positions:
        if player["WAR"] > maxWAR:
            maxWAR = player["WAR"]
            playerName = player["Name"]
    secondMaxWAR = 0
    for player in positions:
        if player["WAR"] > secondMaxWAR and player["WAR"] < maxWAR:
            secondMaxWAR = player["WAR"]
            playerName2 = player["Name"]
    thirdMaxWAR = 0
    for player in positions:
        if player["WAR"] > thirdMaxWAR and player["WAR"] < secondMaxWAR:
            thirdMaxWAR = player["WAR"]
            playerName3 = player["Name"]
    fourthMaxWAR = 0
    for player in positions:
        if player["WAR"] > fourthMaxWAR and player["WAR"] < thirdMaxWAR:
            fourthMaxWAR = player["WAR"]
            playerName4 = player["Name"]
    fifthMaxWAR = 0
    for player in positions:
        if player["WAR"] > fifthMaxWAR and player["WAR"] < fourthMaxWAR:
            fifthMaxWAR = player["WAR"]
            playerName5 = player["Name"]
    return (playerName, maxWAR, playerName2, secondMaxWAR, playerName3, thirdMaxWAR, playerName4, fourthMaxWAR, playerName5, fifthMaxWAR)

# Create a copy of the json file and save as a new file
def createCopy(fileName):
    with open(fileName) as f:
        positions = json.load(f)
    saveJson(positions, "./data/positions/copy.json")

if __name__ == "__main__":
    createCopy("./data/positions/SS.json")

    # First base
    print(find5MaxWAR("./data/positions/1B.json"))
    difference = (findMaxWAR("./data/positions/1B.json")) - (find2ndMaxWAR("./data/positions/1B.json"))
    print("1B Difference:", difference)
    # 2nd Base
    print(find5MaxWAR("./data/positions/2B.json"))
    difference2 = (findMaxWAR("./data/positions/2B.json")) - (find2ndMaxWAR("./data/positions/2B.json"))
    print("2B Difference:", difference2)
    # 3rd Base
    print(find5MaxWAR("./data/positions/3B.json"))
    difference3 = (findMaxWAR("./data/positions/3B.json")) - (find2ndMaxWAR("./data/positions/3B.json"))
    print("3B Difference:", difference3)
    # SS
    print(find5MaxWAR("./data/positions/SS.json"))
    difference4 = (findMaxWAR("./data/positions/SS.json")) - (find2ndMaxWAR("./data/positions/SS.json"))
    print("SS Difference:", difference4)
    # OF
    print(find5MaxWAR("./data/positions/OF.json"))
    difference5 = (findMaxWAR("./data/positions/OF.json")) - (find2ndMaxWAR("./data/positions/OF.json"))
    print("OF Difference:", difference5)
    # C
    print(find5MaxWAR("./data/positions/C.json"))
    difference6 = (findMaxWAR("./data/positions/C.json")) - (find2ndMaxWAR("./data/positions/C.json"))
    print("C Difference:", difference6)
    # P
    print(find5MaxWAR("./data/positions/SP.json"))
    difference7 = (findMaxWAR("./data/positions/SP.json")) - (find2ndMaxWAR("./data/positions/SP.json"))
    print("SP Difference:", difference7)
