# TTT Version 2
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

        self.FPS = 70
        self.game_Clock = pygame.time.Clock()
        self.close_clicked = False
        self.continue_game = True

        # === game specific objects
        Tile.set_surface(self.surface)  # this is how you call a class method
        self.player_1 = 'X'
        self.player_2 = 'O'
        self.turn = self.player_1
        self.board_size = 3
        self.board = []
        self.create_board()

    def create_board(self):
        a = self.surface.get_width()
        b = self.surface.get_height()
        width = a // 3
        height = b // 3
        for row_index in range(0, self.board_size):
            row = []
            for col_index in range(0, self.board_size):
                # item = (row_index,col_index)
                # game = Game(), dot1 = Dot(), student = Student()
                x = width * col_index
                y = height * row_index
                a_tile = Tile(x, y, width, height)
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
        for row in self.board:
            for tile in row:
                if tile.select(position, self.turn) == True:  # select returns True or False
                    self.change_turn()

    def change_turn(self):
        if self.turn == self.player_1:  # Was it the X player's turn
            self.turn = self.player_2  # Change turn to O plater
        else:
            self.turn = self.player_1

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
    # An object in this class represents a Tile
    # Shared or Class Attributes
    surface = None
    font_size = 150
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
        self.flashing = False

    def draw_tile(self):
        # Draw the dot on the surface
        # - self is the Tile
        if self.flashing == True:
            # draw the white rectangle
            pygame.draw.rect(Tile.surface, Tile.fg_color, self.rect, 0)
            self.flashing = False
        else:
            # draw the black rectangle with the white border and draw gte content
            pygame.draw.rect(Tile.surface, Tile.fg_color, self.rect, Tile.border_width)
            self.draw_content()

    def select(self, position, turn):
        # position is a tuple (x,y) coordinates of the click
        # turn is eith X or O
        # returns True or False
        valid_click = False
        if self.rect.collidepoint(position):  # click
            if self.content == '':  # there has been a click inside an unoccupied tile
                self.content = turn
                valid_click = True
            else:
                self.flashing = True
        return valid_click

    def draw_content(self):
        # 5 steps to draw text on the graphical window
        # 1. color- Tile.fg_color
        # 2. create a font object
        font = pygame.font.SysFont('', Tile.font_size)
        # 3. Create a text box
        text_box = font.render(self.content, True, Tile.fg_color)
        text_box_width = text_box.get_width()
        text_box_height = text_box.get_height()
        # 4. Compute the location
        d_x = (self.rect.width - text_box_width) // 2
        d_y = (self.rect.height - text_box_height) // 2
        x = self.rect.x + d_x
        y = self.rect.y + d_y
        location = (x, y)
        # 5 pin/blit the text_box on the surface
        Tile.surface.blit(text_box, location)


main()


