### Not yet finished!!
### If you're seeing this message and you're grading this work, please have mercy yet. ;w;
### I just need a bit longer; this'll be done soon.

import sys, logging, json, random

######################### == CLASSES == #########################

class Skill:
    """
    Creates skill objects that can be called upon in battle for the cost of EP.

    flavor, effect = str | power = int | tooltips = list of strings
    """
    def __init__(self, flavor, power, effect, tooltips):
        self.flavor = flavor
        self.power = power
        self.effect = effect
        self.tooltips = tooltips

class Item: 
    """
    Creates item objects that can be used from the inventory at any time, whether in or out of battle.

    flavor, effect, isEquip (see comment) = str | uses = int
    """
    def __init__(self, flavor, effect, uses, isEquip):
        self.flavor = flavor
        self.effect = effect
        self.uses = uses      #if not meant to break, input 999
        self.isEquip = isEquip #designate 'weapon', 'armor', 'charm', or None, and go on:
                                #set equip function; if equipped to [space], apply stat boosts
    def use(self):
        self.uses -= 1
        print(self.effect)
        if self.uses == 0:
            print("This item's run its course.")
            del self
    
    def discard(self):
        print("Won't be needing this.")
            del self



class Character:
    """
    Creates characters in the game.  Most of these characters can be fought, but are unnecessary to.

    name, about, quote = str | hp, ep, atk, vit, agi = int | skills = list
    """
    def __init__(self, name, about, hp, ep, atk, vit, agi, quote, skills):
        self.name = name
        self.about = about
        self.hp = hp
        self.ep = ep
        self.atk = atk
        self.vit = vit
        self.agi = agi
        self.quote = quote
        self.skills = skills
    ######################## == COMMANDS == #########################
    #actions left: skill setup
    def attack(self, target):
        damage = round(self.atk * random.uniform(.75, 1.25)) - round(target.vit * random.uniform(.8, 1.2))
        if damage < 1: 
            damage = 1
        print("{} damage to {}!").format(damage, target.name)
        target.hp -= damage

    def buff(self, stat, amount):
        self.stat += amount

    def debuff(self, stat, amount):
        self.stat -= amount
    
    def block(self):
        print("{} takes a guard stance!").format(self.name)
        blockTurn = turnNumber
        self.vit * 2
        if turnNumber != turnNumber or combat == False:
            return self.vit / 2

    def look(self, enemy): 
        print(enemy.about)

    def run(self, enemy):
        print("{} tried to get away...").format(self.name)
        chance = float(self.agi / enemy.agi)
        if random.random < chance:
            print("...and did!")
            combat = False
        else: 
            print("...but couldn't!")

######################### == SKILLS == #########################

doubleStrike = Skill()

flameStrike = Skill()

recover = Skill()

temper = Skill()

tense = Skill()

frenzy = Skill()

ironShatteringStrike = Skill()

sidestep = Skill()

lightBlast = Skill()

darkCall = Skill()

pierce = Skill()

berserkRush = Skill()

berserkInferno = Skill()

######################### == ITEMS == ##########################

#items:
# berry, blueshot, pinkshot, apple, malachite, candy, book, dagger, ruby, pendant (from Forrest)
#  moonstone (you win the game if you have this, right)

berry = Item()

blueShot = Item()

pinkShot = Item()

apple = Item()

malachite = Item()

candy = Item()

book = Item()

dagger = Item()

ruby = Item()

pendant = Item()

moonStone = Item()

####################### == CHARACTERS == #######################

# player, pandorah, rochelle, forrest, garnet, bianca,
#  wildcat, crystal, ghost, golem, wight, ancestor, recruit, vergil

laurent = Character("Laurent 'Gadgy' Turntide",
    """A tough and playful Ferial that was turned just as you were one day.  He looks a lot
    more intimidating than he acts, so he's usually just a huggable, coy doggo.
    Unless you anger him, anyway.""",
    35, 30,
    12, 10, 6,
    "If that's how you're gonna be...",
    [temper, tense, doubleStrike])

pandorah = Character("Pandorah Allyson Turntide",
    """An adorable and huggable mother who spent a good deal of her life bettering herself
    in the ways of battle and now passes some of that knowledge onto her children.""",
    36, 42,
    10, 8, 12,
    "No problem here!"
    [recover, sidestep, flameStrike])

rochelle = Character("Rochelle Allyson Turntide",
    """A rough and tough ferial, one daughter of Laurent and Pandorah.  She takes improvement
    incredibly seriously, as if she were dedicated in mind, heart, and body, to an ultimate goal.""",
    60, 48,
    16, 16, 16,
    "You're really trying to pick a fight with me?"
    [doubleStrike, flameStrike, sidestep, ironShatteringStrike])

forrest = Character("Forrest Malachite Turntide",
    """A young Turntide boy, one of Laurent and Pandorah's twin sons.  He looks up to his big
    sister Rochelle as a fighter and wants to be able to fight alongside her one day.
    But most of the time he just prefers to relax anyway, so he's got a ways to go.""",
    25, 22,
    9, 7, 11,
    "--W-Wait, huh?!"
    [sidestep])

