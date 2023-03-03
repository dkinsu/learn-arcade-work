class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west

# not in class!
def main():
    room_list = []
    current_room = 0
    next_room = 0
    done = False

    # Bedroom 2 - 0 - (description, north, east, south, west)
    room = Room("You are in the second bedroom, there is a door to the east.", None, 1, None, None)
    room_list.append(room)

    # South Hall - 1
    southhall = Room("You are in the south hall. There are doors to the north, east, and west.", 4, 2, None, 0)
    room_list.append(southhall)

    # Dining Room - 2
    diningroom = Room("You are in the dining room. There are doors to the west and north.", 5, None, None, 1)
    room_list.append(diningroom)

    # Bedroom 1 - 3
    bedroom1 = Room("You are in the first bedroom. There is a door to the east.", None, 4, None, None)
    room_list.append(bedroom1)

    # North Hall - 4
    northhall = Room("You are in the north hall. There are doors to the north, east, south, and west.", 6, 5, 1, 3)
    room_list.append(northhall)

    # Kitchen - 5
    kitchen = Room("You are in the kitchen. There are doors to the south and west.", None, None, 2, 4)
    room_list.append(kitchen)

    # Balcony - 6
    balcony = Room("You are on the balcony. There is a door to the south.", None, None, 4, None)
    room_list.append(balcony)

    while not done:
        print(room_list[current_room].description)
        direction = input("Which way would you like to go? (n s e w) ").lower()
        if direction[0] == 'n':
            next_room = room_list[current_room].north

        elif direction[0] == 's':
            next_room = room_list[current_room].south
        # add other directions

        elif direction[0] == 'e':
            next_room = room_list[current_room].east

        elif direction[0] == 'w':
            next_room = room_list[current_room].west

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