import pygame
import random
import math


def main():
    # Initialize pygame
    pygame.init()
    # create window
    window_size = (500, 400)
    pygame.display.set_mode(window_size)
    # set the window title
    pygame.display.set_caption('Poke The Dots')
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
        # SCORE ATTRIBUTE - POKE VERSION @
        self.score = 0
        # Randomiza the Dot objects
        self.dot1.randomize()
        self.dot2.randomize()


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
                # self.frames = self.frames + 1 # this is done for sample end of game condition
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
        # DRAW THE SCORE
        self.draw_score()
        # DRAW THE GAME OVER
        if self.continue_game == False:
            self.draw_game_over()
        pygame.display.update()

    def draw_game_over(self):
        fg = pygame.Color('red')
        bg = pygame.Color('blue')
        font = pygame.font.SysFont('', 100)
        text_box = font.render('Game Over', True, fg, bg)
        x = 0
        y = self.surface.get_height() - text_box.get_height()
        location = (x, y)
        self.surface.blit(text_box, location)

    def draw_score(self):
        # 5 steps
        fg = pygame.Color('white')
        bg = pygame.Color('black')
        font = pygame.font.SysFont('', 70)
        text_box = font.render('Score :' + str(self.score), True, fg, bg)
        # x = self.surface.get_width() - text_box.get_width()
        # y = self.surface.get_height() - text_box.get_height()
        location = (0, 0)
        self.surface.blit(text_box, location)

    def update(self):
        self.dot1.move()
        self.dot2.move()
        self.score = pygame.time.get_ticks() // 1000

    def decide_continue(self):
        if self.dot1.collide(self.dot2):
            self.continue_game = False


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
        size = self.surface.get_size()  # size is a tuple (width,height)
        for index in range(0, 2):
            self.center[index] = self.center[index] + self.velocity[index]
            if self.center[index] <= self.radius:  # left edge and top edge
                self.velocity[index] = -self.velocity[index]
            if self.center[index] + self.radius >= size[index]:  # right edge or bottom
                self.velocity[index] = -self.velocity[index]

    def randomize(self):
        # self.center[0] = random.randint(self.radius,width -self.radius)
        # self.center[1] = random.randint(self.radius,height -self.radius)
        size = self.surface.get_size()  # size is a tuple (width, height)
        for index in range(0, 2):
            self.center[index] = random.randint(self.radius, size[index] - self.radius)

    def collide(self, other_dot):
        # COLLISION
        b = self.center[0] - other_dot.center[0]
        a = self.center[1] - other_dot.center[1]
        c = math.sqrt(a ** 2 + b ** 2)
        if c <= (self.radius + other_dot.radius):
            return True
        else:
            return False


main()



