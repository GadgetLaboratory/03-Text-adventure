class Character: #define stats here: name, about, health, energy, strength, defense, agility
    def __init__(self, name, about, hp, mp, str, vit, agi):

class Skill: #define flavor, power, effects, type, element
    def __init__(self, flavor, power, effect, type, element):

class Item: #define flavor, effects, uses
    def __init__(self, flavor, effect, uses):

class Equipment: #define flavor, effects, stats changes
    def __init__(self, flavor, effect, stat):

#edit the below please and make the places ferial places
rooms = {'empty': {'name': 'an empty room', 'east': 'bedroom', 'north': 'temple', 'contents': [],
        'text': 'The stone floors and walls are cold and damp.'},
    'temple': {'name': 'a small temple', 'east': 'torture', 'south': 'empty', 
        'text': 'This seems to be a place of worship and deep contemplation.', 
        'contents': ['bench', 'bench', 'bench', 'statue']},
    'torture': {'name': 'a torture chamber', 'west': 'temple', 'south': 'bedroom', 'contents': ['chains', 'thumbscrews'],
        'text': 'There is a rack and an iron maiden against the wall\naand some dark stains on the floor.'},
    'bedroom': {'name': 'a bedroom', 'north': 'torture', 'west': 'empty', 'contents': ['sheets', 'bed'],
        'text': 'This is clearly a bedroom, but no one has slept\nhere in a long time.'}}
inventory = []
directions = ['north', 'south', 'east', 'west']
current_room = rooms['empty']

#here's the gaem
while True:
    # so where are you?
    print()
    print('You are in {}.'.format(current_room['name']))