
import pygame
from constants import SCORE_INCREMENT

class Score():
    def __init__(self, size = 24, font=None):
        self.size = size
        self.font = pygame.font.SysFont(font, size)
        self.score = 0

    def show(self,screen) :
        text = self.font.render(f"Score : {self.score}",True,'White' )
        screen.blit(text, (10,10))
        
    def add_score(self, Asteroidkind):
        self.score += (SCORE_INCREMENT * Asteroidkind)

