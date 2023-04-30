import random
import arcade

# import lab_12_sounds
import lab_12_rooms
import lab_12_items
import lab_12_combatants

# Inventory and out of play
INV = -1
OOP = -2

# Music
exploration = arcade.load_sound('DS1_Char_Creation.mp3')
exploration_player = exploration.play(0.5, 0, True)


# not in class!


def get_item(item_list, name):
    for item in item_list:
        if name == item.i_name:
            return item


def main():
    wizard = lab_12_combatants.PlayerClass("A class that wields magic.\nPowerful ranged offense, weaker defense.",
                                            "Wizard", 40, 40, 5, 60, 60, "Amplify", "Flare", 4,
                                            'Triples your attack power for the duration of the battle. '
                                            'Can be used multiple times. Costs 40 mana.',
                                            'Cause a fiery explosion. High damage. Costs 20 mana.')

    warrior = lab_12_combatants.PlayerClass("A class that fights with heavy close ranged weapons."
                                            "\nClose-ranged offense, strong defense.",
                                            "Warrior", 60, 60, 8, 30, 30, "Invigorating Cleave", "Guard", 2,
                                            'A long-reaching powerful swing. Deals extra damage proportional to '
                                            'warrior\'s missing HP, and returns 33% of warrior\'s missing HP. Costs 15 mana.',
                                            'Heavily reduces incoming damage. Requires 10 mana to use, but restores 10 mana.')

    rogue = lab_12_combatants.PlayerClass("A class that fights with melee and ranged weapons."
                                          "\nVersatile offense, middling defense.",
                                            'Rogue', 50, 50, 10, 45, 45, "Lacerate", "Retreating Shot", 1,
                                            'A devastating close-ranged attack. Poor range,'
                                            ' heavy damage. Halves the damage the next enemy attack. Costs 15 mana.',
                                            'Fire a shot with a bow before performing evasive maneuvers. '
                                            'Creates distance. Costs 25 mana.')

    cube = lab_12_combatants.Enemy('A BIG CUBE.', 'THE CUBE', 5, 'CUBIC CONTACT', 7,
                                   'CUBE HYPER STRIKE', 14, 'YOU ARE NO MATCH FOR THE CUBE.')
    long_swordsman = lab_12_combatants.Enemy('A warrior renowned for his height... '
                                             'though the size of his limbs is rather lacking.',
                                              'The Long Warrior', 1, 'Straight punch', 12, '90-degree headbutt', 18,
                                              'A shame. They could not match up to my height.')
    dragon = lab_12_combatants.Enemy('The guardian of the village. Something is controlling the dragon\'s behavior.', 'The Dragon',
                                     1, 'Flame Breath', 12, 'Wrathful Claw', 25, 'You were mighty... But not mighty enough.')
    # item_list = []
    dialogue_flag = 0
    cube_defeated = False
    long_defeated = False
    dragon_defeated = False
    battle = False
    done = False

    flag = False
    player_class = None
    current_enemy = None
    while not flag:
        print(warrior.class_name, ':', warrior.player_description)
        print(rogue.class_name, ':', rogue.player_description)
        print(wizard.class_name, ':', wizard.player_description)
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

    print("\nYou have awoken from what feels like years of sleep. You are currently in a mansion."
          "\nIt would be wise to seek out someone who knows why.\nInput C for controls.")
    # arcade.play_sound(exploration, 0.6, 0, True, 1)
    item_list = lab_12_items.populate_items()
    while not done:
        # Exploration Music
        # arcade.play_sound(exploration, 0.8)
        # One time dialogue in town
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
        # Battle 1 - Cube
        elif lab_12_rooms.current_room == 11 and not cube_defeated:
            current_enemy = cube
            battle = True
            exploration_player.pause()
        # Battle 2 - Long warrior
        elif lab_12_rooms.current_room == 13 and not long_defeated:
            current_enemy = long_swordsman
            battle = True
            exploration_player.pause()
        elif lab_12_rooms.current_room == 15 and not dragon_defeated:
            current_enemy = dragon
            battle = True
            exploration_player.pause()
        if not battle:
            print('\n', lab_12_rooms.room_list[lab_12_rooms.current_room].description)

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
                      ' Your attack stat is', player_class.class_attack, '.')

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
                                    key = get_item(item_list, 'key')
                                    # item_list[i].room_number = OOP
                                    key.room_number = OOP
                                    charm = get_item(item_list, 'charm')
                                    charm.room_number = 12

                            elif use == 'charm':
                                print('The charm is absorbed into your weapon. You\'ve gotten stronger.')
                                player_class.class_attack += 3
                                charm = get_item(item_list, 'charm')
                                charm.room_number = OOP

                            elif use == 'elixir':
                                print('You\'ve been fully healed.')
                                player_class.class_hp = player_class.class_max_hp
                                elixir = get_item(item_list, 'elixir')
                                elixir.room_number = OOP

                            elif use == 'talisman':
                                player_class.class_max_hp += 5
                                player_class.class_hp = player_class.class_max_hp
                                print('You\'ve been fully healed, and your max HP increased. Max HP is now', player_class.class_max_hp, '.')
                                talisman = get_item(item_list, 'talisman')
                                talisman.room_number = OOP

            elif command_words[0] == 'q':
                print("Game over.")
                done = True


            else:
                print("Please give a valid command.")
                continue

            # check for valid choice
            if lab_12_rooms.next_room == None:
                print("You can't go that way!")
                continue

            # if all is well, set new room
            lab_12_rooms.current_room = lab_12_rooms.next_room

            # ///////////////////////////////////////////////////// Battle /////////////////////////////////////////////////////
        elif battle == True:
            while current_enemy.monster_hp > 0 and player_class.class_hp > 0:
                guard = 1
                distance = 4
                action = False
                print('You are challenged by', current_enemy.monster_name, '!')
                print('Combat commands: B: Basic attack, 1: Skill 1, 2: Skill 2, advance, retreat, wait, status')
                print('Input controls to show commands.')
                while current_enemy.monster_hp > 0:
                    if player_class.class_hp <= 0:
                        print(current_enemy.m_taunt, '\n You were defeated. Game over.')
                        battle = False
                        cube_defeated = True
                        long_defeated = True
                        dragon_defeated = True
                        done = True
                        break

                    print(current_enemy.monster_name, 'is ', distance, 'meters away.')
                    # command_words = input("What is your command? ").lower().split(" ")
                    while not action:
                        command_words = input("What is your command? ").lower().split(" ")
                        if command_words[0] == 'b' and player_class.p_range >= distance:
                            damage = player_class.class_attack
                            current_enemy.monster_hp -= damage
                            if current_enemy.monster_hp < 0:
                                current_enemy.monster_hp = 0
                            print('You have dealt', damage, 'damage.', player_class.mana, 'mana remains.',
                                  ' You have', player_class.class_hp, 'HP remaining. The enemy has',
                                  current_enemy.monster_hp, 'HP remaining.')
                            # Mana regeneration on basic attack
                            if player_class.mana < player_class.max_mana:
                                if player_class == wizard:
                                    player_class.mana += 10
                                    if player_class.mana > player_class.max_mana:
                                        player_class.mana = player_class.max_mana
                                elif player_class == warrior:
                                    player_class.mana += 5
                                    if player_class.mana > player_class.max_mana:
                                        player_class.mana = player_class.max_mana
                                else:
                                    player_class.mana += 7
                                    if player_class.mana > player_class.max_mana:
                                        player_class.mana = player_class.max_mana
                            action = True

                        elif command_words[0] == 'b' and player_class.p_range < distance:
                            print('A valiant attempt. You are too far away.')
                            action = True

                        # Movement commands
                        elif 'wait' in command_words:
                            if player_class == wizard:
                                player_class.mana += 20
                                if player_class.mana > player_class.max_mana:
                                    player_class.mana = player_class.max_mana
                            else:
                                player_class.mana += 10
                                if player_class.mana > player_class.max_mana:
                                    player_class.mana = player_class.max_mana
                            print('You remain in place, recovering mana.', player_class.mana, 'mana remains.',
                                  ' Your HP is', player_class.class_hp, '.')
                            action = True

                        elif 'advance' in command_words:
                            if distance == 1:
                                print('You\'re at point blank range.')
                            else:
                                distance -= 1
                                if player_class == rogue:
                                    player_class.mana += 7
                                    if player_class.mana > player_class.max_mana:
                                        player_class.mana = player_class.max_mana
                                else:
                                    player_class.mana += 4
                                    if player_class.mana > player_class.max_mana:
                                        player_class.mana = player_class.max_mana
                                print('You advanced one meter. Mana recovered.', player_class.mana, 'mana remains.',
                                      ' Your HP is', player_class.class_hp, '.')
                                action = True
                        elif 'status' in command_words:
                            print('You have', player_class.class_hp, 'HP and', player_class.mana, 'Mana. '
                                    'The enemy has', current_enemy.monster_hp, 'HP. You are', distance, 'meters from the enemy. '
                                    'Your enemy is', current_enemy.monster_name, '.\n', current_enemy.monster_description)
                        elif 'controls' in command_words:
                            print('Combat commands: B: Basic attack, 1: Skill 1, 2: Skill 2, advance, retreat, wait')

                        elif 'retreat' in command_words:
                            retreat_roll = random.randrange(0, 7)
                            if retreat_roll <= 2:
                                r_storage = 2
                                distance += r_storage
                            elif retreat_roll > 2 and retreat_roll <= 5:
                                r_storage = 3
                                distance += r_storage
                            else:
                                r_storage = 4
                                distance += r_storage
                            if player_class == rogue:
                                player_class.mana += 7
                                if player_class.mana > player_class.max_mana:
                                    player_class.mana = player_class.max_mana
                            else:
                                player_class.mana += 4
                                if player_class.mana > player_class.max_mana:
                                    player_class.mana = player_class.max_mana
                            print('You retreated', r_storage, 'meters. Mana recovered.', player_class.mana, 'mana remains.',
                                  ' Your HP is', player_class.class_hp, '.')
                            action = True
                        # Skill 1
                        elif command_words[0] == '1':
                            # Wizard skill 1
                            if player_class == wizard and player_class.mana >= 40:
                                player_class.class_attack *= 3
                                if player_class.class_attack < 30:
                                    print('Your mana amplifies your power. That\'s more like it.')
                                elif player_class.class_attack > 30:
                                    print('Your strength is overflowing.')
                                elif player_class.class_attack > 100:
                                    print('This is excessive.')
                                player_class.mana -= 40
                                print(player_class.mana, 'mana remains.')
                                action = True
                            elif player_class == wizard and player_class.mana < 40:
                                print('You don\'t have enough mana.')

                                # Warrior skill 1
                            elif player_class == warrior:
                                if distance <= 3 and player_class.mana >= 15:
                                    print('You swing your sword destructively. The strike invigorates you.')
                                    damage = player_class.class_attack * (warrior.class_max_hp // warrior.class_hp)
                                    current_enemy.monster_hp -= damage
                                    warrior.class_hp = warrior.class_hp + ((warrior.class_max_hp - warrior.class_hp) // 3)
                                    if current_enemy.monster_hp < 0:
                                        current_enemy.monster_hp = 0
                                    print('You have dealt', damage, 'damage.',
                                          ' You have', player_class.class_hp, 'HP remaining. The enemy has',
                                          current_enemy.monster_hp,
                                          'HP remaining.')
                                    player_class.mana -= 15
                                    action = True
                                elif distance > 3 and player_class.mana >= 15:
                                    print('You swing your sword destructively... From too far away.')
                                    print('You have dealt 0 damage.',
                                          ' You have', player_class.class_hp, 'HP remaining. The enemy has',
                                          current_enemy.monster_hp,
                                          'HP remaining.')
                                    player_class.mana -= 15
                                    print(player_class.mana, 'mana remains.')
                                    action = True
                                elif player_class.mana < 15:
                                    print('You don\'t have enough mana.')

                                    # Rogue skill 1
                            else:
                                if distance == 1 and player_class.mana >= 15:
                                    print('They won\'t be prepared for this.')
                                    damage = player_class.class_attack * 4
                                    current_enemy.monster_hp -= damage
                                    if current_enemy.monster_hp < 0:
                                        current_enemy.monster_hp = 0
                                    print('You have dealt', damage, 'damage.',
                                          ' You have', player_class.class_hp, 'HP remaining. The enemy has',
                                          current_enemy.monster_hp,
                                          'HP remaining.')
                                    guard = 2
                                    player_class.mana -= 15
                                    print(player_class.mana, 'mana remains.')
                                    action = True
                                elif distance > 1 and player_class.mana >= 15:
                                    print('They won\'t be prepared for this... But neither were you. You missed.')
                                    print('You have dealt 0 damage.',
                                          ' You have', player_class.class_hp, 'HP remaining. The enemy has',
                                          current_enemy.monster_hp,
                                          'HP remaining.')
                                    player_class.mana -= 15
                                    print(player_class.mana, 'mana remains.')
                                    action = True
                                elif player_class.mana < 15:
                                    print('You don\'t have enough mana.')
                        # Skill 2
                        # Wizard skill 2
                        elif command_words[0] == '2':
                            if player_class == wizard and player_class.mana >= 20:
                                if distance <= 4:
                                    print('Turn them to ash.')
                                    damage = player_class.class_attack * 3
                                    current_enemy.monster_hp -= damage
                                    if current_enemy.monster_hp < 0:
                                        current_enemy.monster_hp = 0
                                    print('You have dealt', damage, 'damage.',
                                          ' You have', player_class.class_hp, 'HP remaining. The enemy has',
                                          current_enemy.monster_hp,
                                          'HP remaining.')
                                    player_class.mana -= 20
                                    print(player_class.mana, 'mana remains.')
                                    action = True
                                elif distance > 4:
                                    print('Turn them to ash. Or try to, like you just did. You missed.')
                                    print('You have dealt 0 damage.',
                                          ' You have', player_class.class_hp, 'HP remaining. The enemy has',
                                          current_enemy.monster_hp,
                                          'HP remaining.')
                                    player_class.mana -= 20
                                    print(player_class.mana, 'mana remains.')
                                    action = True
                                elif player_class.mana < 20:
                                    print('You don\'t have enough mana.')
                            # Warrior skill 2
                            elif player_class == warrior:
                                if player_class.mana >= 10:
                                    print('Your defenses are raised. You gain 10 mana.')
                                    guard = 3
                                    player_class.mana += 10
                                    if player_class.mana > player_class.max_mana:
                                        player_class.mana = player_class.max_mana
                                    print(player_class.mana, 'mana remains.')
                                    action = True
                                elif player_class.mana < 10:
                                    print('You don\'t have enough mana.')
                                    print(player_class.mana, 'mana remains.')
                            # Rogue skill 2
                            elif player_class == rogue:
                                if distance <= 3 and player_class.mana >= 25:
                                    print('They won\'t be catching you anytime soon.')
                                    distance += 2
                                    damage = player_class.class_attack * 2
                                    current_enemy.monster_hp -= damage
                                    if current_enemy.monster_hp < 0:
                                        current_enemy.monster_hp = 0
                                    print('You have dealt', damage, 'damage.',
                                          ' You have', player_class.class_hp, 'HP remaining. The enemy has',
                                          current_enemy.monster_hp,
                                          'HP remaining.')
                                    player_class.mana -= 25
                                    print(player_class.mana, 'mana remains.')
                                    action = True
                                elif distance > 3 and player_class.mana >= 25:
                                    print('They won\'t be catching you anytime soon. '
                                          'But you won\'t be catching them either with aim like that.')
                                    print('You have dealt 0 damage.',
                                          ' You have', player_class.class_hp, 'HP remaining. The enemy has',
                                          current_enemy.monster_hp,
                                          'HP remaining.')
                                    distance += 2
                                    player_class.mana -= 25
                                    print(player_class.mana, 'mana remains.')
                                    action = True
                                elif player_class.mana < 25:
                                    print('You don\'t have enough mana.')
                                    print(player_class.mana, 'mana remains.')
                        else:
                            print('Please input a valid command.')
                    # Victory, ending battle
                    if current_enemy.monster_hp <= 0:
                        print('You have defeated', current_enemy.monster_name, '!')
                        # Wizard gains extra HP and mana on win
                        if player_class == wizard:
                            wizard.class_max_hp += 5
                            wizard.class_hp += 5
                            wizard.max_mana += 10
                            wizard.mana = wizard.max_mana
                            charm = get_item(item_list, 'charm')
                            if charm.room_number != OOP:
                                wizard.class_attack = 5
                            else: wizard.class_attack = 8
                            # Warrior regains 66% of missing HP on victory and gains more max HP
                        elif player_class == warrior:
                            warrior.mana = warrior.max_mana
                            warrior.class_max_hp += 10
                            warrior.class_hp = warrior.class_hp + ((warrior.class_max_hp - warrior.class_hp) // 1.5)
                        else:
                            # Rogue gets more max mana on victory
                            rogue.max_mana += 15
                            rogue.mana = rogue.max_mana
                        if current_enemy == cube:
                            cube_defeated = True
                            exploration_player.play()
                        elif current_enemy == long_swordsman:
                            long_defeated = True
                            exploration_player.play()
                        elif current_enemy == dragon:
                            dragon_defeated = True
                            exploration_player.play()
                        battle = False
                    else:
                        # Enemy Movement
                        if distance > 1:
                            if distance >= 3:
                                enemy_move = random.randrange(0, 2)
                                if enemy_move == 1:
                                    distance -= 2
                                    print(current_enemy.monster_name, 'moved 2 meters.')
                                    action = False
                                    if distance <= 0:
                                        distance = 1
                                else:
                                    print(current_enemy.monster_name, 'moved 1 meter.')
                                    action = False
                                    distance -= 1
                                    if distance <= 0:
                                        distance = 1
                            elif distance > 1:
                                distance -= 1
                                print(current_enemy.monster_name, 'moved 1 meter.')
                                action = False
                        if distance == 1:
                            enemy_action = random.randrange(0, 4)
                            if enemy_action == 1:
                                print(current_enemy.monster_name, 'makes no action.')
                                action = False

                            enemy_attack = random.randrange(0, 2)
                            if enemy_attack == 1 and enemy_action != 1:
                                print(current_enemy.monster_name, 'is using', current_enemy.m_skill1)
                                enemy_damage = current_enemy.m_skill1_dmg
                                dmg_received = enemy_damage // guard
                                player_class.class_hp -= dmg_received
                                print('You received', dmg_received, 'damage.')
                                guard = 1
                                if current_enemy == dragon:
                                    print('The dragon\'s fire siphons your mana.')
                                    player_class.mana -= 5
                                action = False
                            else:
                                if enemy_action != 1:
                                    print(current_enemy.monster_name, 'is using', current_enemy.m_skill2)
                                    enemy_damage = current_enemy.m_skill2_dmg
                                    dmg_received = enemy_damage // guard
                                    player_class.class_hp -= dmg_received
                                    print('You received', dmg_received, 'damage.')
                                    guard = 1
                                    if current_enemy == dragon:
                                        print('The dragon\'s claws sunder your defenses.')
                                        guard = 0.5
                                    action = False
main()
