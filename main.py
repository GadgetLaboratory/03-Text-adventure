### Not yet finished!!
### If you're seeing this message and you're grading this work, please have mercy yet. ;w;
### I just need a bit longer; this'll be done soon.

import sys, logging, json, random

class Character: #define stats here: name, about, health, energy, strength, defense, agility
    def __init__(self, name, about, hp, mp, atk, vit, agi, quote):
        self.name = name
        self.about = about
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.vit = vit
        self.agi = agi
        self.quote = quote

#characters:
# player, gadgy, pandorah, rochelle, forrest, garnet,
#  wildcat, crystal, ghost, golem, wight, ancestor, recruit, vergil

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
        'enemy': [],
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
        'desc': """You're in a vast field.  Creatures might pop up to say hello, here...
        though the welcomings they give you probably won't be gentle.
        There's a plump-looking berry here if you want to be the risk-taker that grabs it.""",
        'contents': [berry],
        'enemy': wildcat,
        'north': 'A6',
        'east': 'B7',
    },
    'B1': {
        'name': 'in the Moonstone Temple (NW)',
        'desc': """As you enter this portion of the temple, you can hear sounds from elsewhere within.
        They resemble the sounds of battle.  Someone else is here, and you might just know who.""",
        'contents': [],
        'enemy': ghost,
        'south': 'B2',
        'east': 'C1',
    },
    'B2': {
        'name': 'in the Moonstone Temple (W)',
        'desc': """This is the entrance to the mystic Ferial temple.  The stone walls are lined with
        murals and runes, likely from centuries in the past.
        There's a sealed wall to the west of you, unless you've done away with it already.
        If you haven't... the Moonstone is probably there.  How to open the wall...?""",
        'contents': [],
        'enemy': ghost,
        'north': 'B1',
        'south': 'B3',
    },
    'B3': {
        'name': 'in the Moonstone Temple (SW)',
        'desc': """Quiet sounds are audible in this worn corner of the temple.
        Whispers, calling out to you... imploring for your assistance.
        There's something jutting out to the east.""",
        'contents': [],
        'enemy': ghost,
        'north': 'B2',
        'east': 'C3',
    },
    'B6': {
        'name': 'near the big field (center-west)',
        'desc': """Looking around, the infirmary in which you woke up is just a short way east.
        The big field is to the south, where a lot of creatures seem to roam.""",
        'contents': [],
        'south': 'B7',
        'west': 'A6',
        'east': 'C6',
    },
    'B7': {
        'name': 'in the big field (center-west)',
        'desc': """You're in a vast field.  Creatures might pop up to say hello, here...
        though the welcomings they give you probably won't be gentle.
        There's something glittering in the ground, here -- a ruby.""",
        'contents': [ruby],
        'enemy': crystal,
        'north': 'B6',
        'east': 'C7',
    },
    'C1': {
        'name': 'in the Moonstone Temple (N)',
        'desc': """As you come to the northern wall, something peculiar catches your eye.
        There's a depression against the wall, as if it's some sort of pressure switch.
        However, you don't think you have enough strength to depress it.
        ...That golem over there might.  But you won't be able to just strike up a conversation and ask it.""",
        'contents': [],
        'enemy': golem,
        'west': 'B1',
        'east': 'D1',
    },
    'C2': {
        'name': 'before the Moonstone',
        'desc': """It's right here.
        In this dark room, the only source of light is this Moonstone.
        An icy blue, aurora-like glow teems off of it.
        You've saved it from being taken by that maniac, that wild-haired freako that just wanted
        to end all these people.
        You couldn't care less about what the Ferials do, honestly.  You just want out of it.
        So what's stopping you?
        Reach out and touch it.""",
        'contents': [moonstone],
        'enemy': vergil,
        'west': 'B2',
    },
    'C3': {
        'name': 'in the Moonstone Temple (S)',
        'desc': """As you come to the southern wall, something peculiar catches your eye.
        There's a golem here that's been etched into and seems entirely defunct.
        Further, there's a lever within the wall, probably to trigger some sort of mechanism.
        You wonder if this will open the gate.  Probably!  It's worth a shot, right?""",
        'contents': [],
        'enemy': golem,
        'west': 'B3',
        'east': 'D3',
    },
    'C5': {
        'name': 'in the infirmary',
        'desc': """Looking around the infirmary, you can tell that it's very well-kept.  It makes sense,
        given how people are brought here for medical care.  It wouldn't do for it to be horrible.""",
    },
    'C6': {
        'name': 'near the big field (center-east)',
        'desc': """You're just in front of the infirmary you woke up in -- that place is just north of here.
        The big field is to the south, where a lot of creatures seem to roam.""",
        'contents': [],
        'south': 'C7',
        'west': 'B6',
        'east': 'D6',
    },
    'C7': {
        'name': 'in the big field (center-east)',
        'desc': """You're in a vast field.  Creatures might pop up to say hello, here...
        though the welcomings they give you probably won't be gentle.""",
        'contents': [apple, apple, apple, apple],
        'enemy': wildcat,
        'north': 'C6',
        'east': 'D7',
    },
    'D1': {
        'name': 'in the Moonstone Temple (NE)',
        'desc': """Religious practices seem to be conducted in this temple, you figure.
        I mean, it makes sense -- it IS a temple.  But here is different, for some reason.
        The paintings on these walls depict battles under some divine figure.  That's
        one way to show faith, you suppose.
        ...Also, there's some guy in a black jacket here and no shirt beneath.  When he sees you,
        he glares at you with palpable ferocity.""",
        'contents': [],
        'enemy': recruit,
        'south': 'D2',
        'west': 'C1',
    },
    'D2': {
        'name': 'in the Moonstone Temple (E)',
        'desc': """This portion of the temple is... grim.  You probably don't need to be here.
        Maybe that's just what you mind is telling you upon seeing several long-dead Ferial adults.
        They seem preserved incredibly well, though... in fact, you feel some sort of gaze from that way.
        Leave.""",
        'contents': [],
        'enemy': ancestor,
        'north': 'D1',
        'south': 'D3',
    },
    'D3': {
        'name': 'in the Moonstone Temple (SE)',
        'desc': """There are bodies here -- potentially those that entered this place simply for kicks,
        or on an objective to steal the Moonstone.  Given what you've seen so far in this place, it
        probably wouldn't surprise you if one of them jumped up and triedto make you join them.""",
        'contents': [],
        'enemy': wight,
        'north': 'D2',
        'west': 'C3',
    },
    'D6': {
        'name': 'near the big field (east)',
        'desc': """Looking around, the infirmary in which you woke up is just a short way west.
        The big field is to the south, where a lot of creatures seem to roam.""",
        'contents': [],
        'south': 'D7',
        'west': 'C6',
        'east': 'E6',
    },
    'D7': {
        'name': 'in the big field (east)',
        'desc': """You're in a vast field.  Creatures might pop up to say hello, here...
        though the welcomings they give you probably won't be gentle.
        Somebody's just chilling out here, a young Ferial boy.""",
        'contents': [],
        'people': forrest,
        'north': 'C6',
        'east': 'D7',
    },
    'E1': {
        'name': '',
        'desc': """""",
    },
    'E2': {
        'name': '',
        'desc': """""",
    },
    'E3': {
        'name': '',
        'desc': """""",
    },
    'E4': {
        'name': '',
        'desc': """""",
    },
    'E5': {
        'name': '',
        'desc': """""",
    },
    'E6': {
        'name': '',
        'desc': """""",
    },
    'F1': {
        'name': '',
        'desc': """""",
    },
    'F2': {
        'name': '',
        'desc': """""",
    },
    'F5': {
        'name': '',
        'desc': """""",
    },
    'G2': {
        'name': '',
        'desc': """""",
    },
    'G4': {
        'name': '',
        'desc': """""",
    },
    'G5': {
        'name': '',
        'desc': """""",
    },
}



