# Disable "Hello from PyGame COmmunity" message
from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
# ---------------------------------------
import pygame
from constants import *


def main():
    pygame.init()
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        # Quits if user clicks exit window button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        pygame.Surface.fill(screen, "black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
