import gym
from gym import spaces
from gym.utils import seeding
import numpy as np

def cmp(a, b):
    return int((a > b)) - int((a < b))

# 1 = Ace, 2-10 = Number cards, Jack/Queen/King = 10
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw_card(np_random):
    return np_random.choice(deck)


def draw_hand(np_random):
    return [draw_card(np_random), draw_card(np_random)]





def usable_ace(hand):  # Does this hand have a usable ace?
  return 1 in hand and sum(hand) + 10 <= 21

class Player:
    def sum_hand(self):  # Return current hand total
        if usable_ace(self.mycards):
                self.sum=sum(self.mycards)+10
        self.sum=sum(self.mycards)

    def __init__(self,identity):
        self.mycards=[]
        self.identity=identity
        self.sum=0
        self.mycards.append(np.random.choice(deck))
        if(identity==1):
            self.mycards.append(np.random.choice(deck))
        self.draw=True
        self.sum_hand()



    def action(self):
        i=input("draw card or stop ")
        if(i=='draw'):
            self.mycards.append(draw_card(np.random))
            for i in self.mycards:
                print (i)
            self.sum_hand()
            print ("the sum is %d" %(self.sum))
        else:
            print ("stop")
            self.draw=False

    def play(self):
        for i in self.mycards:
            print (i)
        print ("the sum is %d" %(self.sum))
        while(self.sum<21 and self.draw):
            self.action()
            self.sum_hand()



while(True):
    customer=Player(1)
    dealer=Player(0)
    print ("new game")
    print ("customer plays")
    customer.play()
    print ("end")
    print ("dealer plays")
    dealer.play()
    if(customer.sum>21):
        print ("dealer win")
    elif dealer.sum>21 or customer.sum>dealer.sum:
        print ("customer win")
    condition=input("continue or not (y/n)")
    if(condition=='n'):
        break
