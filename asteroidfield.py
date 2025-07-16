import pygame
import random
from asteroid import Asteroid
from constants import *

class AsteroidField(pygame.sprite.Sprite):

    edges = [

        # Spawn from the left side, looking to the right side 
        [ 
            pygame.Vector2(1,0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT)
        ],

        # Spawn from the right side, looking to the left side
        [
            pygame.Vector2(-1,0),
            lambda y: pygame.Vector2(SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT)
        ],

        # Spawn from the bottom side, looking up / to the upside
        [
            pygame.Vector2(0,1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH,-ASTEROID_MAX_RADIUS)
        ],

        # Spawn from the top side, looking down / to the bottom
        [
            pygame.Vector2(0,-1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, ASTEROID_MAX_RADIUS + SCREEN_HEIGHT)
        ]

 # Each edge has a direction vector and a lambda function that calculates spawn positions just off-screen

    ]

    def __init__(self):
        # Initializes the sprite with its containers and sets up a timer to track when to spawn the next asteroid.
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.spawn_timer = 0
    
    def spawn(self, radius, position, velocity):
        # Creates a new asteroid at the given position with the specified radius and velocity.
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity
    
    def update(self,dt):
        # Timer for spawning new Asteroid
        self.spawn_timer+=dt 
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0
        
            # Spawning new Asteroid at random edges
            edge = random.choice(self.edges)                             # Asteroid Spawn location
            speed = random.randint(40,100)                               # Asteroid speed
            velocity = edge[0] * speed                                   # Calc Asteroid Velocity, by: pygame.Vector2(1,0) <- updating this value 
            velocity = velocity.rotate(random.randint(-30, 30))          # Add slight rotation to Asteroid trejectory for variant
            position = edge[1](random.uniform(0,1))                      # Calls the lambda function with a random value (0-1) to get spawn position
            kind = random.randint(1,ASTEROID_KINDS)                      # Pick Asteroid kind
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)   # Spawn Asteroid




       


        