garnet = Character("Isabelle 'Garnet' Harding",
    """Someone who fights alongside the rebel leader, Rochelle, as part of her squadron.
    She takes her job very seriously, but depends on her leader a little bit too much.""",
    40, 48,
    10, 6, 14,
    "Moron!  I'll skewer you right here!!",
    [pierce, temper, sidestep])

bianca = Character("Bianca Maye",
    """A motherly cowgirl that's decided to take time helping in the Ferial village, since
    times have been tougher than usual.  There's a wonderful soul hidden away behind that
    significant bust of hers. *snrk*""",
    65, 25,
    10, 16, 4,
    "Goodness, and here I am tryin' to look after these poor folk..."
    [tense, recover])

wildcat = Character("a stray wildcat",
    """A beast that strays around, looking for minor prey.  It seems it's decided that's you.
    If you can endure a round or two, hit it with your toughest attack and it'll be pulverized.""",
    15, 10,
    6, 4, 8,
    "*It locks sights with you, and then pounces!*",
    [frenzy, sidestep])

crystal = Character("a formation of some magic crystals",
    """Some sort of magical force is keeping it together... seems like it's asking to be broken, to me.
    Its defenses are somewhat high for a random creature.  Try breaking through them.""",
    30, 10,
    6, 9, 6, #nice
    "*It's trying to find a signal... and it detects you, as the closest thing!*",
    [lightBlast, tense])

ghost = Character("a departed spirit",
    """Seems like this spirit didn't want to head up to Sanctuary.  Make it regret sticking around.
    Attacking something incorporeal is usually a bad idea.  Just hit it *enough*, unless you can burn it.""",
    3, 40,
    8, 25, 7,
    "Help...",
    [lightBlast, darkCall])

golem = Character("a golem put together by some spiritual force",
    """This golem is protecting the temple for a reason; simple precautionary measures, you know.
    If you want to reach the Moonstone, you'll probably have to take it out.
    It's a very bulky attacker.  Try breaking through its defenses, if you can.""",
    40, 20,
    12, 16, 7,
    "*Now fully activated, it detects you as an intruder and attacks!*",
    [recover, doubleStrike])

wight = Character("a greater, skeletal spirit bound to this world by dark means",
    """A wight that sprang back into the action of life after you came through.
    It doesn't appreciate intruders...
    Somewhat of a glass cannon.  You should try to kill it before it kills you, and
    if you're reading this, you're not on the best start.""",
    35, 36,
    16, 9, 12,
    "Begone...", 
    [darkCall, temper, pierce, flameStrike])

ancestor = Character("a ghostly Ferial that should be long since dead",
    """Some sort of long-forgotten Ferial guardian.  Maybe this being had a part in guarding
    the Moonstone however many generations ago?  Never mind that -- they'll tear you apart.
    They're incredibly strong all around, but Ferials are all weak to magic in some way.""",
    38, 30,
    15, 18, 15,
    "If you dare to step into this temple, you will prove that you are worthy."
    [sidestep, recover, tense])

recruit = Character("a recruit of the Human Salvation Brigade",
    """A raggedy soldier recruited by the man you've heard of as Vergil.  His sort doesn't
    like Ferials because of the accidents they've caused.  They want to make you pay in blood.
    Apart from Vergil himself, you probably won't find a tougher opponent -- this one may
    be worth using your items for.  He'll run out of energy eventually.""",
    50, 32,
    16, 12, 18,
    "Ferial scum.  You'll not interfere with our boss's plan if I have anything to say about it!",
    [temper, pierce, lightBlast, recover])

vergil = Character("Vergil Rainer Caldwell",
    """The general of the Human Salvation Brigade.  His ripped figure and his wild, flowing hair
    and his dark skin all come together to convey the absolute might of him.  What's more, you can
    feel a burning aura come from him, as if he was on fire.  He's commanding this brigade for
    a reason, you can tell that now more than ever.
    Conserve your resources until you've done enough damage to him.  When you have him on the ropes,
    he'll go berserk.  He is NOT someone that would ever lose to someone he considers below him.""",
    150, 80,
    24, 21, 16,
    "If you won't listen... then you'll DIE like the rest of these mutts!!",
    [doubleStrike, flameStrike, frenzy, temper]
    )

######################### == ROOMS == ##########################

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
        'people': [garnet],
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
        'contents': [moonStone],
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
        'contents': [blueShot, pinkShot],
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
        'desc': """Religious practices seem to be (or were) conducted in this temple, you figure.
        I mean, it makes sense -- it IS a temple.  But here is different, for some reason.
        The paintings on these walls depict battles under some divine figure.  That's
        one way to show faith, you suppose.
        ...Also, there's some fit guy in a black jacket here and no shirt beneath.  When he sees you,
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
        'desc': """Welcome to the Turntide House!
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
        'people': [rochelle],
        'west': 'F4',
    },
    'G6': {
        'name': 'in the Warehouse',
        'desc': """The air is warm and dry in here.  And the amount of supplies is high as hell.
        It's sorted to a degree, but there's so much of a surplus here that it's kind of all over
        the place.  Nobody's in right now, either. Surely they wouldn't notice if you borrowed
        something for just long enough to get your whole turning-back-to-normal thing over with.
        There's a stray dagger, malachite, candy, and a book, for example.""",
        'contents': [dagger, malachite, candy, book],
        'people': [],
        'west': 'F6',
    },
}

