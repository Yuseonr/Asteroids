# 16 July 2025
# Circle Shape Class

import pygame

# Game base 0bject class

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius
    
    def draw(self, screen):
        pass

    def update(self, screen):
        pass

    def collisions(self, circle):
        distance = self.position.distance_to(circle.position)
        return (self.radius + circle.radius) > distance