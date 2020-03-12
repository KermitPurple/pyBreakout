import pygame

class Grid:
    def __init__(self, screen, size):
        self.screen = screen
        self.size = size
        self.scale = (10,10)
        self.block = [[True] * self.scale[0]] * self.scale[1]
        self.width = self.size[0]/self.scale[0]
        self.height = self.size[1]/self.scale[1]/2

    def draw(self):
        colors = [(255,0,0),(255,90,0), (255,230,0), (43, 255, 0), (0,255,255), (0,0,255), (140,0,255),(225,0,255)]
        for i,line in enumerate(self.block):
            for j,block in enumerate(line):
                if block:
                    color = colors[(i + j) % len(colors)]
                    pygame.draw.rect(self.screen, color, pygame.Rect(j * self.width, i * self.height, self.width, self.height))
