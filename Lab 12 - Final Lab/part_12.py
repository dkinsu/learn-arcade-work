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
    def __init__(self, player_description, class_name, class_hp, class_attack, mana, p_skill1, p_skill2, p_range):
        self.player_description = player_description
        self.class_name = class_name
        self.class_hp = class_hp
        self.class_attack = class_attack
        self.mana = mana
        self.p_skill1 = p_skill1
        self.p_skill2 = p_skill2
        self.p_range = p_range


class Enemy:
    def __init__(self, monster_description, monster_name, monster_hp, monster_attack, m_skill1, m_skill2, m_range):
        self.monster_description = monster_description
        self.monster_name = monster_name
        self.monster_hp = monster_hp
        self.monster_attack = monster_attack
        self.m_skill1 = m_skill1
        self.m_skill2 = m_skill2
        self.m_range = m_range


def player_classes():
    wizard = PlayerClass("A class that wields magic.\nPowerful ranged offense, weaker defense.",
                         "Wizard", 40, 15, 60, "Amplify", "Flare", 4)
    warrior = PlayerClass("A class that fights with heavy close ranged weapons.\nClose-ranged offense, strong defense.",
                          "Warrior", 60, 7, 30, "Cleave", "Guard Crash", 2)
    rogue = PlayerClass("A class that fights with melee and ranged weapons.\nVersatile offense, middling defense.",
                        'Rogue', 50, 10, 45, "Lacerate", "Retreating Shot", 1)

# not in class!


def main():
    player_classes()
    item_list = []
    room_list = []
    current_room = 0
    next_room = 0
    done = False

    key = Item(3, "A glass key. Brittle. It will definitely break after use. Get the key?", "key")
    item_list.append(key)
    elixir = Item(2, "A healing elixir. It will restore your HP, but can only be used once. Get the elixir?",
                  "Health Elixir")
    item_list.append(elixir)

    # Bedroom 2 - 0 - (description, north, east, south, west, down, up)
    room = Room("You are in the second bedroom, there is a door to the east.", None, 1, None, None, None, None)
    room_list.append(room)

    # South Hall - 1
    south_hall = Room("You are in the south hall.\nThere are doors to the north, east, and west.", 4, 2, None, 0, None, None)
    room_list.append(south_hall)

    # Dining Room - 2
    dining_room = Room("You are in the dining room.\nThere are doors to the west and north.", 5, None, None, 1, None, None)
    room_list.append(dining_room)

    # Bedroom 1 - 3
    bedroom1 = Room("You are in the first bedroom.\nThere is a door to the east.", None, 4, None, None, None, None)
    room_list.append(bedroom1)

    # North Hall - 4
    north_hall = Room("You are in the north hall.\nThere are doors to the north, east, south, and west.", 6, 5, 1, 3, None, None)
    room_list.append(north_hall)

    # Kitchen - 5
    kitchen = Room("You are in the kitchen.\nThere are doors to the south and west.", None, None, 2, 4, None, None)
    room_list.append(kitchen)

    # Balcony - 6
    balcony = Room("You are on the balcony.\nThere is a door to the south.", None, None, 4, None, 7, None)
    room_list.append(balcony)

    # Town road - 7
    """town_road = Room('You are on the road to a nearby town. The town is to the north, '
                     'there is a forest to the east, and a lake to the west. '
                     'You can also climb back up to the balcony. ', 8, 9, None, 10, None, 6)
    # Town - 8"""

    print("You have awoken from what feels like years of sleep. You are currently in a mansion."
          "\nIt would be wise to seek out someone who knows why.\nInput C for controls.")

    while not done:

        print(room_list[current_room].description)

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
            print('N, E, S W, for cardinal directions, '
                  'D, U, for down and up,\nI for inventory, '
                  'get to retrieve items, drop to drop items, and u to use items. Q to quit.')

        elif 'get' in command_words:
            found = False
            for item in item_list:
                if item.room_number == current_room:
                    item.room_number = -1
                    print (item.i_name, 'retrieved.')
                    found = True
            if not found:
                print('No items are present.')


        elif command_words[0] == 'i':
            found = False
            for item in item_list:
                if item.room_number == -1:
                    print('Your inventory contains', item.i_name)
                    found = True
            if not found:
                print('Your inventory is empty.')


        elif 'drop' in command_words:
            drop = input("What would you like to drop? ").lower
            for item in item_list:
                if item.room_number == -1:
                    if drop == item.i_name:
                        item.room_number = current_room

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
