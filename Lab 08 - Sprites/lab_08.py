""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 3.0
SPRITE_SCALING_RING = 1.0
SPRITE_SCALING_FIRE = 1.0
RING_COUNT = 50
FIRE_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.player_list = None
        self.ring_list = None
        self.fire_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.ring_list = arcade.SpriteList()
        self.fire_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl micro-roguelike
        self.player_sprite = arcade.Sprite("tile_0004.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(RING_COUNT):

            # Create the ring instance
            # ring image from kenney.nl micro-roguelike
            ring = arcade.Sprite("tile_0089.png", SPRITE_SCALING_RING)

            # Position the ring
            ring.center_x = random.randrange(SCREEN_WIDTH)
            ring.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the ring to the lists
            self.ring_list.append(ring)

        for i in range(FIRE_COUNT):

            # Creating fire instance
            # fire image from kenney.nl micro-roguelike
            fire = arcade.Sprite("tile_0136.png", SPRITE_SCALING_FIRE)

            # Positioning fire
            fire.center_x = random.randrange(SCREEN_WIDTH)
            fire.center_y = random.randrange(SCREEN_HEIGHT)

            self.fire_list.append(fire)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.ring_list.draw()
        self.fire_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.ring_list.update()
        self.fire_list.update()

        # Generate a list of all sprites that collided with the player.
        rings_hit_lists_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.ring_list)
        fire_hit_lists_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.fire_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for ring in rings_hit_lists_hit_list:
            ring.remove_from_sprite_lists()
            self.score += 1

        # Reducing score for bad sprites
        for fire in fire_hit_lists_hit_list:
            fire.remove_from_sprite_lists()
            self.score -= 1


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()