import sys      # sys is used to exit the game when player quits
import pygame

def check_events():
    """Responds to keypresses and mouse events."""
    # watch for keyboard and mouse events (as declared by pygame.event.get())
    for event in pygame.event.get():                        # this is an event loop
        if event.type == pygame.QUIT:                       # which listens for an event
            sys.exit()                                      # and does a task if event occurs

def update_screen(ai_settings, screen, ship, character):
    """Update images on the screen and flip to the new screen."""
    # redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)                       # use the pygame fill module and Settings class to set the background color
    ship.blitme()
    character.blitme()

    # make the most recently drawn screen visible (to create the illusion of smooth movement)
    pygame.display.flip()                                   # draws an empty screen in this case