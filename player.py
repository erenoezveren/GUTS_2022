"""
Implementation of player objects

"""

import numpy as np

class Player:
    def __init__(self, id, card):
        self.wins = 0
        self.card1 = card
        self.card2 = 0
        self._id = id

    def play_card1(self):
        temp_card = self.card1
        self.card1 = self.card2
        self.card2 = 0
        return temp_card  

    def play_card2(self):
        temp_card = self.card2
        self.card2 = 0
        return temp_card   
    