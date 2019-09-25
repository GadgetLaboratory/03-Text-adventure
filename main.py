### Not yet finished!!
### If you're seeing this message and you're grading this work, please have mercy yet. ;w;
### I just need a bit longer; this'll be done soon.

import sys, logging, json, random

class Character: #define stats here: name, about, health, energy, strength, defense, agility
    def __init__(self, name, about, hp, mp, str, vit, agi):

class Skill: #define flavor, power, effects, type, element
    def __init__(self, flavor, power, effect, type, element):

class Item: #define flavor, effects, uses
    def __init__(self, flavor, effect, uses):

class Equipment: #define flavor, effects, stats changes
    def __init__(self, flavor, effect, stat):

rooms = {
    'placeholder': {
        'name': 'in a forbidden place',
        'desc': """Do not look.  Leave.""",
        'contents': [],
        'north': 'glitch',
        'south': 'glitch',
        'east': 'glitch',
        'west': 'glitch',
    },
    'A2': {
        'name': 'near the temple gate',
        'desc': """The gateway leading to this rocky temple is sealed off by runes.
        Moonrunes, you're temped to call them.  You normally won't understand them.
        There's a bow-wielding Ferial standing guard here, it seems.""",
        'contents': [],
        'south': 'A3',
        'east': 'B2',
    },
    'A3': {
        'name': 'on the road to the temple (nearby)',
        'desc': """There isn't much to be made out about this road as its dust escapes from
        under your feet, but you can see a rocky temple in the distance.
        You'll get there soon, but if you don't know why you're going there,
        you probably don't have business there.""",
        'contents': [],
        'north': 'A2',
        'south': 'A4',
    },
    'A4': {
        'name': 'on the road to the temple',
        'desc': """There isn't much to be made out about this road as its dust escapes from
        under your feet, but you can see a rocky temple in the distance.
        You'll get there soon, but if you don't know why you're going there,
        you probably don't have business there.""",
        'contents': [],
        'north': 'A3',
        'south': 'A5',
    },
    'A5': {
        'name': 'on the road to the temple (distant)',
        'desc': """There isn't much to be made out about this road as its dust escapes from
        under your feet, but you can see a rocky temple in the distance.
        You'll get there soon, but if you don't know why you're going there,
        you probably don't have business there.""",
        'contents': [],
        'north': 'A4',
        'south': 'A6',
    },
    'A6': {
        'name': 'near the big field (west)',
        'desc': """Looking around, the road to some stony temple is just up to the north.
        The big field is to the south, where a lot of creatures seem to roam.""",
        'contents': [],
        'north': 'A5',
        'south': 'A7',
        'east': 'B6',
    },
    'A7': {
        'name': 'in the big field (west)',
        'desc': "You're in a vast field.  Creatures might pop up to say hello, here.",
        'contents': ['berry'],
        'north': 'A6',
        'east': 'B7',
    },
    'B1': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'B2': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'B3': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'B6': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'B7': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'C1': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'C2': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'C3': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'C5': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'C6': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'C7': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'D1': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'D2': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'D3': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'D6': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'D7': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'E2': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'E3': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'E4': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'E5': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'E6': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'E7': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'F1': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'F2': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'F5': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'G2': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'G4': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'G5': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'G7': {
        'name': '',
        'desc': 'The stone floors and walls are cold and damp.',
    } 
}



game = "not win"
inventory = []
directions = ['north', 'south', 'east', 'west']
current_room = rooms['C5']
combat = False

#deciding when random encounters will happen, in certain areas
def randomEncounter(pChance):
    

#here's the gaem
while game != "win":
    while combat == False:
        if current_room in [rooms[], rooms[], rooms[], rooms[], rooms[], rooms[], rooms[], rooms[],]:
            randomEncounter(20)
            if combat == True:
                break
        # so where are you?
        print()
        print("You're currently {}.".format(current_room['name']))

        current_room = "empty"
        action = input("What to do...? ").lower()
        if "look" or "look around" in action:
            print(rooms[current_room['desc']])
        elif "take" in action:
            item = action[4:]
            for c in rooms[current_room]['contents']:
                if c == item:
                    inventory.append(item)
                    rooms[current_room]['contents'].remove(item)
        elif action[0:4] == 'take ':
            if (action in directions and action not in rooms[current_room]):
                print("You can't go that way!")
        else:
            current_room = rooms[current_room][action]