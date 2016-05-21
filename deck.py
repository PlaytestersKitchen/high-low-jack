import cards
import random

class Deck:
    def __init__(self):
        self.cards = cards.cards
        self.cards_in_play = []
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def draw(self, amount):
        drawn_cards = []
        for i in range(amount):
            card = self.cards.pop()
            self.cards_in_play.append(card)
            drawn_cards.append(card)
        return drawn_cards