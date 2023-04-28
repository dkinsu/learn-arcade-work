import random

class Room:
    def __init__(self, description, north, east, south, west, down, up):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.down = down
        self.up = up


class Item:
    def __init__(self, room_number, i_description, i_name):
        self.room_number = room_number
        self.i_description = i_description
        self.i_name = i_name


class PlayerClass:
    def __init__(self, player_description, class_name, class_hp, class_max_hp, class_attack, mana, max_mana, p_skill1, p_skill2, p_range,
                 p_skill1_desc, p_skill2_desc):
        self.player_description = player_description
        self.class_name = class_name
        self.class_hp = class_hp
        self.class_max_hp = class_max_hp
        self.class_attack = class_attack
        self.mana = mana
        self.max_mana = max_mana
        self.p_skill1 = p_skill1
        self.p_skill2 = p_skill2
        self.p_range = p_range
        self.p_skill1desc = p_skill1_desc
        self.p_skill2desc = p_skill2_desc


class Enemy:
    def __init__(self, monster_description, monster_name, monster_hp, monster_attack, m_skill1, m_skill1_dmg, m_skill2, m_skill2_dmg, m_range):
        self.monster_description = monster_description
        self.monster_name = monster_name
        self.monster_hp = monster_hp
        self.monster_attack = monster_attack
        self.m_skill1 = m_skill1
        self.m_skill1_dmg = m_skill1_dmg
        self.m_skill2 = m_skill2
        self.m_skill2_dmg = m_skill2_dmg
        self.m_range = m_range


# def player_classes(wizard, warrior, rogue):



# not in class!

