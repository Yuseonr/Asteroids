
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
    Menu_msg = Text(48)


    #-----------------------#
    resume_img = pygame.image.load('Asteroids/Assets/CONTINUE.png').convert_alpha()
    quit_img = pygame.image.load('Asteroids/Assets/Quit.png').convert_alpha()
    Start_img = pygame.image.load('Asteroids/Assets/Start.png').convert_alpha()
    Game_over_img = pygame.image.load('Asteroids/Assets/Game_over.png').convert_alpha()

    resume_button = Button(490,260,resume_img,1)
    quit_button = Button(490, 360, quit_img, 1)
    start_button = Button(490, 310, Start_img,1)
    game_over_button = Button(490, 310, Game_over_img,1)

    game_paused = False
    game_menu = True
    game_over = False
    #-----------------------#

    while True : 

        # Close Program / Pause Program
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                        game_paused = not game_paused
            if event.type == pygame.QUIT:
                return
            
        # Update and check for value    
        if game_menu == False and not game_over:
            for asteroid in asteroids :
                for shot in shots:
                    if asteroid.collisions(shot):
                        asteroid.split()
                        shot.kill()
                        score.add_score(asteroid.kind)

                if asteroid.collisions(player) :
                    game_over = True
        
        # Screen Fill & Screen Update
        screen.fill('Black')
        if game_paused == False and not game_over:
                updateable.update(dt)

        # Menu
        if game_menu == True and not game_over :
            Menu_msg.write(screen, 'WELCOME TO ASTEROID ! !', 420,500)
            for asteroid in asteroids :
                asteroid.draw(screen)
            if start_button.draw(screen) :
                game_menu = False
                for asteroid in asteroids :
                    asteroid.kill()

        elif game_menu == False and not game_over :
            # Screen Draw
            score.write(screen)
            Start_msg.write(screen, "ASTEROID", 585, 600)

            for obj in drawable :
                obj.draw(screen)    

            # if Game is Paused 
            if game_paused == True :
                if resume_button.draw(screen) :
                    game_paused = False

                Start_msg.write(screen, "Press [Return] to unpause", 535, 640)

                if quit_button.draw(screen):
                    return
            else :
                Start_msg.write(screen, "Press [Return] to pause", 535, 640)

        # Game Over        
        else :
            Start_msg.write(screen, f"YOUR SCORE : {score.score}", 555, 600)
    
            if score.high_score(score) :
                Start_msg.write(screen, "NEW HIGHSCORE !", 545, 640)
            for asteroid in asteroids :
                asteroid.draw(screen)
            if game_over_button.draw(screen) :
                game_over = False
                game_menu = True
                score.score = 0
            
            
        pygame.display.flip()

        # Limit Frame rate to 60 FPS
        dt = clock.tick(60)/1000
    

if __name__ == "__main__":
    main()
