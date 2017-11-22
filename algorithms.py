import numpy as np
import random
from player import Player
from deck import Deck
from game import Game

def Q_Learning(reward, observed_keys, counter_state, counter_state_action, value_function):
    if reward is not None:
        # update over all keys
        for i in range(len(observed_keys)):
            # update counts
            counter_state[observed_keys[i][:-1]] += 1
            counter_state_action[observed_keys[i]] += 1

            # update value function
            alpha = 1.0 / counter_state_action[observed_keys1[i]]
            old = value_function[observed_keys1[i]]
            if i < len(observed_keys1) - 1:
                hit = observed_keys1[i+1][:2] + (1, )
                stick = observed_keys1[i+1][:2] + (0, )
                maxvalue = max(value_function[hit],value_function[stick])
                new = 0.8 * maxvalue
            else:
                new = 0
            value_function[observed_keys1[i]] = (1-alpha) * old + alpha * (reward1 + new)