# Disable "Hello from PyGame Community" message
from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

# Run this in order to run the program:
# uv run main.py
# ---------------------------------------
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    
    print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    
    while True:
        # Quits if user clicks exit window button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("black")
        updatable.update(dt)
        
        for item in drawable:
            item.draw(screen)
            
        for a in asteroids:
            if a.collides(player):
                print("GAME OVER!!!")
                return
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()
