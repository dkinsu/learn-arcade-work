import random
import lab_12_rooms
import lab_12_items

# Inventory and out of play
INV = -1
OOP = -2

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
    def __init__(self, monster_description, monster_name, monster_hp, monster_attack, m_skill1, m_skill1_dmg, m_skill2, m_skill2_dmg, m_taunt):
        self.monster_description = monster_description
        self.monster_name = monster_name
        self.monster_hp = monster_hp
        self.monster_attack = monster_attack
        self.m_skill1 = m_skill1
        self.m_skill1_dmg = m_skill1_dmg
        self.m_skill2 = m_skill2
        self.m_skill2_dmg = m_skill2_dmg
        self.m_taunt = m_taunt


# def player_classes(wizard, warrior, rogue):



# not in class!
def get_item(item_list, name):
    for item in item_list:
        if name == item.i_name:
            return item

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

    cube = Enemy('A BIG CUBE.', 'THE CUBE', 50, 7, 'CUBIC CONTACT', 7, 'CUBE HYPER STRIKE', 14, 'YOU ARE NO MATCH FOR THE CUBE.')
    item_list = []
    dialogue_flag = 0
    cube_defeated = 0
    long_defeated = 0
    dragon_defeated = 0
    done = False

    flag = False
    player_class = None
    while not flag:
        class_select = input('What is your class of choice? ').lower()
        if 'wizard' in class_select:
            player_class = wizard
            flag = True
        elif 'rogue' in class_select:
            player_class = rogue
            flag = True
        elif 'warrior' in class_select:
            player_class = warrior
            flag = True
        else:
            print('Please select a valid class.')

    print("You have awoken from what feels like years of sleep. You are currently in a mansion."
          "\nIt would be wise to seek out someone who knows why.\nInput C for controls.")
    item_list = lab_12_items.populate_items()
    while not done:
        if lab_12_rooms.current_room == 8 and dialogue_flag == 0:
            print('\nYou must be the new hero. I\'m the town\'s chief guard. I\'ll fill you in on what\'s going on.\n'
                  'To the southeast, through the forest, is a fortress. A dragon inhabits it. That dragon\n'
                  'used to protect us, but now it antagonizes the village...\n'
                  'I don\'t know what caused it to change, but as of now,\n'
                  'it believes that only the strong have a right to live.\n'
                  'Those who cannot protect themselves must die. That is the dragon\'s doctrine.\n'
                  'Countless heroes like yourself have tried to stop the dragon, but they never return...\n'
                  'If you wish to follow in their footsteps, take care in preparing yourself.')
            dialogue_flag = 1

        print('\n',lab_12_rooms.room_list[lab_12_rooms.current_room].description)

        # item_list = lab_12_items.populate_items()
        for item in item_list:
            if item.room_number == lab_12_rooms.current_room:
                print(item.i_description)
        command_words = input("What is your command? ").lower().split(" ")

        if command_words[0] == 'n':
            lab_12_rooms.next_room = lab_12_rooms.room_list[lab_12_rooms.current_room].north

        elif command_words[0] == 's':
            lab_12_rooms.next_room = lab_12_rooms.room_list[lab_12_rooms.current_room].south

        elif command_words[0] == 'e':
            lab_12_rooms.next_room = lab_12_rooms.room_list[lab_12_rooms.current_room].east

        elif command_words[0] == 'w':
            lab_12_rooms.next_room = lab_12_rooms.room_list[lab_12_rooms.current_room].west

        elif command_words[0] == 'd':
            lab_12_rooms.next_room = lab_12_rooms.room_list[lab_12_rooms.current_room].down

        elif command_words[0] == 'u':
            lab_12_rooms.next_room = lab_12_rooms.room_list[lab_12_rooms.current_room].up

        elif command_words[0] == 'c':
            print('N, E, S, W, for cardinal directions, '
                  'D, U, for down and up,\nI for inventory, '
                  'get to retrieve items, drop to drop items, and u to use items.'
                  'status for character status.\nQ to quit.')

        elif 'get' in command_words:
            found = False
            for item in item_list:
                if item.room_number == lab_12_rooms.current_room:
                    item.room_number = INV
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
                if item.room_number == INV:
                    print('Your inventory contains', item.i_name)
                    found = True
            if not found:
                print('Your inventory is empty.')

        elif 'drop' in command_words:
            drop = input("What would you like to drop? ").lower()

            for i in range(len(item_list)):
                if item_list[i].room_number == INV:
                    if drop == item_list[i].i_name:
                        item_list[i].room_number = lab_12_rooms.current_room

        elif 'use' in command_words:
            use = input("What would you like to use? ").lower()

            for i in range(len(item_list)):
                if item_list[i].room_number == INV:
                    if use == item_list[i].i_name:
                        if use == 'mirror':
                            print('You look dashing.')

                        elif use == 'key':
                            if lab_12_rooms.current_room == 12:
                                print('The chest was opened, but the key broke in the process.')
                                item_list[i].room_number = OOP
                                charm = get_item(item_list, 'charm')
                                charm.room_number = 12

                        elif use == 'charm':
                            print('The charm is absorbed into your weapon. You\'ve gotten stronger.')
                            player_class.class_attack += 3
                            charm = get_item(item_list, 'charm')
                            charm.room_number = OOP

                        elif use == 'elixir':
                            print('You\'ve been fully healed.')
                            # hp = max_hp
                            elixir = get_item(item_list, 'elixir')
                            elixir.room_number = OOP
                    else:
                        print('You do not have that item.')
        elif command_words[0] == 'q':
            print("Game over.")
            break

        else:
            print("Please give a valid command.")
            continue

        # check for valid choice
        if lab_12_rooms.next_room == None:
            print("You can't go that way!")
            continue

        # if all is well, set new room
        lab_12_rooms.current_room = lab_12_rooms.next_room


main()
