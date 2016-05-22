from deck import Deck
import unittest
from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose import with_setup
from collections import Counter
from copy import deepcopy


test_deck = Deck()
def setup_deck():
    pass
    
def teardown_deck():
    test_deck.collect()

def test_number_of_cards():
    assert_equal(len(test_deck.cards), 52)

def test_13_of_each_suit():
    suits = ['hearts', 'spades', 'clubs', 'diamonds']
    c = Counter([card['suit'] for card in test_deck.cards])
    for suit in suits:
        assert_equal(c[suit], 13)

def test_4_of_each_value():
    values = ['ace'] + map(str, range(2, 11)) + ['jack', 'queen', 'king']
    c = Counter([card['value'] for card in test_deck.cards])
    for value in values:
        assert_equal(c[value], 4)
    
def test_shuffle():
    cards_before = deepcopy(test_deck.cards)
    test_deck.shuffle()
    assert_not_equal(cards_before, test_deck.cards)

@with_setup(setup_deck, teardown_deck)
def test_collect():
    test_hand = test_deck.draw(5)
    test_deck.collect()
    assert_equal(len(test_deck.cards), 52)
    assert_equal(len(test_deck.cards_in_play), 0)
    
@with_setup(setup_deck, teardown_deck)
def test_draw_1():
    test_hand = test_deck.draw(1)

    assert_equal(len(test_hand), 1)
    assert_equal(len(test_deck.cards), 51)
    assert_equal(test_hand, test_deck.cards_in_play)
    
    

@with_setup(setup_deck, teardown_deck)
def test_draw_3():
    test_hand = test_deck.draw(3)

    assert_equal(len(test_hand), 3)
    assert_equal(len(test_deck.cards), 49)
    assert_equal(test_hand, test_deck.cards_in_play)
