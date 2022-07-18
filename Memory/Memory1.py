#
# CMPUT 174
# Lab 4 Memory version 1
#
# First name: Yi
# Last name: Yang
# Lab section: H04
#
# Description: This is version 1 of the Memory program
#
#


import pygame
import random


# User-defined functions

def main():
    # initialize all pygame modules (some need initialization)
    pygame.init()
    # create a pygame display window
    pygame.display.set_mode((500, 400))
    # set the title of the display window
    pygame.display.set_caption('Memory')
    # get the display surface
    w_surface = pygame.display.get_surface()
    # create a game object
    game = Game(w_surface)
    # start the main game loop by calling the play method on the game object
    game.play()
    # quit pygame and clean up the pygame window
    pygame.quit()


# User-defined classes

class Game:
    # An object in this class represents a complete game.

    def __init__(self, surface):
        # Initialize a Game.
        # - self is the Game to initialize
        # - surface is the display window surface object
        self.surface = surface
        self.bg_color = pygame.Color('black')
        self.FPS = 60
        self.game_Clock = pygame.time.Clock()

        self.close_clicked = False
        self.continue_game = True

        self.a = 'image1.bmp'
        self.b = 'image2.bmp'
        self.c = 'image3.bmp'
        self.d = 'image4.bmp'
        self.e = 'image5.bmp'
        self.f = 'image6.bmp'
        self.g = 'image7.bmp'
        self.h = 'image8.bmp'
        self.pic_list = [self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h]
        self.pic_list = self.pic_list * 2

        self.pic = []
        self.board_size = 4
        self.board = []

        self.create_pic()
        self.create_tile()

    def create_pic(self):
        # load pictures into a list
        for item in self.pic_list:
            self.picture = pygame.image.load(item)
            self.pic.append(self.picture)
            random.shuffle(self.pic)

    def create_tile(self):
        width = self.picture.get_width()
        height = self.picture.get_height()
        for row_index in range(0, self.board_size):
            row = []
            for col_index in range(0, self.board_size):
                x = col_index * width
                y = row_index * height
                image_index = row_index * 4 + col_index
                a_tile = Tile(x, y, width, height, self.pic[image_index], self.surface)
                row.append(a_tile)
            self.board.append(row)

    def play(self):
        # Play the game until the player presses the close box.
        # - self is the Game that should be continued or not.
        while not self.close_clicked:  # until player clicks close box
            # play frame
            self.handle_events()
            self.draw()
            if self.continue_game:
                self.update()
                self.decide_continue()
            self.game_Clock.tick(self.FPS)  # run at most with FPS Frames Per Second

    def handle_events(self):
        # Handle each user event by changing the game state appropriately.
        # - self is the Game whose events will be handled
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.close_clicked = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.handle_mouse_up(event.pos)  # event.pos is (x,y) coordinates of the click

    def handle_mouse_up(self, position):
        # position is bound to whatever event.pos is bound to

        pass

    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw
        self.surface.fill(self.bg_color)  # clear the display surface first
        # drawing of the board
        for row in self.board:
            for tile in row:
                tile.draw_tile()
        pygame.display.update()  # make the updated surface appear on the display

    def update(self):
        # Update the game objects for the next frame.
        # - self is the Game to update

        pass

    def decide_continue(self):
        # Check and remember if the game should continue
        # - self is the Game to check

        pass


class Tile:
    fg_color = pygame.Color('black')
    border_width = 4

    def __init__(self, x, y, width, height, picture, surface):
        # Initialize a Tile.
        # - self is the Tile to initialize
        # - x,y top left coordinates of the rectangle
        # - - width, height are the dimensions of the rectangle
        # Instance Attributes or Object Attributes
        self.rect = pygame.Rect(x, y, width, height)
        self.surface = surface
        self.pic = picture
        self.location = (x, y)

    def draw_tile(self):
        self.surface.blit(self.pic, self.location)
        pygame.draw.rect(self.surface, Tile.fg_color, self.rect, Tile.border_width)


main()