def main():
    wizard = PlayerClass("A class that wields magic.\nPowerful ranged offense, weaker defense.",
                         "Wizard", 40, 40, 15, 60, 60, "Amplify", "Flare", 4,
                         'Increases your attack power. Costs 20 mana.',
                         'Cause a fiery explosion. High damage. Costs 20 mana.')

    warrior = PlayerClass("A class that fights with heavy close ranged weapons.\nClose-ranged offense, strong defense.",
                          "Warrior", 60, 60, 7, 30, 30, "Cleave", "Guard", 2,
                          'A long-reaching powerful swing. Costs 15 mana.',
                          'Heavily reduces incoming damage. Costs 10 mana.')

    rogue = PlayerClass("A class that fights with melee and ranged weapons.\nVersatile offense, middling defense.",
                        'Rogue', 50, 50, 10, 45, 45, "Lacerate", "Retreating Shot", 1,
                        'A devastating close-ranged attack. Poor range, heavy damage. Costs 15 mana.',
                        'Fire a shot with a bow before performing evasive maneuvers. Creates distance. Costs 25 mana.')

    cube = Enemy('A BIG CUBE.', 'THE CUBE', 50, 7, 'CUBIC CONTACT', 7, 'CUBE HYPER STRIKE', 14, 1)
    item_list = []
    room_list = []
    current_room = 0
    next_room = 0
    done = False

    key = Item(3, "A glass key. Brittle. It will definitely break after use. Get the key?", "key")
    item_list.append(key)

    elixir = Item(2, "A healing elixir. It will restore your HP, but can only be used once. Get the elixir?",
                  "elixir")
    item_list.append(elixir)

    mirror = Item(1, "A pocket mirror is lying on the ground. Get the mirror?", "mirror")
    item_list.append(mirror)

    charm = Item(-2, 'A charm of some sort is present. '
                     'Just standing near it makes you feel stronger. Get the charm?', 'charm')
    item_list.append(charm)

    dialogue_flag = Item(-2, 'flag for one-use dialogue line', 'd_flag')
    item_list.append(dialogue_flag)

    # Bedroom 2 - 0 - (description, north, east, south, west, down, up)
    room = Room("You are in the second bedroom, there is a door to the east.",
                None, 1, None, None, None, None)
    room_list.append(room)

    # South Hall - 1
    south_hall = Room("You are in the south hall.\nThere are doors to the north, east, and west.",
                      4, 2, None, 0, None, None)
    room_list.append(south_hall)

    # Dining Room - 2
    dining_room = Room("You are in the dining room.\nThere are doors to the west and north.",
                       5, None, None, 1, None, None)
    room_list.append(dining_room)

    # Bedroom 1 - 3
    bedroom1 = Room("You are in the first bedroom.\nThere is a door to the east.",
                    None, 4, None, None, None, None)
    room_list.append(bedroom1)

    # North Hall - 4
    north_hall = Room("You are in the north hall.\nThere are doors to the north, east, south, and west.",
                      6, 5, 1, 3, None, None)
    room_list.append(north_hall)

    # Kitchen - 5
    kitchen = Room("You are in the kitchen.\nThere are doors to the south and west.",
                   None, None, 2, 4, None, None)
    room_list.append(kitchen)

    # Balcony - 6
    balcony = Room("You are on the balcony.\nThere is a door to the south. You can also jump down.",
                   None, None, 4, None, 7, None)
    room_list.append(balcony)

    # Town road - 7
    town_road = Room('You are on the road to a nearby town. The town is to the north, '
                     'there is a forest to the east, and a lake to the west. '
                     'You can also climb back up to the balcony. ', 8, 9, None, 10, None, 6)
    room_list.append(town_road)
    # Town - 8
    town = Room('You have entered the town. The atmosphere is friendly. '
                'there is a road to the south. ', None, None, 7, None, None, None)
    room_list.append(town)
    # Forest - 9
    forest = Room('You stand at the outskirts of the forest. You feel uneasy. '
                  'You can continue to the east, or return to the road in the west. ', None, 11, None, 7, None, None)
    room_list.append(forest)
    # Lake - 10
    lake = Room('You stand on the edge of a lake. It is clearly not your typical body of water. '
                'Stepping down into it may be worth a try. There is a road to the east.', None, 7, None, None, 12, None)
    room_list.append(lake)
    # Fortress Entrance - 11
    f_entrance = Room('You\'ve arrived at the entrance of a fortress. '
                      'You can enter the gate by continuing east, or try to scale the wall.'
                      'The forest is to the west.', None, 13, None, 9, None, 14)
    room_list.append(f_entrance)
    # Lake portal - 12
    l_portal = Room('Entering the lake has left you in a small room. '
                    'There is a treasure chest present. It requires a key. '
                    'You can return to the surface.', None, None, None, None, None, 10)
    room_list.append(l_portal)

    player_class = None
    class_select = input('What is your class of choice? ').lower()
    if 'wizard' in class_select:
        player_class = wizard
    elif 'rogue' in class_select:
        player_class = rogue
    elif 'warrior' in class_select:
        player_class = warrior
    else:
        print('Please select a valid class.')

    print("You have awoken from what feels like years of sleep. You are currently in a mansion."
          "\nIt would be wise to seek out someone who knows why.\nInput C for controls.")

    while not done:
        if current_room == 8 and dialogue_flag.room_number == -2:
            print('\nYou must be the new hero. I\'m the town\'s chief guard. I\'ll fill you in on what\'s going on.\n'
                  'To the southeast, through the forest, is a fortress. A dragon inhabits it. That dragon\n'
                  'used to protect us, but now it antagonizes the village...\n'
                  'I don\'t know what caused it to change, but as of now,\n'
                  'it believes that only the strong have a right to live.\n'
                  'Those who cannot protect themselves must die. That is the dragon\'s doctrine.\n'
                  'Countless heroes like yourself have tried to stop the dragon, but they never return...\n'
                  'If you wish to follow in their footsteps, take care in preparing yourself.')
            dialogue_flag.room_number = -3

        print('\n',room_list[current_room].description)

        for item in item_list:
            if item.room_number == current_room:
                print(item.i_description)
        command_words = input("What is your command? ").lower().split(" ")

        if command_words[0] == 'n':
            next_room = room_list[current_room].north

        elif command_words[0] == 's':
            next_room = room_list[current_room].south

        elif command_words[0] == 'e':
            next_room = room_list[current_room].east

        elif command_words[0] == 'w':
            next_room = room_list[current_room].west

        elif command_words[0] == 'd':
            next_room = room_list[current_room].down

        elif command_words[0] == 'u':
            next_room = room_list[current_room].up

        elif command_words[0] == 'c':
            print('N, E, S, W, for cardinal directions, '
                  'D, U, for down and up,\nI for inventory, '
                  'get to retrieve items, drop to drop items, and u to use items.'
                  'status for character status.\nQ to quit.')

        elif 'get' in command_words:
            found = False
            for item in item_list:
                if item.room_number == current_room:
                    item.room_number = -1
                    print('You retrieved the ', item.i_name, '.')
                    found = True
            if not found:
                print('No items are present.')

        elif 'status' in command_words:
            print('You have', player_class.class_hp, 'health and ', player_class.mana, 'mana.'
                  ' Your attack stat is', player_class.class_attack,'.')

        elif command_words[0] == 'i':
            found = False
            for item in item_list:
                if item.room_number == -1:
                    print('Your inventory contains', item.i_name)
                    found = True
            if not found:
                print('Your inventory is empty.')

        elif 'drop' in command_words:
            drop = input("What would you like to drop? ").lower()
            # for item in item_list:
            #     if item.room_number == -1:
            #         if drop == item.i_name:
            #             item.room_number = current_room

            for i in range(len(item_list)):
                if item_list[i].room_number == -1:
                    if drop == item_list[i].i_name:
                        item_list[i].room_number = current_room

        elif 'use' in command_words:
            use = input("What would you like to use? ").lower()

            for i in range(len(item_list)):
                if item_list[i].room_number == -1:
                    if use == item_list[i].i_name:
                        if use == 'mirror':
                            print('You look dashing.')

                        elif use == 'key':
                            if current_room == 12:
                                print('The chest was opened, but the key broke in the process.')
                                key.room_number = -2
                                charm.room_number = 12

                        elif use == 'charm':
                            print('The charm is absorbed into your weapon. You\'ve gotten stronger.')
                            player_class.class_attack += 3
                            charm.room_number = -2

        elif command_words[0] == 'q':
            print("Game over.")
            break

        else:
            print("Please give a valid command.")
            continue

        # check for valid choice
        if next_room == None:
            print("You can't go that way!")
            continue

        # if all is well, set new room
        current_room = next_room


main()
