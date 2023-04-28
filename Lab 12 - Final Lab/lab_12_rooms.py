class Room:
    def __init__(self, description, north, east, south, west, down, up):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.down = down
        self.up = up

room_list = []
current_room = 0
next_room = 0

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
