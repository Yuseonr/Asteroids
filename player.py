# 16 July 2025
# Player subclass

import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.speed_mode = 1

    # Draw Triangel

    def triangel(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, 'white', self.triangel(), 2)
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys [pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_a] or keys [pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_s] or keys [pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_d] or keys [pygame.K_RIGHT]:
            self.rotate(dt)

        if keys[pygame.K_1]:
            self.speed_mode = 1
        if keys[pygame.K_2]:
            self.speed_mode = 2
        if keys[pygame.K_3]:
            self.speed_mode = 3

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED*dt

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * self.increase_mode(self.speed_mode) * dt

    def increase_mode(self,mode):
        if mode == 1:
            return PLAYER_SPEED * 1
        elif mode == 2:
            return PLAYER_SPEED * 2
        elif mode == 3:
            return PLAYER_SPEED * 5
