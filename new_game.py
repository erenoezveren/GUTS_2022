import random
'''
    Love letter - implementation of the game
'''

class Game:
    def __init__(self, deck, player_N):
        self._deck = deck #array of cards in numbers, ie: [1, 1, 8] would mean Guard, Guard, Princess left in the deck
        self.turn = 0
        self.current_player = 0

        players_left = player_N
        self._active = players_left> 1 and self._cards_left() > 0

        #set up players
        players = []
        for i in range(player_N):
            players.append(id=i, card=self.draw_card())


    def play(self, player, move):
        if player == self.current_player:
            self.current_player += 1

    
    def draw_card(self):
    #return card at the top of the deck (if game is running (This should probably be checked somewhere else for like every turn though right?))
        if(self._active):
            if len(self.deck) > 1:
                new_card = self._deck[0]
                self._deck = self._deck[1:]
            else:
                new_card = self._deck[0]
                self._deck = []

            return new_card

    def turn(self):
    #return the current turn number
        return self.turn
    
    def current_player(self):
    #return the player whose turn it currently is?
        return self.current_player
    
    def winner(self):
    #return the winner of the game (if there is one) REQUIRES: DECK EMPTY
        highest = 0
        for player in self._players:
            pass

    
    def cards_left(self):
    #return the number of the cards left in the deck
        return len(self._deck)
    
    
    """left to add:
        event for each specific card
        function that checks if a move is valid?
        function that shuffles/resets the deck
        
       """

