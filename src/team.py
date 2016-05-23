class Team:
    def __init__(self, players):
        self.players = players
        self.points = 0
        
    def set_accepted_bid(self, accepted_bid):
        self.accepted_bid = accepted_bid
        
    def get_points_earned():
        pass

    def made_bid(bid, points_earned):
        return bid <= points_earned

    def game_points_earned(cards):
        return sum([card['game_points'] for card in cards])

class Player:
    def __init__(self, name, table_position):
        self.name = name
        self.bid = 0
        self.cards = []
        self.teammates = []
        self.table_position = table_position