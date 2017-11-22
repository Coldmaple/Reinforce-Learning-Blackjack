from player import Player
from deck import Deck
from state import State
from random import *

class Game_Long:
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
        self.initial_bet = 5
        self.state = State()

    def step(game, dealer_sum, state, action, reward):
        """ 
        Returns the next game state and reward, given current state and actions.
        :param state: current state of the game
        :param action: 0 (stand), 1 (hit), 2 (double)
        :return: a tuple (next game state, rewards)
        """
        # state
        player_sum = state.player_sum()
        bet = state.bet()

        if action == 1:
            game.player.draw(game.deck)
            player_sum = game.player.calculate_points()
            if player_sum > 21:
                reward = - bet

        elif action == 2:
            bet *= 2
            game.player.draw(game.deck)
            player_sum = game.player.calculate_points()
            if player_sum > 21:
                reward = - bet

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
                    reward = - bet
                    break
                elif diff > 0:
                    # deck is infinite so the probability is uniform
                    expect = (before_bust - diff) / 52 * 1 - (52 - before_bust) / 52 * 0.5
                    if expect > 0:
                        game.dealer.draw(game.deck)
                        dealer_sum = game.dealer.calculate_points()
                    else:
                        reward = bet
                        break
                else:
                    # use monte carlo sampling to define dealer's action when meeting same sum
                    rand = random()
                    if (rand < before_bust / 52):
                        reward = - bet
                    else:
                        reward = 0
                    break

            if (dealer_sum > 21):
                reward = bet

        return state, reward

