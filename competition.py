import gym
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys
import itertools

from collections import defaultdict
if "../" not in sys.path:
  sys.path.append("../") 
from blackjack import BlackjackEnv
import plot

env = BlackjackEnv()

import q_learning_epsilon_greedy
# import sarsa_epsilon_greedy
# import mc_epsilon_greedy
# import mc

reward_total_array = []
episodes_array = []

for episodes in range(10000, 100000, 10000):
    Q, stats, reward_total = q_learning_epsilon_greedy.train(env, episodes, test_episodes = 200)
    reward_total_array.append(reward_total)
    episodes_array.append(episodes / 1000)

plt.plot(episodes_array, reward_total_array, 'b')
plt.title('Reward vs episodes--Q Learning with epsilon greedy')
plt.xlabel('Episodes (k)')
plt.ylabel('Total reward')
plt.show()