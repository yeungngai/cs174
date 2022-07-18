#
# CMPUT 174
# Lab 3 Pong version 3
#
# First name: Yi
# Last name: Yang
# Lab section: H04
#
# Description: This is version 3 of the Pong program
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

        # Objects attributes
        self.dot = Ball('white', 5, [250, 200], [4, 2], self.surface)
        self.rect = Paddle(surface)

        # Score attributes
        self.left_score = 0
        self.right_score = 0

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
        self.paddle_movement()

    def paddle_movement(self):
        pressed = pygame.key.get_pressed()
        if self.continue_game:
            if pressed[pygame.K_q] and Paddle.left_rect.top >= 0:
                Paddle.left_rect.move_ip(0, -6)
            if pressed[pygame.K_a] and Paddle.left_rect.bottom <= 400:
                Paddle.left_rect.move_ip(0, 6)
            if pressed[pygame.K_p] and Paddle.right_rect.top >= 0:
                Paddle.right_rect.move_ip(0, -6)
            if pressed[pygame.K_l] and Paddle.right_rect.bottom <= 400:
                Paddle.right_rect.move_ip(0, 6)

    def draw(self):
        # Draw all game objects.
        self.surface.fill(self.bg_color)
        self.rect.draw()
        self.dot.draw()

        # Draw score
        self.draw_left_score()
        self.draw_right_score()
        pygame.display.update()  # make the updated surface appear on the display

    def draw_left_score(self):
        fg = pygame.Color('white')
        bg = pygame.Color('black')
        font = pygame.font.SysFont('', 80)
        left_text_box = font.render(str(self.left_score), True, fg, bg)
        location_left = (0, 0)
        self.surface.blit(left_text_box, location_left)

    def draw_right_score(self):
        fg = pygame.Color('white')
        bg = pygame.Color('black')
        font = pygame.font.SysFont('', 80)
        right_text_box = font.render(str(self.right_score), True, fg, bg)
        x = self.surface.get_width() - right_text_box.get_width()
        location_right = (x, 0)
        self.surface.blit(right_text_box, location_right)

    def update(self):
        # Update the game objects for the next frame.
        self.dot.move()
        if self.dot.left_collide():
            self.left_score = self.left_score + 1
        if self.dot.right_collide():
            self.right_score = self.right_score + 1

    def decide_continue(self):
        if self.left_score == 11 or self.right_score == 11:
            self.continue_game = False


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
            if self.center[i] <= self.radius or self.center[i] + self.radius >= size[i]:
                self.velocity[i] = -self.velocity[i]
            if self.left_paddle_collision() and self.velocity[0] < 0:
                self.velocity[i] = -self.velocity[i]
            if self.right_paddle_collision() and self.velocity[0] > 0:
                self.velocity[i] = -self.velocity[i]

    def draw(self):
        # Draw the dot and paddles on the surface
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)

    def left_collide(self):
        if self.center[0] <= self.radius:
            return True

    def right_collide(self):
        if self.center[0] + self.radius >= self.surface.get_width():
            return True

    def left_paddle_collision(self):
        if Paddle.left_rect.collidepoint(self.center[0], self.center[1]):
            return True

    def right_paddle_collision(self):
        if Paddle.right_rect.collidepoint(self.center[0], self.center[1]):
            return True


class Paddle:
    rect_color = pygame.Color('white')
    rect_width = 10
    rect_height = 40
    left_rect_x = 105
    left_rect_y = 180
    right_rect_x = 395
    right_rect_y = 180
    left_rect = pygame.Rect(left_rect_x, left_rect_y, rect_width, rect_height)
    right_rect = pygame.Rect(right_rect_x, right_rect_y, rect_width, rect_height)

    def __init__(self, surface):
        # Initialize a Rectangle.
        self.surface = surface

    def draw(self):
        # Draw the Rectangle on the surface
        # - self is the Rectangle
        pygame.draw.rect(self.surface, self.rect_color, self.left_rect)
        pygame.draw.rect(self.surface, self.rect_color, self.right_rect)


main()
