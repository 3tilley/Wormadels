
from player import players

class Interactions(object):
    def __init__(self, input, output, eventQueue):
        self.input = input
        self.output = output
        self.eventQueue = eventQueue

    def getCharacterInput(self, gameChars, player, isPick):
        verb = None
        if isPick:
            verb = "pick"
        else:
            verb = "discard"

        self.output.clearScreen()

        self.output.output("Player {} please {} a card".format(player.name, verb), player.playerNo)

        self.output.outputOptions(gameChars, player.playerNo)

        pick = self.input.input()

        while pick not in gameChars.keys():
            self.output.output("Naughty, that's not a valid choice. Try again.", player.playerNo)
            pick = self.input.input()

        self.output.output("You chose {}".format(gameChars[pick]), player.playerNo)
        
        if isPick:
            player.characters.append(gameChars[pick])

        del gameChars[pick]

        return pick

    def takeCardsOrGold(self, player, deck, **kwargs):
        self.output.outputOptions(["Take gold", "Take cards"], player.playerNo)
        inp = self.input.input()
        if int(inp)==1:
            player.gold += 2
        elif int(inp)==2:
            cards = deck.drawCards(2)
            c, d = self.discardAndTakeCards(player, cards, 1)
            deck.returnCards(d)
            player.districts.extend(c)

    def performCharacterEffect(self, player, character, deck, **kwargs):
        pass

    def build(self, player, character, endDistricts=8, **kwargs):
        choices = [d for d in player.districts if d.cost <= player.gold]
        self.output.outputOptions(choices, player.playerNo)
        buildIndex = self.input.input()
        chosenDist = [i for i, v in enumerate(player.districts) if (v.name==choices[buildIndex].name)][0]
        dist = player.districts.pop(chosenDist)
        player.builtDistricts.append(dist)
        player.gold -= dist.cost
        if len(player.builtDistricts)==endDistricts:
            self.eventQueue("Game end triggered")

    def discardAndTakeCards(self, player, cards, numberToDiscard):
        self.output.output(
            "Discard {} card{}".format(numberToDiscard, "s" if numberToDiscard > 1 else ""), player.playerNo)
        discards = []
        for i in range(numberToDiscard):
            self.output.outputOptions(cards, player.playerNo)
            inp = self.input.input()
            # TODO put error checking here
            d = cards.pop(inp-1)
            discards.append(d)

        return(cards, discards)

class ScreenPrinter(object):
    def __init__(self):
        pass

    def output(self, message, playerId=None):
        if playerId is None:
            playerId = 0
        print 4*playerId*"  " + message

    def clearScreen(self):
        print "\n" * 100

    def outputOptions(self, options, playerId=None):
        if isinstance(options, list):
            d = { i+1: v for i, v in enumerate(options)}
        else:
            d = options

        for i in sorted(d.keys()):
            self.output("{}. {}".format(i, d[i]), playerId)

class ConsoleInput(object):
    def __init__(self):
        pass
    
    def input(self):
        return input()