
import random

import districts
import characters
import interactions
from player import Player


class Game(object):
    """Holds game information"""

    def __init__(self, playerCount, deck=None, seed=None, input=None, output=None):
        self.playerCount = playerCount
        self.players = [Player(i+1) for i in range(playerCount)]
        self.deck = deck if deck else districts.createUnshuffledDeck()
        self.rng = random.Random(seed)

        if input is None:
            input = interactions.ConsoleInput()

        if output is None:
            output = interactions.ScreenPrinter()

        self.eventQueue = []

        self.characterInteraction = interactions.Interactions(input, output, self.eventQueue)
        self.endDistricts = 8
        self.characters = characters.characters

        self.isLastTurn = False

    def gameSetup(self, firstPlayer=None):

        if firstPlayer is None:
            firstPlayer = self.rng.randint(0, self.playerCount-1)
        
        self.players[firstPlayer].hasFirstPick = True

        for p in self.players:
            p.districts.extend(self.deck.drawCards(4))
            p.gold = 2
        

    def chooseCharacters(self):

        # First we need to arrange the order of the players
        firstPlayerIndex = [i for i,v in enumerate(self.players) if v.hasFirstPick]

        assert len(firstPlayerIndex)==1, "First pick players: {}".format(firstPlayerIndex)

        firstPlayerIndex = firstPlayerIndex[0]

        self.players = self.players[firstPlayerIndex:] + self.players[:firstPlayerIndex]

        # Copy game characters so we don't destroy it
        gameChars = {i+1: v for i, v in enumerate(self.characters)}

        # TODO this needs to be properly parameterised, only valid for 2

        if self.playerCount==2:
            # Pick a character to discard
            discardIndex = self.rng.randint(1,8)

            del gameChars[discardIndex]

            self.characterInteraction.getCharacterInput(gameChars, self.players[0], True)

            self.characterInteraction.getCharacterInput(gameChars, self.players[1], True)

            self.characterInteraction.getCharacterInput(gameChars, self.players[1], False)

            self.characterInteraction.getCharacterInput(gameChars, self.players[0], True)

            self.characterInteraction.getCharacterInput(gameChars, self.players[0], False)

            self.characterInteraction.getCharacterInput(gameChars, self.players[1], True)
        else:
            raise("Not supported for anything other than two player")

    def playerTurn(self, player, character):
        # Offer options
        optionsDict = {1: ("Perform character effect", 1, self.characterInteraction.performCharacterEffect),
                       2: ("Play action", 1, self.characterInteraction.takeCardsOrGold),
                       3: ("Build", 1, self.characterInteraction.build)}

        actionsRemain = True
        while(actionsRemain):
            options = {}
            for k, (name, count, func) in optionsDict.iteritems():
                if count > 0:
                    options[k] = name
                
            if len(options) >= 1:
                self.characterInteraction.output.outputOptions(options, player.playerNo)
                inp = self.characterInteraction.input.input()
                choice = int(inp)
                if choice == 0:
                    actionsRemain = False
                elif choice in options.keys():

                    kwargs = {"deck": self.deck, "player": player, "character": character, "endDistricts": self.endDistricts}
                    n, c, f = optionsDict[choice]
                    f(**kwargs)
                    optionsDict[choice] = (n, c-1, f)
                else:
                    self.characterInteraction.output("Error, choose again", player.playerNo)
            else:
                actionsRemain = False

    def cycleThroughPlayers(self):

        for c in self.characters:
            playerList = [i for i in self.players if c in i.characters]
            assert len(playerList) <= 1, "Following players have character {} - {}".format(c, playerList)
            if len(playerList) != 0:
                player = playerList[0]
                self.playerTurn(player, c)

    def cleanUpAfterTurn(self):
        for p in self.players:
            p.characters = []

    def playGame(self):
        self.gameSetup()
        while (not self.isLastTurn):
            self.chooseCharacters()
            self.cycleThroughPlayers()
            self.cleanUpAfterTurn()
        return self.countVictoryPoints()

    def countVictoryPoints(self):
        ps = [sum(d.victoryPoints for d in p.districts) for p in self.players]
        return ps