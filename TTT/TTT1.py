# TTT Version 1
# Brief Game Description

import pygame


# User-defined functions

def main():
    # initialize all pygame modules (some need initialization)
    pygame.init()
    # create a pygame display window
    pygame.display.set_mode((500, 400))
    # set the title of the display window
    pygame.display.set_caption('Tic Tac Toe')
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

        # === objects that are part of every game that we will discuss
        self.surface = surface
        self.bg_color = pygame.Color('black')

        self.FPS = 60
        self.game_Clock = pygame.time.Clock()
        self.close_clicked = False
        self.continue_game = True

        # === game specific objects
        Tile.set_surface(self.surface)  # this is how you call a class method
        self.board_size
        self.board

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

    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw

        self.surface.fill(self.bg_color)  # clear the display surface first
        # drawing of the board
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
    # An object in this class represents a Tile
    # Shared or Class Attributes
    surface = None
    font_size = 133
    fg_color = pygame.Color('white')
    border_width = 3

    # Whenever we want to initialize or set the value if a class attribute
    # we use a class method for it
    @classmethod
    def set_surface(cls, surface_from_Game):
        cls.surface = pygame.display.get_surface()

    def __init__(self, x, y, width, height):
        # Initialize a Tile.
        # - self is the Tile to initialize
        # - x,y top left coordinates of the rectangle
        # - - width, height are the dimensions of the rectangle
        # Instance Attributes or Object Attributes
        self.rect = pygame.Rect(x, y, width, height)
        self.content = ''

    def draw(self):
        # Draw the dot on the surface
        # - self is the Tile

        pygame.draw.rect(Tile.surface, self.color, self.rect)


main()

