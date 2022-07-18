#
# CMPUT 174
# Lab 3 Pong version 1
#
# First name: Yi
# Last name: Yang
# Lab section: H04
#
# Description: This is version 1 of the Pong program
#
#

import pygame


# User-defined functions

def main():
    # initialize all pygame modules (some need initialization)
    pygame.init()
    # create a pygame display window
    pygame.display.set_mode((500, 400))
    # set the title of the display window
    pygame.display.set_caption('Pong')
    # get the display surface
    surface = pygame.display.get_surface()
    game = Game(surface)
    game.play()
    pygame.quit()


# User-defined classes

class Game:
    def __init__(self, surface):

        self.surface = surface
        self.bg_color = pygame.Color('black')

        self.FPS = 60
        self.game_Clock = pygame.time.Clock()
        self.close_clicked = False
        self.continue_game = True

        # Dot attributes
        self.dot = Ball('white', 5, [250, 200], [4, 2], self.surface)

        # Rectangle attributes
        self.rect1 = Paddle('white', [105, 180, 10, 40], self.surface)
        self.rect2 = Paddle('white', [395, 180, 10, 40], self.surface)

    def play(self):
        # Main while loop
        while not self.close_clicked:  # until player clicks close box
            # 1. handle events
            self.handle_events()
            # 2. DRAW
            self.draw()
            if self.continue_game:
                # 3. UPDATE - moving the dot
                self.update()
                # 4. decide_continue ?????
                self.decide_continue()
            self.game_Clock.tick(self.FPS)  # run at most with FPS Frames Per Second

    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.close_clicked = True  # the window is now closed

    def draw(self):
        # Draw all game objects.
        self.surface.fill(self.bg_color)
        self.dot.draw()
        self.rect1.draw()
        self.rect2.draw()

        pygame.display.update()  # make the updated surface appear on the display

    def update(self):
        # Update the game objects for the next frame.
        self.dot.move()

    def decide_continue(self):
        # Check and remember if the game should continue
        pass


class Ball:
    def __init__(self, dot_color, dot_radius, dot_center, dot_velocity, surface):
        # Initialize a Dot.
        self.color = pygame.Color(dot_color)
        self.radius = dot_radius
        self.center = dot_center
        self.velocity = dot_velocity
        self.surface = surface

    def move(self):
        size = self.surface.get_size()  # size is a tuple (width,height)
        for i in range(0, 2):
            self.center[i] = (self.center[i] + self.velocity[i])
            if self.center[i] <= self.radius:  # left edge and top edge
                self.velocity[i] = -self.velocity[i]
            if self.center[i] + self.radius >= size[i]:  # right edge or bottom
                self.velocity[i] = -self.velocity[i]

    def draw(self):
        # Draw the dot on the surface
        # - self is the Dot

        pygame.draw.circle(self.surface, self.color, self.center, self.radius)


class Paddle:
    def __init__(self, rect_color, center_size, surface):
        # Initialize a Rectangle.
        self.color = pygame.Color(rect_color)
        self.rect = center_size
        self.surface = surface

    def move(self):

        pass

    def draw(self):
        # Draw the Rectangle on the surface
        # - self is the Rectangle

        pygame.draw.rect(self.surface, self.color, self.rect)


main()
