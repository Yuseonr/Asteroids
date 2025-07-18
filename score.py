
import pygame
from constants import SCORE_INCREMENT
from writetext import Text

class Score(Text):
    def __init__(self, size=24, font=None):
        super().__init__(size, font)
        self.score = 0
        
    def write(self,screen) :
        super().write(screen,f"Score : {self.score}",10,10)
        
    def add_score(self, Asteroidkind):
        self.score += (SCORE_INCREMENT * Asteroidkind)

