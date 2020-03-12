import pygame

class Ball:
    def __init__(self, screen, pos, vel):
        self.screen = screen
        self.pos = pos
        self.vel = vel
        self.r = 10

    def update(self):
        pass

    def draw(self):
        x,y = self.pos
        x = int(x)
        y = int(y)
        pos = x,y
        pygame.draw.circle(self.screen, (255,255,255), pos, self.r)
