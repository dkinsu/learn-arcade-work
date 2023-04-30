import arcade
cube_pic = arcade.load_texture('iron_block.jpg')
def cube_draw():
    arcade.open_window(600, 600, 'CUBE')
    arcade.draw_lrwh_rectangle_textured(0,0, 600,600, cube_pic)
    arcade.start_render()
    arcade.finish_render()
    arcade.run()
cube_draw()