####################### == VARIABLES == ########################

game = "start"
inventory = []
# define clause: inventory can only contain 5 items; equipment can be pushed into the designations below
weapon = []
armor = []
charm = []
directions = ['north', 'south', 'east', 'west']
current_room = rooms['C5']
enemy = None
combat = False
turnNumber = 0
templeSwitch1 = False
templeSwitch2 = False
kills = 0
atrPoints = 10
sklPoints = 0

#################### == MISC. FUNCTIONS == #####################

#deciding when random encounters will happen, in certain areas
def randomEncounter(pChance, enemyA):
    enemyChance = random.randint(0, 100)
    if enemyChance <= pChance:
        combat = True
        enemy = enemyA
        print(str("You've been discovered by {}.".format(current_room['enemy'])))
        print(current_room['enemy']['quote'])
    else:
        pass

#if you just want to fight somebody
def startEncounter(chara):
    combat = True
    enemy = chara
    print(current_room[chara]['quote'])
    return str("{} will be your opponent!".format(chara.name))

def showHealth(chara):
    print("{} has {} health remaining.").format(chara.name, chara.hp)

#misc. story functions
# need: when rochelle grants access to the temple (garnet lets you through)

#when both switches in the temple have been activated
def unlockMoonstone():
    rooms['B2'].update({'east':'C2'})
    print("""
    As the other switch is clicked into an active position, you hear gates rumbling near the entrance.  It
    seems you might have finally unlocked the Moonst--
    "HEY, THANKS FOR DOING ALL THE WORK!"
    That's a loud yell you hear all of a sudden, snapping oyu out of your thoughts.  As you look around the
    corner, there's someone with wild hair and a long, flowing jacket that disappears.  He's heading towards
    the Moonstone. Is that the guy you were warned about?!  Damn, you've got to catch him!
    """)

def flipSwitchA():
    templeSwitch1 = True
    if templeSwitch1 and templeSwitch2 == True:
        unlockMoonstone()

def flipSwitchB():
    templeSwitch2 = True
    if templeSwitch1 and templeSwitch2 == True:
        unlockMoonstone()

def berserk():
    print("""
    "Hah... hahahahah... you think I'm gonna lose to some random mutt like you?"
    "Some INSIGNIFICANT, SUBHUMAN WASTE OF SPACE?!  LIKE HELL I'LL EVER BE HUMILIATED LIKE THAT!!"
    "You're a fuckin' strong mutt to get me pissed off, I'll give you that much!"
    "BUT THIS IS WHERE YOUR EFFORTS STOP COLD!"
    "BURN INTO NOTHING!!"

    Vergil's body is taken by a sudden, bright-yellow aura of flame as his eyes shine and his hair
    almost seems to ignite.  It's almost like the wind is blowing his attire from inside this temple.
    He wants nothing more than to destroy you, now.
    """)
    vergil.hp = 120
    vergil.ep = 80
    vergil.skills.remove[flameStrike, frenzy]
    vergil.skills.append[berserkRush, berserkInferno]

def killCharacter(chara):
    current_room['people'].remove(chara)
    current_room['enemy'].remove(chara)
    #killer queen has touched this character

################### == STARTING SEQUENCE == ####################

#how do we wake up? (and allocate our atrPoints?)
#define the player as an entity here; store their responses and apply them to an instance of Character after all prompts are answered
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
player = Character(str(playerName),
    """You don't remember how you gothere.  All you remember is that you were attacked by
    another Ferial and woke up as one in the infirmary.  Now, though, you have an opportunity
    to turn back.  Will you succeed in taking this path?""",
    playerHealth, playerEnergy, playerAttack, playerVitality, playerAgility
    "", 
    [])

######################## == LET'S GO == ########################

game = "not win"

#here's the gaem
while game == "not win":
    while combat == False:
        if current_room in [rooms['A7'], rooms['B1'], rooms['B2'], rooms['B3'],
        rooms['B7'], rooms['C7'], rooms['D2'], rooms['D3'], [rooms['D7']]]:
            randomEncounter(20)
            if combat == True:
                break
        print()
        print("You're currently {}.".format(current_room['name']))
        if atrPoints > 0:
            print("You have {} power points to allocate. (use with 'increase [stat]')").format(atrPoints)

        current_room = "empty"
        action = input("What to do...? ").lower()
        #actions: look, yell, take, equip, go
        if "look" or "look around" in action:
            print(rooms[current_room]['desc'])
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
        #actions: attack, block, skill, item, run (prompt)
        #have a function to return list of sub-options that are matched to numbers
        #have a way to log turns, health, energy, skills
        #look should show health and print the enemy's flavor text
        if player.hp <= 0:
            game = "over"
        if enemy.hp <= 0:
            print(You made it through the fight!)
            enemy = None

while game == "over":
    #dead