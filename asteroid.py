# 16 July 2025
# Asteroid Subclass

import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_SPLIT_SPEED_MULTIPLAYER
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.kind = round(radius/20)

    def draw(self, screen):
        pygame.draw.circle(screen,'white',self.position,self.radius,2)
    
    def update(self, dt):
        self.position += self.velocity*dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        vel1 = self.velocity.rotate(angle)
        vel2 = self.velocity.rotate(-angle)
        self.radius -= ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, self.radius)
        asteroid1.velocity = vel1 * ASTEROID_SPLIT_SPEED_MULTIPLAYER
        asteroid2 = Asteroid(self.position.x, self.position.y, self.radius)
        asteroid2.velocity = vel2 * ASTEROID_SPLIT_SPEED_MULTIPLAYER

        