game = "not win"
inventory = []
directions = ['north', 'south', 'east', 'west']
current_room = rooms['C5']
combat = False
kills = 0
atrPoints = 0
sklPoints = 0

#deciding when random encounters will happen, in certain areas
def randomEncounter(pChance, enemy):
    enemyChance = random.randint(0, 100)
    if enemyChance <= pChance:
        combat = True
        return str("You've been discovered by {}.".format(current_room['enemy']))
    else:
        pass

def unlockMoonstone():
    rooms['B2'].update({'east':'C2'})

#how do we wake up and allocate our atrPoints?


#here's the gaem
while game != "win":
    if current_room in [rooms[], rooms[], rooms[], rooms[], rooms[], rooms[], rooms[], rooms[] ]:
        randomEncounter(20)
    while combat == False:
        # so where are you?
        print()
        print("You're currently {}.".format(current_room['name']))
        if atrPoints > 0:
            print("You have {} power points to allocate.").format(atrPoints)

        current_room = "empty"
        action = input("What to do...? ").lower()
        if "look" or "look around" in action:
            print(rooms[current_room['desc']])
        elif "yell" in action:
            randomEncounter(100)
        elif "take" in action:
            item = action[4:]
            for c in rooms[current_room]['contents']:
                if c == item:
                    inventory.append(item)
                    rooms[current_room]['contents'].remove(item)
                    print("Got it.")
        elif 'go' in action:
            if (action in directions and action not in rooms[current_room]):
                print("You can't go that way!")
        else:
            current_room = rooms[current_room][action]
    while combat == True:
        #actions: attack, block, skill, item, run
