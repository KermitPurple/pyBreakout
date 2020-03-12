import pygame
from ball import Ball
import os

def main():
    os.environ["SDL_VIDEO_WINDOW_POS"] = "15,30"
    pygame.display.init()
    size = 900,600
    screen = pygame.display.set_mode(size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    main()
