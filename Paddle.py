import pygame

class Paddle:
    def __init__(self, screen, size, pos):
        self.length = 175
        self.height = 20
        self.screen = screen
        self.size = size
        self.pos = (pos[0] - self.length/2, pos[1])
        self.vel = (0,0)

    def draw(self):
        rect = pygame.Rect(int(self.pos[0]), int(self.pos[1]), self.length, self.height)
        pygame.draw.rect(self.screen, (255,255,255), rect)
        
    def update(self):
        self.pos = (self.pos[0] + self.vel[0], self.pos[1] + self.vel[1])
        self.vel = (0,0)

    def move(self, delta):
        if self.pos[0] + delta >= 0 and self.pos[0] + delta + self.length <= self.size[0]:
            self.vel = (delta, self.vel[1])
