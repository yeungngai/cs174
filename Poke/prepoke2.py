import pygame


def main():
    # Initialize pygame
    pygame.init()

    # create window
    window_size = (500, 400)
    pygame.display.set_mode(window_size)

    # set the window title
    pygame.display.set_caption('Example Pygame Program')

    # get the surface of the window
    surface = pygame.display.get_surface()
    game = Game(surface)
    game.play()
    pygame.quit()


class Game:
    def __init__(self, surface):
        self.surface = surface

        # Set the attributes
        self.close_clicked = False  # the window is open
        self.continue_game = True  # the game is running
        self.frames_per_second = 60
        self.game_clock = pygame.time.Clock()
        self.bg_color = pygame.Color('black')
        self.frames = 0  # identifier used in example end of game condition

        # DOT Attributes - specific to the Game
        self.dot1 = Dot(pygame.Color('red'), [50, 150], 30, [1, 2], surface)
        self.dot2 = Dot(pygame.Color('blue'), [200, 100], 40, [2, 1], surface)

    def play(self):
        # MAIN WHILE LOOP
        while self.close_clicked == False:  # window is still open

            # 1. handle events
            self.handle_events()

            # 2. DRAW
            self.draw()
            if self.continue_game == True:

                # 3. UPDATE - moving the dot
                self.update()

                # 4. decide_continue ?????
                self.decide_continue()
            self.frames = self.frames + 1  # this is done for sample end of game condition
            self.game_clock.tick(self.frames_per_second)

    def handle_events(self):
        list_of_events = pygame.event.get()
        for event in list_of_events:
            if event.type == pygame.QUIT:
                self.close_clicked = True  # the window is now closed

    def draw(self):
        self.surface.fill(self.bg_color)
        self.dot1.draw()
        self.dot2.draw()
        pygame.display.update()

    def update(self):
        self.dot1.move()
        self.dot2.move()

    def decide_continue(self):
        if self.frames > 100:  # example condition
            self.continue_game = False  # game has stopped


class Dot:
    def __init__(self, color, center, radius, velocity, surface):
        self.color = color
        self.center = center
        self.radius = radius
        self.velocity = velocity
        self.surface = surface

    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)

    def move(self):
        for index in range(0, 2):
            self.center[index] = self.center[index] + self.velocity[index]


main()


