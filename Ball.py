import pygame
import random
from numpy import sin, cos

class Ball:
    def __init__(self, screen, pos, vel):
        self.screen = screen
        self.pos = pos
        self.vel = vel
        self.r = 10

    def collide(self, size, grid, paddle = None):
        self.collidewalls(size)
        self.collidegrid(grid)
        self.collidepaddle(paddle)

    def collidewalls(self, size):
        if self.pos[0] - self.r < 0 or self.pos[0] + self.r > size[0]:
            self.vel = (-self.vel[0], self.vel[1])
        if self.pos[1] - self.r < 0 or self.pos[1] + self.r > size[1]:
            self.vel = (self.vel[0], -self.vel[1])

    def collidegrid(self, grid):
        bounced = False
        for i, line in enumerate(grid.blocks):
            if bounced: break
            for j, block in enumerate(line):
                if block:
                    if self.pos[0] + self.r >= j * grid.width and self.pos[0] - self.r <= (j + 1) * grid.width: # if x coord is in block
                        if self.pos[1] - self.r < (i+1) * grid.height and self.pos[1] - self.r < (i+1) * grid.height:
                            self.vel = (self.vel[0], -self.vel[1])
                            grid.blocks[i][j] = False
                            bounced = True
                            break

    def collidepaddle(self, paddle):
        if self.pos[0] + self.r > paddle.pos[0] and self.pos[0] - self.r < paddle.pos[0] + paddle.length: #inside x
            if self.pos[1] + self.r > paddle.pos[1] and self.pos[1] - self.r < paddle.pos[1] + paddle.height: #inside y
                self.vel = (self.vel[0] + paddle.vel[0]/15, -self.vel[1])

    def update(self):
        self.pos = (self.pos[0] + self.vel[0], self.pos[1] + self.vel[1])

    def draw(self):
        x,y = self.pos
        x = int(x)
        y = int(y)
        pos = x,y
        pygame.draw.circle(self.screen, (255,255,255), pos, self.r)

    def randomvel(self, scale):
        theta = random.random()*3.14159265
        self.vel = (scale* cos(theta), scale* -sin(theta))
