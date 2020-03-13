import pygame
from ball import Ball
from grid import Grid
from Paddle import Paddle
import os

def main():
    os.environ["SDL_VIDEO_WINDOW_POS"] = "15,30"
    pygame.display.init()
    size = 900,600
    screen = pygame.display.set_mode(size)
    ball = Ball(screen, (size[0]/2,size[1]/4*3), (1,1))
    ball.randomvel(3)
    grid = Grid(screen, size)
    paddle = Paddle(screen, size, (size[0]/2, size[1]/10 * 9))
    running = True
    pygame.key.set_repeat(40)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    paddle.move(-15)
                elif event.key == pygame.K_RIGHT:
                    paddle.move(15)
        screen.fill((0,0,0))
        grid.draw()
        ball.update()
        ball.collide(size, grid)
        ball.draw()
        paddle.update()
        paddle.draw()
        pygame.display.update()

if __name__ == "__main__":
    main()
