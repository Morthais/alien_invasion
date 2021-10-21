"""
This is the main file for the alien invasion video game built using PyGame.
"""
# import packages
import sys      # sys is used to exit the game when the player quits
import pygame   # pygame contains the functionality needed to make a game

def run_game():
    # initialize game and create a screen object
    pygame.init()   # initializes background settings
    screen = pygame.display.set_mode((1200, 800))   # creates a display window called "screen" which is a surface
    pygame.display.set_caption("Alien Invasion")

    # start the main loop for the game
    while True:

        # watch for keyboard and mouse events (as declared by pygame.event.get())
        for event in pygame.event.get():    # this is an event loop
            if event.type == pygame.QUIT:   # which listens for an event
                sys.exit()                  # and does a task if the event occurs

        # make the most recently drawn screen visible
        pygame.display.flip()   # draws an empty screen in this case

run_game()