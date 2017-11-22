from player import Player
from deck import Deck
from state import State
from random import *

class Game_Single:
    def __init__(self):
        self.end = False
        self.player = Player('player')
        self.dealer = Player('dealer')
        self.player_list = [self.player, self.dealer]
        self.deck = Deck()
        self.deck.shuffle()
        for player in self.player_list:
            player.draw(self.deck)
            player.draw(self.deck)
        self.state = State()
        self.dealer.dealer_up_card = self.dealer.hand[1]
        self.player.points = self.player.calculate_points()
        self.dealer.points = self.dealer.calculate_points()

    def step(game, dealer_sum, player_sum, action, reward, debug):
        """ 
        Returns the next game state and reward, given current state and actions.
        :param state: current state of the game
        :param action: 0 (stand), 1 (hit)
        :return: a tuple (next game state, rewards)
        """

        if debug:
            print('Before action, player sum: %d' %player_sum + ' Dealer sum: %d' %dealer_sum)

        if action == 1:
            game.player.draw(game.deck)
            player_sum = game.player.calculate_points()
            if player_sum > 21:
                reward = - 1
                if debug:
                    print('Lose due to bust.' + '\nPlayer hand: ', game.player.hand, '\nDealer hand: ', game.dealer.hand)
                game.end = True

        else:
            game.end = True
            # dealer is smaller than 17
            while dealer_sum < 17:
                game.dealer.draw(game.deck)
                dealer_sum = game.dealer.calculate_points()

            while dealer_sum <= 21:
                diff = player_sum - dealer_sum
                before_bust = 21 - dealer_sum
                
                if diff < 0:
                    reward = - 1
                    if debug:
                        print('Lose due to smaller than dealer.' + '\nPlayer hand: ', game.player.hand, '\nDealer hand: ', game.dealer.hand)
                    break
                elif diff > 0:
                    # deck is infinite so the probability is uniform
                    game.dealer.draw(game.deck)
                    dealer_sum = game.dealer.calculate_points()
                else:
                    # use monte carlo sampling to define dealer's action when meeting same sum
                    expect = before_bust / 13 * 1 - (1 - (before_bust / 13)) * 0.5
                    if (expect > 0):
                        game.dealer.draw(game.deck)
                        dealer_sum = game.dealer.calculate_points()
                    else:
                        reward = 0
                        if debug:
                            print('Same.' + '\nPlayer hand: ', game.player.hand, '\nDealer hand: ', game.dealer.hand)
                    break

            if (dealer_sum > 21):
                reward = 1
                if debug:
                    print('Win due to dealer bust.' + '\nPlayer hand: ', game.player.hand, '\nDealer hand: ', game.dealer.hand)

        return player_sum, reward

