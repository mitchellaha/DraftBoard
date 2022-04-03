
from turtle import position


class players:
    def __init__(self, name, Position, WAR):
        self.name = name
        self.Position = Position
        self.WAR = WAR
        self.Position_list = []

    def add_Position(self, Position):
        self.Position_list.append(Position)

x = players("Barry Bonds", "Right", "1")
