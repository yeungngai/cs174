

import pygame


class Tile:
    def __init__(self, x, y, image, cover):
        self.image = image
        self.cover = cover
        self.rect = pygame.Rect(x, y, 60, 60)
        self.covered = True

    def draw(self, screen):
        # draw cover or image
        if self.covered:
            screen.blit(self.cover, self.rect)
        else:
            screen.blit(self.image, self.rect)

    def handle_event(self, event):
        # check left button click
        if event.type == pygame.MOUSEBUTTONDOWN:
            # check position
            if self.rect.collidepoint(event.pos):
                self.covered = False


pygame.init()

screen = pygame.display.set_mode((550, 550))

# create images
img = pygame.image.load('image1.bmp')

cov = pygame.image.load('image0.bmp')

# create tiles
tiles = []
for y in range(5):
    for x in range(5):
        tiles.append(Tile(x * 110, y * 110, img, cov))

# mainloop
clock = pygame.time.Clock()
running = True

while running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        for x in tiles:
            x.handle_event(event)
    print(tiles)

    # draws
    for x in tiles:
        x.draw(screen)

    pygame.display.flip()

    # clock
    clock.tick(25)

pygame.quit()
