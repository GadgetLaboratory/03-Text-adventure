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

#edit the below please and make the places ferial places
rooms = {
    'placeholder': {
        'name': 'a forbidden place'
        ,'north': 'glitch'
        ,'south': 'glitch'
        ,'east': 'glitch'
        ,'west': 'glitch'
        ,'contents': []
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'A2': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'A3': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'A4': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'A5': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'A6': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'A7': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'A8': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'A9': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
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
    'B8': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'B9': {
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
    'C8': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'C9': {
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
    'D8': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'D9': {
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
    'E8': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'E9': {
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
    'F8': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'F9': {
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
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'G8': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'G9': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'H1': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'H2': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'H5': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'H8': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'H9': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'I2': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'I3': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'I4': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'I5': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'I6': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'I7': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'I8': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    },
    'I9': {
        'name': ''
        ,'desc': 'The stone floors and walls are cold and damp.'
    }

    
}
inventory = []
directions = ['north', 'south', 'east', 'west']
current_room = rooms['empty']
combat = False

#here's the gaem
while combat == False:
    # so where are you?
    print()
    print("You're currently in the {}.".format(current_room['name']))

    current = "empty"
    action = input("What to do...? ").lower()
    if action[0:4] == 'take ':
        item = action[4:]
        for c in rooms[current]['contents']:
            if c == item:
                inventory.append(item)
                rooms[current]['contents'].remove(item)
    if action[0:4] == 'take ':
        if (action in directions and action not in rooms[current]):
            print("You can't go that way!")
    else:
        current = rooms[current][action]