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
# player, laurent, pandorah, rochelle, forrest, garnet, bianca,
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
        'people': [],
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
        'people': [garnet]
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
        'people': [],
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
        'people': [],
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
        'people': [],
        'north': 'A4',
        'south': 'A6',
    },
    'A6': {
        'name': 'near the big field (west)',
        'desc': """Looking around, the road to some stony temple is just up to the north.
        The big field is to the south, where a lot of creatures seem to roam.""",
        'contents': [],
        'people': [],
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
        'people': [],
        'enemy': [wildcat],
        'north': 'A6',
        'east': 'B7',
    },
    'B1': {
        'name': 'in the Moonstone Temple (NW)',
        'desc': """As you enter this portion of the temple, you can hear sounds from elsewhere within.
        They resemble the sounds of battle.  Someone else is here, and you might just know who.""",
        'contents': [],
        'people': [],
        'enemy': [ghost],
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
        'people': [],
        'enemy': [ghost],
        'north': 'B1',
        'south': 'B3',
    },
    'B3': {
        'name': 'in the Moonstone Temple (SW)',
        'desc': """Quiet sounds are audible in this worn corner of the temple.
        Whispers, calling out to you... imploring for your assistance.
        There's something jutting out to the east.""",
        'contents': [],
        'people': [],
        'enemy': [ghost],
        'north': 'B2',
        'east': 'C3',
    },
    'B6': {
        'name': 'near the big field (center-west)',
        'desc': """Looking around, the infirmary in which you woke up is just a short way east.
        The big field is to the south, where a lot of creatures seem to roam.""",
        'contents': [],
        'people': [],
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
        'people': [],
        'enemy': [crystal],
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
        'people': [],
        'enemy': [golem],
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
        'people': [vergil],
        'enemy': [vergil],
        'west': 'B2',
    },
    'C3': {
        'name': 'in the Moonstone Temple (S)',
        'desc': """As you come to the southern wall, something peculiar catches your eye.
        There's a golem here that's been etched into and seems entirely defunct.
        Further, there's a lever within the wall, probably to trigger some sort of mechanism.
        You wonder if this will open the gate.  Probably!  It's worth a shot, right?""",
        'contents': [],
        'people': [],
        'enemy': [golem],
        'west': 'B3',
        'east': 'D3',
    },
    'C5': {
        'name': 'in the infirmary',
        'desc': """Looking around the infirmary, you can tell that it's very well-kept.  It makes sense,
        given how people are brought here for medical care.  It wouldn't do for it to be horrible.
        Bianca, the cowgirl who tended to you, is still here, supervising and taking care of others as well.
        Somebody left a couple of shots around here, one blue and one pink.  But is it really wise
        to be taking random medical supplies?
        Well, they must not be super-dangerous if they were forgotten about...""",
        'contents': [blueshot, pinkshot],
        'people': [bianca],
        'south': 'C6',
    },
    'C6': {
        'name': 'near the big field (center-east)',
        'desc': """You're just in front of the infirmary you woke up in -- that place is just north of here.
        The big field is to the south, where a lot of creatures seem to roam.""",
        'contents': [],
        'people': [],
        'south': 'C7',
        'west': 'B6',
        'east': 'D6',
    },
    'C7': {
        'name': 'in the big field (center-east)',
        'desc': """You're in a vast field.  Creatures might pop up to say hello, here...
        though the welcomings they give you probably won't be gentle.""",
        'contents': [apple, apple, apple, apple],
        'people': [],
        'enemy': [wildcat],
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
        'people': [],
        'enemy': [recruit],
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
        'people': [],
        'enemy': [ancestor],
        'north': 'D1',
        'south': 'D3',
    },
    'D3': {
        'name': 'in the Moonstone Temple (SE)',
        'desc': """There are bodies here -- potentially those that entered this place simply for kicks,
        or on an objective to steal the Moonstone.  Given what you've seen so far in this place, it
        probably wouldn't surprise you if one of them jumped up and tried to make you join them.""",
        'contents': [],
        'enemy': [wight],
        'north': 'D2',
        'west': 'C3',
    },
    'D6': {
        'name': 'near the big field (east)',
        'desc': """Looking around, the infirmary in which you woke up is just a short way west.
        The big field is to the south, where a lot of creatures seem to roam.""",
        'contents': [],
        'people': [],
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
        'people': [forrest],
        'north': 'C6',
        'east': 'D7',
    },
    'E2': {
        'name': 'on the main street (north)',
        'desc': """The main street of the Ferial village.  Here, you can see several Ferials just
        strolling about, going on their day.  Their culture doesn't really seem too different from
        human culture, when you look at it.  It's like its own world parallel to the normal world.
        ...Sadly, you've heard that it isn't always quite that peaceful.
        Coming up on the east is the Turntide household.""",
        'contents': [],
        'people': [],
        'south': 'E3',
        'east': 'F2'
    },
    'E3': {
        'name': 'on the main street (center-north)',
        'desc': """The main street of the Ferial village.  Here, you can see several Ferials just
        strolling about, going on their day.  Their culture doesn't really seem too different from
        human culture, when you look at it.  It's like its own world parallel to the normal world.
        ...Sadly, you've heard that it isn't always quite that peaceful.""",
        'contents': [],
        'people': [],
        'north': 'E2',
        'south': 'E4',
    },
    'E4': {
        'name': 'on the main street (center)',
        'desc': """The main street of the Ferial village.  Here, you can see several Ferials just
        strolling about, going on their day.  Their culture doesn't really seem too different from
        human culture, when you look at it.  It's like its own world parallel to the normal world.
        ...Sadly, you've heard that it isn't always quite that peaceful.
        Coming up on the east is the training dojo that the Turntides founded.""",
        'contents': [],
        'people': [],
        'north': 'E3',
        'south': 'E5',
        'east': 'F4',
    },
    'E5': {
        'name': 'on the main street (center-south)',
        'desc': """The main street of the Ferial village.  Here, you can see several Ferials just
        strolling about, going on their day.  Their culture doesn't really seem too different from
        human culture, when you look at it.  It's like its own world parallel to the normal world.
        ...Sadly, you've heard that it isn't always quite that peaceful.""",
        'contents': [],
        'people': [],
        'north': 'E4',
        'south': 'E6',
    },
    'E6': {
        'name': 'on the main street (south)',
        'desc': """The main street of the Ferial village.  Here, you can see several Ferials just
        strolling about, going on their day.  Their culture doesn't really seem too different from
        human culture, when you look at it.  It's like its own world parallel to the normal world.
        ...Sadly, you've heard that it isn't always quite that peaceful.
        Coming up on the east is the supply warehouse, used for several different things.""",
        'contents': [],
        'people': [],
        'north': 'E5',
        'east': 'F6',
        'west': 'D6',
    },
    'F2': {
        'name': 'near the Turntide household',
        'desc': """Coming off of the main street, you're near the Turntide house.  From here, it seems
        like a decent enough place, although there's very little in the way of decoration.
        You wonder what the Turntides are like...""",
        'contents': [],
        'people': [],
        'east': 'G2',
        'west': 'E2',
    },
    'F4': {
        'name': 'near the Dojo',
        'desc': """Coming off of the main street, you're near the dojo.  They say the eldest child of the
        Turntide couple trains here constantly and is surpassing limits that no other Ferial had
        even come close to before.  She is incredibly dedicated...""",
        'contents': [],
        'people': [],
        'east': 'G4',
        'west': 'E4',
    },
    'F6': {
        'name': 'near the Warehouse',
        'desc': """Coming off of the main street, you're near the supply warehouse.  It's simple, wooden,
        and gets the job done.  It's also big.
        ...It also doesn't sound like there's anyone inside...""",
        'contents': [],
        'people': [],
        'east': 'G6',
        'west': 'E6',
    },
    'G2': {
        'name': 'in the Turntide House.',
        'desc': """Welcom to the Turntide House!
        There's such a warm atmosphere here.  Understandable, since, from what you've heard, there's a very
        big family that lives here.  Most of them seem to be away right now, though, which explains why
        your ears aren't being assaulted by clamor.  There's only the main two parents here:
        Laurent and Pandorah.""",
        'contents': [],
        'people': [laurent, pandorah],
        'west': 'F2',
    },
    'G4': {
        'name': 'in the Dojo.',
        'desc': """As you enter the dojo, you hear something break apart.  A very rough and fit female
        Ferial has just destroyed a training dummy with a loud punch of great magnitude.
        You've heard of her name.  Rochelle.  From what she looks like, maybe the rumors
        of her strength aren't entirely conjecture...""",
        'contents': [],
        'people': [rochelle]
        'west': 'F4',
    },
    'G6': {
        'name': 'in the Warehouse',
        'desc': """The air is warm and dry in here.  And the amount of supplies is high as hell.
        It's sorted to a degree, but there's so much of a surplus here that it's kind of all over
        the place.  Surely they wouldn't notice if you borrowed something for just long enough
        to get your whole turning-back-to-normal thing over with.
        There's a stray dagger, malachite, candy, and a book, for example.""",
        'contents': [dagger, malachite, candy, book],
        'people': [],
        'west': 'F6',
    },
}



game = "not win"
inventory = []
directions = ['north', 'south', 'east', 'west']
current_room = rooms['C5']
combat = False
ene = None
kills = 0
atrPoints = 10
sklPoints = 0

#deciding when random encounters will happen, in certain areas
def randomEncounter(pChance, enemy):
    enemyChance = random.randint(0, 100)
    if enemyChance <= pChance:
        combat = True
        print(str("You've been discovered by {}.".format(current_room['enemy'])))
        print(current_room['enemy'['quote'])
    else:
        pass

def startEncounter(chara):
    combat = True
    return str("{} will be your opponent!".format(chara.name))

def unlockMoonstone():
    rooms['B2'].update({'east':'C2'})

def killCharacter(chara):
    current_room['people'].remove(chara)
    current_room['enemy'].remove(chara)
    #killer queen has touched this character

#how do we wake up? (and allocate our atrPoints?)
print("""Your entire arm aches... buuut at least it feels better than it did.""")
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()

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
