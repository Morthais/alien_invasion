import sys      # sys is used to exit the game when player quits
import pygame

def check_keydown_events(event, ship):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
                    
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    """Responds to keypresses and mouse events."""
    # watch for keyboard and mouse events (as declared by pygame.event.get())
    for event in pygame.event.get():                        # this is an event loop
        if event.type == pygame.QUIT:                       # which listens for an event
            sys.exit()                                      # and does a task if event occurs
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, character):
    """Update images on the screen and flip to the new screen."""
    # redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)                       # use the pygame fill module and Settings class to set the background color
    ship.blitme()
    character.blitme()

    # make the most recently drawn screen visible (to create the illusion of smooth movement)
    pygame.display.flip()                                   # draws an empty screen in this case