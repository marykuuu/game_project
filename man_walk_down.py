import sys

import pygame
from pygame.constants import QUIT, K_ESCAPE, KEYDOWN


def my_animation(w1, h1, k, fps, name, position):
    image = pygame.image.load("man_up.png")
    animation_frames = []
    timer = pygame.time.Clock()

    scr = pygame.display.set_mode((800, 800), 0, 32)
    sprite = pygame.image.load("man_up.png".format(name)).convert_alpha()

    width, height = sprite.get_size()
    w, h = width / w1, height / h1
    row = 0
    for j in range(int(height / h)):
        for i in range(int(width / w)):
            animation_frames.append(image.subsurface(pygame.Rect(i * w, row, w, h)))
        row += int(h)

    counter = 0

    while True:
        for evt in pygame.event.get():
            if evt.type == QUIT or (evt.type == KEYDOWN and evt.key == K_ESCAPE):
                sys.exit()
        scr.fill((255, 0, 0))
        scr.blit(animation_frames[counter], position)

        counter = (counter + 1) % k

        pygame.display.update()
        timer.tick(fps)


if __name__ == "__main__":
    my_animation(12, 1, 12, 10, "image", (300, 300))