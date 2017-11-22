from deck import Deck
from player import Player

class State(object):

    def __init__(self):
        self.dealer_up_card = None
        # for debugging
        self.dealer_bottom_card = None
        self.player_sum = None
        self.bet = None



