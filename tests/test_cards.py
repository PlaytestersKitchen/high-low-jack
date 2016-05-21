from cards import cards
from nose.tools import assert_equal
from collections import Counter

def test_number_of_cards():
    assert_equal(len(cards), 52)
    
def test_13_of_each_suit():
    suits = ['hearts', 'spades', 'clubs', 'diamonds']
    hearts = [card for card in cards if card['suit'] == 'hearts']
    spades = [card for card in cards if card['suit'] == 'spades']
    clubs = [card for card in cards if card['suit'] == 'clubs']
    diamonds = [card for card in cards if card['suit'] == 'diamonds']
    
    assert_equal(len(hearts), 13)
    assert_equal(len(spades), 13)
    assert_equal(len(clubs), 13)
    assert_equal(len(diamonds), 13)
    
    # c = Counter([card['value'] for card in cards])
    # for suit in suits:
    #    assert_equal(c[suit], 4)
    
def test_4_of_each_value():
    values = ['ace'] + map(str, range(2, 11)) + ['jack', 'queen', 'king']
    
    pass       
