import pygame

class Text():
    def __init__(self, size = 24, font=None):
        self.size = size
        self.font = pygame.font.SysFont(font, size)
    
    def write(self, screen, text, x , y, font = None, color = 'White'):
        text = self.font.render(text,True, color )
        screen.blit(text, (x,y))