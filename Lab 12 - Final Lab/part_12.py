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

    glass_key = Item(5, "A glass key. Brittle. It will definitely break after use.", "Glass Key")
    hp_potion_1 = Item(-1, "A health potion. It will restore your HP, but can only be used once.", "Health Potion")

    # Bedroom 2 - 0 - (description, north, east, south, west)
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
    balcony = Room("You are on the balcony.\nThere is a door to the south.", None, None, 4, None, None, None)
    room_list.append(balcony)

    print("Welcome to the haunted mansion!\nDo your best to escape!\nInput q to quit.")

    while not done:
        # rudimentary gameplay through avoidance of enemies
        # dining room ghost
        if room_list[current_room] == dining_room:
            print("There is a hungry looking ghost present.\nYou can fight, or avoid it.\n(f, or n, e, s, w input)")
            fight = input("Fight? ").lower()
            if fight[0] == 'f':
                print("Why did you think you could beat a ghost? Game over.")
                break

        # kitchen vampire
        if room_list[current_room] == kitchen:
            print("There is a vampire standing in the kitchen.\nQuick, throw the nearby garlic at him!\n(yes/no)")
            throw = input("Throw garlic? ").lower()
            if throw[0] == 'y':
                print("The vampire is dazed. Best to leave now. ")
            else:
                print("You probably should have thrown that garlic. Now you're the vampire's meal. Game Over.")
                break

        # bedroom 1 werewolf
        if room_list[current_room] == bedroom1:
            print("There is a werewolf in the bedroom! It's too fast to avoid! Game over.")
            break

        # balcony escape
        if room_list[current_room] == balcony:
            print("Maybe you can jump off the balcony to escape.")
            jump = input("Jump? (yes/no) ").lower()
            if jump[0] == 'y':
                print("You safely land from the balcony, and escape the creatures of the night.\nYou win! Game over.")
                break

        print(room_list[current_room].description)
        direction = input("Which way would you like to go? (n s e w) ").lower()

        if direction[0] == 'n':
            next_room = room_list[current_room].north

        elif direction[0] == 's':
            next_room = room_list[current_room].south

        elif direction[0] == 'e':
            next_room = room_list[current_room].east

        elif direction[0] == 'w':
            next_room = room_list[current_room].west

        elif direction[0] == 'q':
            print("Game over.")
            break

        else:
            print("Please pick a valid direction.")
            continue

        # check for valid choice
        if next_room == None:
            print("You can't go that way!")
            continue

        # if all is well, set new room
        current_room = next_room


main()
