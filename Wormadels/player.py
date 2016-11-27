
players = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight"]

class Player(object):

    def __init__(self, playerNo, name=None):
        self.playerNo = playerNo
        self.name = name if name else players[playerNo]
        self.characters = []
        self.districts = []
        self.gold = 0