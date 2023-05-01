import random


class PlayerClass:
    def __init__(self, player_description, class_name, class_hp, class_max_hp,
                 class_attack, mana, max_mana, p_skill1, p_skill2, p_range,
                 p_skill1_desc, p_skill2_desc, passive):
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
        self.passive = passive


class Enemy:
    def __init__(self, monster_description, monster_name, monster_hp,
                 m_skill1, m_skill1_dmg, m_skill2, m_skill2_dmg, m_taunt):
        self.monster_description = monster_description
        self.monster_name = monster_name
        self.monster_hp = monster_hp
        self.m_skill1 = m_skill1
        self.m_skill1_dmg = m_skill1_dmg
        self.m_skill2 = m_skill2
        self.m_skill2_dmg = m_skill2_dmg
        self.m_taunt = m_taunt

"""def main():
    wizard = PlayerClass("A class that wields magic.\nPowerful ranged offense, weaker defense.",
                         "Wizard", 40, 40, 5, 60, 60, "Amplify", "Flare", 4,
                         'Triples your attack power for the duration of the battle. Can be used multiple times. Costs 40 mana.',
                         'Cause a fiery explosion. High damage. Costs 20 mana.')

    warrior = PlayerClass("A class that fights with heavy close ranged weapons.\nClose-ranged offense, strong defense.",
                          "Warrior", 60, 60, 8, 30, 30, "Cleave", "Guard", 2,
                          'A long-reaching powerful swing. Deals extra damage proportional to warrior\'s missing HP. Costs 15 mana.',
                          'Heavily reduces incoming damage. Costs 10 mana.')

    rogue = PlayerClass("A class that fights with melee and ranged weapons.\nVersatile offense, middling defense.",
                        'Rogue', 50, 50, 10, 45, 45, "Lacerate", "Retreating Shot", 1,
                        'A devastating close-ranged attack. Poor range, heavy damage. Costs 15 mana.',
                        'Fire a shot with a bow before performing evasive maneuvers. Creates distance. Costs 25 mana.')

    cube = Enemy('A BIG CUBE.', 'THE CUBE', 80, 'CUBIC CONTACT', 7, 'CUBE HYPER STRIKE', 14, 'YOU ARE NO MATCH FOR THE CUBE.')
    long_swordsman = Enemy('A warrior renowned for his height... though the size of his limbs is rather lacking.',
                           'The Long Warrior', 120, 'Straight punch', 12, '90-degree headbutt', 18, 'A shame. They could not match up to my height.')

    current_enemy = None
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

    # damage = int
    guard = 1
    distance = 4
    current_enemy = cube
    print('You are challenged by', current_enemy.monster_name,'!')
    print('Combat commands: B: Basic attack, 1: Skill 1, 2: Skill 2, advance, retreat, wait')
    while current_enemy.monster_hp > 0:
        if player_class.class_hp <= 0:
            print(current_enemy.m_taunt, '\n You were defeated. Game over.')
            break
        print(current_enemy.monster_name, 'is ', distance, 'meters away.')
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

        elif command_words[0] == 'b' and player_class.p_range < distance:
            print('A valiant attempt. You are too far away.')

        # Movement commands
        elif 'wait' in command_words:
            print('You remain in place, recovering mana.')
            if player_class == wizard:
                player_class.mana += 20
                if player_class.mana > player_class.max_mana:
                    player_class.mana = player_class.max_mana
            else:
                player_class.mana += 10
                if player_class.mana > player_class.max_mana:
                    player_class.mana = player_class.max_mana

        elif 'advance' in command_words:
            if distance == 1:
                print('You\'re at point blank range.')
            else:
                distance -= 1
                print('You advanced one meter. Mana recovered.')
                if player_class == rogue:
                    player_class.mana += 7
                    if player_class.mana > player_class.max_mana:
                        player_class.mana = player_class.max_mana
                else:
                    player_class.mana += 4
                    if player_class.mana > player_class.max_mana:
                        player_class.mana = player_class.max_mana

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
            print('You retreated', r_storage, 'meters. Mana recovered.')
            if player_class == rogue:
                player_class.mana += 7
                if player_class.mana > player_class.max_mana:
                    player_class.mana = player_class.max_mana
            else:
                player_class.mana += 4
                if player_class.mana > player_class.max_mana:
                    player_class.mana = player_class.max_mana
    # Skill 1
        elif command_words[0] == '1':
            # Wizard
            if player_class == wizard and player_class.mana >= 40:
                player_class.class_attack *= 3
                if player_class.class_attack < 30:
                    print('Your mana amplifies your power. That\'s more like it.')
                elif player_class.class_attack > 30:
                    print('Your strength is overflowing.')
                elif player_class.class_attack > 100:
                    print('This is excessive.')
                player_class.mana -= 40
            elif player_class == wizard and player_class.mana < 40:
                print('You don\'t have enough mana.')

                # Warrior
            elif player_class == warrior:
                if distance <= 3 and player_class.mana >= 15:
                    print('You swing your sword destructively.')
                    damage = player_class.class_attack * 2
                    current_enemy.monster_hp -= damage
                    if current_enemy.monster_hp < 0:
                        current_enemy.monster_hp = 0
                    print('You have dealt', damage, 'damage.', player_class.mana, 'mana remains.',
                          ' You have', player_class.class_hp, 'HP remaining. The enemy has', current_enemy.monster_hp,
                          'HP remaining.')
                    player_class.mana -= 15
                elif distance > 3 and player_class.mana >= 15:
                    print('You swing your sword destructively... From too far away.')
                    print('You have dealt 0 damage.', player_class.mana, 'mana remains.',
                          ' You have', player_class.class_hp, 'HP remaining. The enemy has', current_enemy.monster_hp,
                          'HP remaining.')
                    player_class.mana -= 15
                elif player_class.mana < 15:
                    print('You don\'t have enough mana.')

                    # Rogue
            else:
                if distance == 1 and player_class.mana >= 15:
                    print('They won\'t be prepared for this.')
                    damage = player_class.class_attack * 4
                    current_enemy.monster_hp -= damage
                    if current_enemy.monster_hp < 0:
                        current_enemy.monster_hp = 0
                    print('You have dealt', damage, 'damage.', player_class.mana, 'mana remains.',
                          ' You have', player_class.class_hp, 'HP remaining. The enemy has', current_enemy.monster_hp,
                          'HP remaining.')
                    player_class.mana -= 15
                elif distance > 1 and player_class.mana >= 15:
                    print('They won\'t be prepared for this... But neither were you. You missed.')
                    print('You have dealt 0 damage.', player_class.mana, 'mana remains.',
                          ' You have', player_class.class_hp, 'HP remaining. The enemy has', current_enemy.monster_hp,
                          'HP remaining.')
                    player_class.mana -= 15
    # Skill 2
        # Wizard
        elif command_words[0] == '2':
            if player_class == wizard and player_class.mana >= 20:
                if distance <= 4:
                    print('Turn them to ash.')
                    damage = player_class.class_attack * 3
                    current_enemy.monster_hp -= damage
                    if current_enemy.monster_hp < 0:
                        current_enemy.monster_hp = 0
                    print('You have dealt', damage, 'damage.', player_class.mana, 'mana remains.',
                        ' You have', player_class.class_hp, 'HP remaining. The enemy has', current_enemy.monster_hp,
                        'HP remaining.')
                    player_class.mana -= 20
                elif distance > 4:
                    print('Turn them to ash. Or try to, like you just did. You missed.')
                    print('You have dealt 0 damage.', player_class.mana, 'mana remains.',
                          ' You have', player_class.class_hp, 'HP remaining. The enemy has', current_enemy.monster_hp,
                          'HP remaining.')
                    player_class.mana -= 20
                elif player_class.mana < 20:
                    print('You don\'t have enough mana.')
        # Warrior
            elif player_class == warrior:
                if player_class.mana >= 10:
                    print('Your defenses are raised.')
                    guard = 3
                elif player_class.mana < 10:
                    print('You don\'t have enough mana.')
        # Rogue
            else:
                if distance <= 3 and player_class.mana >= 25:
                    print('They won\'t be catching you anytime soon.')
                    distance += 2
                    damage = player_class.class_attack * 2
                    current_enemy.monster_hp -= damage
                    if current_enemy.monster_hp < 0:
                        current_enemy.monster_hp = 0
                    print('You have dealt', damage, 'damage.', player_class.mana, 'mana remains.',
                        ' You have', player_class.class_hp, 'HP remaining. The enemy has', current_enemy.monster_hp,
                        'HP remaining.')
                    player_class.mana -= 25
                elif distance > 3 and player_class.mana >= 25:
                    print('They won\'t be catching you anytime soon. '
                          'But you won\'t be catching them either with aim like that.')
                    print('You have dealt 0 damage.', player_class.mana, 'mana remains.',
                        ' You have', player_class.class_hp, 'HP remaining. The enemy has', current_enemy.monster_hp,
                        'HP remaining.')
                    distance += 2
                    player_class.mana -= 25
                elif player_class.mana < 25:
                    print('You don\'t have enough mana.')
        if current_enemy.monster_hp <= 0:
            print('You have defeated', current_enemy.monster_name, '!')
        else:
            if distance > 1:
                if distance >= 3:
                    enemy_move = random.randrange(0, 2)
                    if enemy_move == 1:
                        distance -= 2
                        print(current_enemy.monster_name, 'moved 2 meters.')
                        if distance <= 0:
                            distance = 1
                    else:
                        print(current_enemy.monster_name, 'moved 1 meter.')
                        distance -= 1
                        if distance <= 0:
                            distance = 1
                elif distance > 1:
                    distance -= 1
                    print(current_enemy.monster_name, 'moved 1 meter.')
            if distance == 1:
                enemy_action = random.randrange(0, 4)
                if enemy_action == 1:
                    print(current_enemy.monster_name, 'makes no action.')
            # Debugging - not sure how to prevent enemy action
                enemy_attack = random.randrange(0, 2)
                if enemy_attack == 1 and enemy_action != 1:
                    print(current_enemy.monster_name,'is using', current_enemy.m_skill1)
                    enemy_damage = current_enemy.m_skill1_dmg
                    dmg_received = enemy_damage // guard
                    player_class.class_hp -= dmg_received
                    print('You received', dmg_received, 'damage.')
                    guard = 1
                else:
                    if enemy_action != 1:
                        print(current_enemy.monster_name, 'is using', current_enemy.m_skill2)
                        enemy_damage = current_enemy.m_skill2_dmg
                        dmg_received = enemy_damage // guard
                        player_class.class_hp -= dmg_received
                        print('You received', dmg_received, 'damage.')
                        guard = 1"""
# main()
