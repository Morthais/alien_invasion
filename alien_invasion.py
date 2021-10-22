"""
This is the main file for the alien invasion video game built using PyGame.
"""
# import packages
import sys      # sys is used to exit game when player quits
import pygame   # pygame contains functionality needed to make a game
from settings import Settings   # import Settings class I created from settings.py file/module

def run_game():
    # initialize pygame, settings, and screen object
    pygame.init()   # initialize pygame
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))   # use pygame display module and Settings class to set screen dimensions
    pygame.display.set_caption("Alien Invasion")    # use pygame display module to set a caption

    bg_color = (230, 230, 230)  # store a color to fill screen background

    # start the main loop for game
    while True:

        # watch for keyboard and mouse events (as declared by pygame.event.get())
        for event in pygame.event.get():    # this is an event loop
            if event.type == pygame.QUIT:   # which listens for an event
                sys.exit()                  # and does a task if event occurs

        screen.fill(ai_settings.br_color)   # use the pygame fill module and Settings class to set the background color

        # make the most recently drawn screen visible (to create the illusion of smooth movement)
        pygame.display.flip()   # draws an empty screen in this case

run_game()

