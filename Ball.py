import pygame

class Ball:
    def __init__(self, screen, pos, vel):
        self.screen = screen
        self.pos = pos
        self.vel = vel
        self.r = 10

    def collide(self, size, grid = None, paddle = None):
        if self.pos[0] - self.r < 0 or self.pos[0] + self.r > size[0]:
            self.vel = (-self.vel[0], self.vel[1])
        if self.pos[1] - self.r < 0 or self.pos[1] + self.r > size[1]:
            self.vel = (self.vel[0], -self.vel[1])

    def update(self):
        self.pos = (self.pos[0] + self.vel[0], self.pos[1] + self.vel[1])

    def draw(self):
        x,y = self.pos
        x = int(x)
        y = int(y)
        pos = x,y
        pygame.draw.circle(self.screen, (255,255,255), pos, self.r)
