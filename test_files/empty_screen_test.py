"""
This is the main module for an alien invasion video game built using PyGame.
Author: Jacob Farr (Morthais)
Credits: "Python Crash Course" by Eric Matthes
"""
# import packages
import pygame   # pygame contains functionality needed to make a game
import functions_test as gf     # import game_functions I created as the alias gf
from settings import Settings   # import Settings class I created from settings.py file/module

def run_game():

    # initialize pygame
    pygame.init()

    # initialize settings
    ai_settings = Settings()

    # initialize screen
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))  # set display dimensions
    pygame.display.set_caption("Alien Invasion")                # set display caption

    # start the main loop for game
    while True:
        """This is the main loop for alien_invasion"""
        gf.check_events()
        gf.update_screen(ai_settings, screen)

run_game()

