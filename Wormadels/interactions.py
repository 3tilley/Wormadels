
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

        self.output.output("Player {} please {} a card".format(player.name, verb))

        self.output.outputOptions(gameChars)

        pick = self.input.input()

        while pick not in gameChars.keys():
            self.output.output("Naughty, that's not a valid choice. Try again.")
            pick = self.input.input()

        self.output.output("You chose {}".format(gameChars[pick]))
        
        if isPick:
            player.characters.append(gameChars[pick])

        del gameChars[pick]

        return pick

    def takeCardsOrGold(self, player, deck):
        self.output.outputOptions(["Take gold", "Take cards"])
        inp = self.input.input()
        if int(inp)==1:
            player.gold += 2
        elif int(inp)==2:
            cards = deck.drawCards(2)
            c, d = self.discardAndTakeCards(cards, 1)
            deck.returnCards(d)
            player.districts.append(c)

    def performCharacterEffect(self, player, character, deck):
        pass

    def build(self, player, character, endDistricts=8):
        self.output.outputOptions(player.districts)
        buildIndex = self.input.input()
        dist = player.districts.pop(buildIndex)
        player.playedDistricts.append(dist)
        if len(player.playedDistricts)==endDistricts:
            self.eventQueue("Game end triggered")

    def discardAndTakeCards(self, cards, numberToDiscard):
        self.output.output("Discard {} cards".format(numberToDiscard))
        discards = []
        for i in range(numberToDiscard):
            self.output.outputOptions(cards)
            inp = self.input.input()
            # TODO put error checking here
            d = cards.pop(inp-1)
            discards.append(d)

        return(cards, discards)

class ScreenPrinter(object):
    def __init__(self):
        pass

    def output(self, message):
        print message

    def clearScreen(self):
        print "\n" * 100

    def outputOptions(self, options):
        if isinstance(options, list):
            d = { i+1: v for i, v in enumerate(options)}
        else:
            d = options

        for i in sorted(d.keys()):
            self.output("{}. {}".format(i, d[i]))

class ConsoleInput(object):
    def __init__(self):
        pass
    
    def input(self):
        return input()