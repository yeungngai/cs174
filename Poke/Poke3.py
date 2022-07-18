# Poke Version 3 PLUS EXAMPLE OF USING KEYUP AND KEYDOWN events
# Major Tasks --- > changes the color of the ball when a key is pressed
# start of the game
# Based on Code Example 2.py and poke1.py
import pygame
import random
import math


class Dot:
    def __init__(self, color, center, radius, velocity, surface):
        # initializes the instance attributes of the Dot object
        self.color = color
        self.center = center
        self.radius = radius
        self.velocity = velocity
        self.surface = surface

    def set_color(self, new_color):
        self.color = new_color

    def set_radius(self, new_radius):
        if new_radius > 0:
            self.radius = new_radius

    def draw(self):
        # draws the Dot object
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)

    def randomize(self):
        # randomizes the center of the Dot object
        width = self.surface.get_width()
        height = self.surface.get_height()
        self.center[0] = random.randint(self.radius, width - self.radius)
        self.center[1] = random.randint(self.radius, height - self.radius)

    def collide(self, other_dot):
        distance_x = self.center[0] - other_dot.center[0]
        distance_y = self.center[1] - other_dot.center[1]
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
        # if distance < self.radius + other_dot.radius:
        #    return True
        # else:
        #    return False
        return distance < self.radius + other_dot.radius

    def move(self):
        # moves the Dot object by changing its center by the value of velcoity
        # self.center[0] = self.center[0] + self.velocity[0]
        # self.center[1] = self.center[1] + self.velocity[1]
        size = self.surface.get_size()  # size is a tuple (width,height)
        for index in range(0, 2):
            self.center[index] = self.center[index] + self.velocity[index]
            if self.center[index] < self.radius:  # left or top
                self.velocity[index] = -self.velocity[index]  # bounce the dot
            if self.center[index] + self.radius > size[index]:  # right of bottom
                self.velocity[index] = -self.velocity[index]  # bounce the dot


class Game:
    def __init__(self, surface):
        # Attributes that should be in every graphical game
        self.close_clicked = False
        self.continue_game = True
        self.game_clock = pygame.time.Clock()
        self.frames_per_second = 60
        self.surface = surface
        self.bg_color = pygame.Color('black')
        # Attributes that are specific to the game
        self.score = 0
        self.create_dots()

    def create_dots(self):
        self.small_dot = Dot(pygame.Color('red'), [50, 50], 30, [1, 2], self.surface)
        self.big_dot = Dot(pygame.Color('blue'), [200, 100], 40, [2, 1], self.surface)
        self.small_dot.randomize()
        self.big_dot.randomize()
        while self.small_dot.collide(self.big_dot):
            self.small_dot.randomize()
            self.big_dot.randomize()

    def play(self):
        while self.close_clicked == False:
            self.handle_events()
            self.draw()
            if self.continue_game == True:
                self.update()
                self.decide_continue()
            self.game_clock.tick(self.frames_per_second)

    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.close_clicked = True
            if event.type == pygame.MOUSEBUTTONUP and self.continue_game:
                self.small_dot.randomize()
                self.big_dot.randomize()
            if event.type == pygame.KEYDOWN and self.continue_game:
                self.handle_key_down(event)
            if event.type == pygame.KEYUP and self.continue_game:
                self.handle_key_up(event)

    def handle_key_up(self, event):
        if event.key == pygame.K_a:
            self.small_dot.set_color(pygame.Color('red'))
            self.big_dot.set_color(pygame.Color('blue'))

    def handle_key_down(self, event):
        if event.key == pygame.K_a:
            # INCORRECt self.small_dot.color =pygame.Color('orange')
            # INCORRECT self.big_dot.color = pygame.Color('green')
            # INSTEAD
            self.small_dot.set_color(pygame.Color('orange'))
            self.big_dot.set_color(pygame.Color('green'))

    def draw(self):
        self.surface.fill(self.bg_color)
        self.small_dot.draw()
        self.big_dot.draw()
        # draw the score
        self.draw_score()
        if self.continue_game == False:
            self.draw_game_over()
        pygame.display.update()

    def draw_game_over(self):
        # Follow the 5 steps to draw Game Over
        fg_color = pygame.Color('red')
        bg_color = pygame.Color('blue')
        font = pygame.font.SysFont('', 100)
        text_box = font.render('Game Over', True, fg_color, bg_color)
        surface_height = self.surface.get_height()
        text_box_height = text_box.get_height()
        location = (0, surface_height - text_box_height)
        self.surface.blit(text_box, location)

    def draw_score(self):
        # 1. Set the color
        fg_color = pygame.Color('white')
        # 2.create the font object
        font = pygame.font.SysFont('', 70)
        # 3 Create a text box by rendering the font
        text_string = 'Score:' + str(self.score)
        text_box = font.render(text_string, True, fg_color, self.bg_color)
        # 4 Compute the location of the text box
        location = (0, 0)
        # 5 Blit or pin the text box on the surface
        self.surface.blit(text_box, location)

    def update(self):
        self.small_dot.move()
        self.big_dot.move()
        self.score = pygame.time.get_ticks() // 1000

    def decide_continue(self):
        # the game ends when the dots collide
        if self.small_dot.collide(self.big_dot):
            self.continue_game = False


def main():
    # Step 1Initialize pygame
    pygame.init()
    # Ste 2 create a graphical display and set the caption
    size = (500, 400)
    title = 'Poke The Dots'
    pygame.display.set_mode(size)
    pygame.display.set_caption(title)
    # Step 3 get window's surface
    w_surface = pygame.display.get_surface()
    # Step 4 Create Game object
    game = Game(w_surface)
    game.play()
    pygame.quit()


main()


