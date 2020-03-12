import pygame
from Ball import Ball
import os

os.environ["SDL_VIDEO_WINDOW_POS"] = "15,30"
pygame.display.init()
size = 900,600
screen = pygame.display.set_mode(size)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
