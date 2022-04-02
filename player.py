
class players:
    def __init__(self, name, Position, WAR):
        self.name = name
        self.Position = Position
        self.WAR = WAR
        self.WAR_list = []

    def add_WAR(self, WAR):
        self.WAR_list.append(WAR)

x = players("Barry Bonds", "Right", "1")
