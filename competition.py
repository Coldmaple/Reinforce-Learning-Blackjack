import gym
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys

from collections import defaultdict
if "../" not in sys.path:
  sys.path.append("../") 
from blackjack import BlackjackEnv
import plot

env = BlackjackEnv()

import q_learning_epsilon_greedy
import sarsa_epsilon_greedy
import mc_epsilon_greedy

reward_avg_array1 = []
reward_avg_array2 = []
reward_avg_array3 = []

reward_avg_array_GLIE = []
reward_avg_array_FIX = []

episodes_array = []

def compare_three():

    for episodes in range(10000, 300000, 10000):
        Q1 = q_learning_epsilon_greedy.train(env, episodes)
        reward_total1 = q_learning_epsilon_greedy.test(100000, Q1)

        Q2 = sarsa_epsilon_greedy.train(env, episodes)
        reward_total2 = sarsa_epsilon_greedy.test(100000, Q2)

        Q3 = mc_epsilon_greedy.train(env, episodes)
        reward_total3 = mc_epsilon_greedy.test(100000, Q3)

        avg_reward1 = reward_total1 / 100000
        reward_avg_array1.append(avg_reward1)

        avg_reward2 = reward_total2 / 100000
        reward_avg_array2.append(avg_reward2)

        avg_reward3 = reward_total3 / 100000
        reward_avg_array3.append(avg_reward3)
        
        episodes_array.append(episodes / 1000)

    plt.plot(episodes_array, reward_avg_array1, 'b', label='q_learning')
    plt.plot(episodes_array, reward_avg_array2, 'r', label='sarsa')
    plt.plot(episodes_array, reward_avg_array3, 'g', label='mc_control')

    plt.title('Reward vs Episodes--Multiple algorithms')
    plt.xlabel('Episodes (k)')
    plt.ylabel('Average reward')
    plt.legend()
    plt.show()

def q_learning_compare_learning_rate():

    for episodes in range(1000, 50000, 1000):
        reward_total1 = q_learning_epsilon_greedy_GLIE.train(env, episodes)
        reward_total2 = q_learning_epsilon_greedy.train(env, episodes)

        avg_reward1 = reward_total1 / episodes
        reward_avg_array_GLIE.append(avg_reward1)

        avg_reward2 = reward_total2 / episodes
        reward_avg_array_FIX.append(avg_reward2)

        episodes_array.append(episodes / 1000)

    plt.plot(episodes_array, reward_avg_array_GLIE, 'b', label='GLIE')
    plt.plot(episodes_array, reward_avg_array_FIX, 'r', label='Learning rate=0.5')

    plt.title('Q Learning: How to set learning rate')
    plt.xlabel('Episodes (k)')
    plt.ylabel('Average reward')
    plt.legend()
    plt.show()

compare_three()
# q_learning_compare_learning_rate()

