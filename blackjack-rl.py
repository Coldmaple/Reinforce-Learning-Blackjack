from player import Player
from deck import Deck
from game_single import Game_Single
from game_long import Game_Long
import numpy as np
import random
from collections import defaultdict

def random_policy():
    return 0 if random.random() < 0.5 else 1

def epsilon_greedy(epsilon, value_function, player_sum, dealer_up_card):
    # exploration
    if random.random() < epsilon:
        return random_policy()
    # exploitation
    else:
        return complete_exploitation(value_function, player_sum, dealer_up_card)

def complete_exploitation(value_function, player_sum, dealer_up_card):
    value_HIT = value_function[(player_sum, dealer_up_card, 1)]
    value_STICK = value_function[(player_sum, dealer_up_card, 0)]

    if value_HIT > value_STICK:
        return 1
    elif value_STICK > value_HIT:
        return 0
    else:
        return random_policy()

def run_single_game(iteration_times, update_algorithm, Name, epsilon_value, policy, n_zero=100):

    # train_times: numbe of train times
    # algorithm
    # money: money one player starts the game
    # deck

    # state: (player_sum, dealer_up_card)
    # (player, dealer, action) key
    value_function = defaultdict(float)
    # (state) key
    counter_state = defaultdict(int)
    # (state, action) key
    counter_state_action = defaultdict(int)

    # number of wins
    wins = 0
    winrecord = []

    for j in range(iteration_times):
        # create a new random starting state
        game = Game_Single()
        player_sum = game.player.points
        dealer_sum = game.dealer.points
        dealer_up_card = game.dealer.hand[1]
        action = None
        reward = None
        # play a round
        observed_keys = []
        while not game.end:

            # find an action defined by the policy

            # epsilon
            if (epsilon_value == -1):
                # greedy in limit of infinite exploration
                epsilon = n_zero / float(n_zero + counter_state[(player_sum, dealer_up_card)])
            else:
                epsilon = epsilon_value

            if action is not 0 and reward is not -1:
                action = policy(epsilon, value_function, player_sum, dealer_up_card)
            else:
                action = 0
            # take a step

            if (player_sum, dealer_up_card, action) not in observed_keys and player_sum <= 21:
                observed_keys.append((player_sum, dealer_up_card, action))


            [player_sum, reward] = Game_Single.step(game, dealer_sum, player_sum, action, reward, debug = False)

        # we have reached an end of episode
        update_algorithm(reward, observed_keys, counter_state, counter_state_action, value_function)

        # test
        if (j > iteration_times * 0.99):
            if reward == 1:
                wins += 1

        winrecord.append(reward)

    print(Name + ' Wins: %.4f%%' % ((float(wins) / (iteration_times * 0.01)) * 100))

def Q_Learning(reward, observed_keys, counter_state, counter_state_action, value_function):
    if reward is not None:
        # update over all keys
        for i in range(len(observed_keys)):
            # update counts

            counter_state[observed_keys[i][:-1]] += 1
            counter_state_action[observed_keys[i]] += 1

            # update value function
            # alpha: learning rate
            # gamma: discount rate
            alpha = 1.0 / counter_state_action[observed_keys[i]]
            gamma = 0.8
            old = value_function[observed_keys[i]]

            if i < len(observed_keys) - 1:
                hit = observed_keys[i + 1][:2] + (1, )
                stick = observed_keys[i + 1][:2] + (0, )
                maxvalue = max(value_function[hit], value_function[stick])
                new = gamma * maxvalue
            else:
                new = 0
            value_function[observed_keys[i]] = (1 - alpha) * old + alpha * (reward + new)

# epsilon = 1: random policy
# winrecord_QL_random = run_single_game(1, Q_Learning, 'Q_Learning_random', 1, epsilon_greedy)
# winrecord_QL_epsilon = run_single_game(100000000, Q_Learning, 'Q_Learning_epsilon_greedy', 0.1, epsilon_greedy)
winrecord_QL_epsilon_GLIE = run_single_game(1000000, Q_Learning, 'Q_Learning_epsilon_greedy_GLIE', -1, epsilon_greedy)
# winrecord_QL_epsilon = run_single_game(10000000, Q_Learning, 'Q_Learning_complete_exploitation', 0.1, complete_exploitation)
