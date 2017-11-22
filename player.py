from deck import Deck

class Player(object):
    #A player has a hand and a name. Interacts with the deck

    def __init__(self, player_name):
        self.hand = []
        self.name = player_name
        self.points = 0
        self.money = 1000

    def draw(self, deck):
        #Draw a card from deck and tell the deck to remove its top card
        self.hand.append(deck.contents[0])
        deck.removeTopCard()

    def calculate_points(self):
        #Figures out how many points the player's hand is worth
        points = 0
        numberOfAces = 0

        for card in self.hand:
            temp = card.split()
            if temp[0].isdigit():
                points += int(temp[0])
            elif temp[0] == 'Ace':
                points += 11
                numberOfAces += 1
            else:
                points += 10

        while numberOfAces > 0 and points > 21:
            numberOfAces -= 1
            points -= 10

        return points

