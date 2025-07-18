
import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score
from writetext import Text


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
    score = Score()
    Start_msg = Text(48)

    while True : 
        # Close Program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update and check for value    
        updateable.update(dt)
        
        for asteroid in asteroids :
           for shot in shots:
                if asteroid.collisions(shot):
                    asteroid.split()
                    shot.kill()
                    score.add_score(asteroid.kind)

           if asteroid.collisions(player) :
               print("GAME OVER!")
               sys.exit()
        
        # Screen Fill 

        screen.fill('Black')

        score.write(screen)
        Start_msg.write(screen, "THIS IS ASTEROID", 500, 500)

        for obj in drawable :
            obj.draw(screen)
        
        pygame.display.flip()

        # Limit Frame rate to 60 FPS
        dt = clock.tick(60)/1000
        

if __name__ == "__main__":
    main()
