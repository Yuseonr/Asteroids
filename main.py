# 16 July 2025

import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    while True : 
        # Close Program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updateable.update(dt)

        # Screen Fill

        screen.fill('Black')

        for obj in drawable :
            obj.draw(screen)
        
        for asteroid in asteroids :
           for shot in shots:
                if asteroid.collisions(shot):
                    asteroid.kill()
                    shot.kill()

           if asteroid.collisions(player) :
               print("GAME OVER!")
               sys.exit()
        
        pygame.display.flip()
        

        # Limit Frame rate to 60 FPS
        dt = clock.tick(60)/1000
        

if __name__ == "__main__":
    main()
