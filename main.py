import pygame
from ball import Ball
import os

def main():
    os.environ["SDL_VIDEO_WINDOW_POS"] = "15,30"
    pygame.display.init()
    size = 900,600
    screen = pygame.display.set_mode(size)
    ball = Ball(screen, (size[0]/2,size[1]/2), (0.5,0.5))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0,0,0))
        ball.update()
        ball.collide(size)
        ball.draw()
        pygame.display.update()

if __name__ == "__main__":
    main()
