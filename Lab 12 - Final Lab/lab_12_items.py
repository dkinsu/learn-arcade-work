class Item:
    def __init__(self, room_number, i_description, i_name):
        self.room_number = room_number
        self.i_description = i_description
        self.i_name = i_name

def populate_items():
    item_list = []
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
    return item_list