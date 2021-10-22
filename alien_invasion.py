"""
This is the main module for an alien invasion video game built using PyGame.
Author: Jacob Farr (Morthais)
Credits: "Python Crash Course" by Eric Matthes
"""
# import packages
import sys      # sys is used to exit game when player quits
import pygame   # pygame contains functionality needed to make a game
from settings import Settings   # import Settings class I created from settings.py file/module
from ship import Ship

def run_game():

    # initialize pygame
    pygame.init()

    # initialize settings
    ai_settings = Settings()

    # initialize screen
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))  # set display dimensions
    pygame.display.set_caption("Alien Invasion")                # set display caption

    # Make a ship. Out of the loop because we only want one ship.
    ship = Ship(screen)                                         # pass the screen to draw the ship rectangle on
                                                                # the proper location on the screen surface

    # start the main loop for game
    while True:
        """This is the main loop for alien_invasion"""
        # watch for keyboard and mouse events (as declared by pygame.event.get())
        for event in pygame.event.get():                        # this is an event loop
            if event.type == pygame.QUIT:                       # which listens for an event
                sys.exit()                                      # and does a task if event occurs

        # redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)                       # use the pygame fill module and Settings class to set the background color
        ship.blitme()

        # make the most recently drawn screen visible (to create the illusion of smooth movement)
        pygame.display.flip()                                   # draws an empty screen in this case

run_game()

