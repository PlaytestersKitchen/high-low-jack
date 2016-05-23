"""
A round is a series of tricks that lasts one deal.
There is one trump suit for the entire hand.
Bids happen at the start of each hand.
Points are given out and taken away after each hand.
At the end of a hand, if a team/player has gained the points needed to win, the match is over.
"""

class Round:
    def __init__(self, deck, teams, players, table_positions, first_dealer):
        self.trump_suit = ''
        self.deck = deck
        self.teams = teams
        self.players = players
        self.table_positions = table_positions
        self.dealer = first_dealer
        self.first_to_play = None
        self.accepted_bid = {}
        self.trump_suit = None
        
def collect_bids(self):
    pass

def game_points_earned(self, cards):
    return sum([card['game_points'] for card in cards])

def play_round(self):
    # while something:
        # hand.something()
        pass
    
def get_team_points(self):
    # return team_points

def get_points_earned(self, team_points):
    pass

def made_bid(self, bid, points_earned):
    return bid <= points_earned

def give_out_points(self):
    pass
