'''
Implementation of Cards

Static class

Cards or game can be renamed later to better fit the office theme:
i.e., Boss instead of the Princess and Recommendation letter instead of the Love letter?

'''
import numpy as np

class Card():
    names = ['', 'Guard', 'Priest', 'Baron', 'Handmaid', 'Prince', 'King', 'Countess', 'Princess']    
    actions = ['None', 
                'Guess a player\'s hand',
                'Look at another player\'s hand',
                'Compare your card with another player\'s card. The lower hand is eliminated.',
                'Gain protection from opponents cards for one turn',
                'Choose a player. That player discards their hand',
                'Swap your hand with another player',
                'Discard if caught with Prince or King',
                'Concede the round if discarded']
    frequencies = [ 0,
                    5,  # Guard 
                    2,  # Priest
                    2,  # Baron
                    2,  # Handmaid
                    2,  # Prince
                    1,  # King
                    1,  # Countess
                    1,] # Princess
    
    self = [4, 7, 8]
    other = [1, 2, 3, 6]

    #Prince can be played on both self or other players

    #Initializes the deck at the beginning of the game
    def shuffle_deck():
        deck_1 = []
        for card, freq in enumerate(card.frequencies):
            deck_1.append([card] * freq)
        deck_2 = np.array(deck_1)
        np.random.shuffle(deck_2)
        return deck_2






