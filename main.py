
import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score
from writetext import Text
from button import Button



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
    Start_msg = Text(30)


    #-----------------------#
    resume_img = pygame.image.load('Asteroids/Assets/CONTINUE.png').convert_alpha()
    quit_img = pygame.image.load('Asteroids/Assets/Quit.png').convert_alpha()

    resume_button = Button(490,260,resume_img,1)
    quit_button = Button(490, 360, quit_img, 1)

    game_paused = False

    while True : 
        
        # Close Program / Pause Program
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                     game_paused = not game_paused
            if event.type == pygame.QUIT:
                return
           
        # Update and check for value    
        
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

        # if Game is Paused 
        if game_paused == True :
            if resume_button.draw(screen) :
                game_paused = False
            if quit_button.draw(screen):
                return
        else :
            updateable.update(dt)
        
        # Screen Draw

        score.write(screen)
        Start_msg.write(screen, "ASTEROID", 585, 600)
        Start_msg.write(screen, "Press [Return] to pause", 535, 640)

        for obj in drawable :
            obj.draw(screen)
        
        pygame.display.flip()

        # Limit Frame rate to 60 FPS
        dt = clock.tick(60)/1000
        

if __name__ == "__main__":
    main()
