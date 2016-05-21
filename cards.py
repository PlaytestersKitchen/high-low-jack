from collections import defaultdict

suits = ['hearts', 'spades', 'clubs', 'diamonds']
values = ['ace'] + map(str, range(2, 11)) + ['jack', 'queen', 'king']

# create a dictionary with the default game point values for each card value
game_point_values = defaultdict(int)
game_point_values['ace'] = 4
game_point_values['king'] = 3
game_point_values['queen'] = 2
game_point_values['jack'] = 1
game_point_values['10'] = 10

# creates a list of 52 card objects, each with suit, value, and game_points attributes
# cards = [
#     {
#           'name': 'ace of hearts'
#           'suit': 'hearts'
#           'value': 'ace'
#           'game_points': 4
#      },
#     {
#           'name': 'two of hearts'
#           'suit': 'hearts'
#           'value': 'two'
#           'game_points': 0
#      },
#      and so on 50 more times...
# ]
cards = []
for suit in suits:
    for value in values:
        cards.append({
                'name': '{0} of {1}'.format(value, suit)
                'suit': suit,
                'value': value,
                'game_points': game_point_values[value],
        })
