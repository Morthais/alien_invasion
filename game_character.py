import pygame

class Character():

    def __init__(self, screen):
        """Initialize the game character at his starting position."""
        self.screen = screen

        # Load the game character and get its rectangle.
        self.image = pygame.image.load('images/game character resized.bmp') # load game character image
        self.rect = self.image.get_rect()                               # get the rectangle of the game character image
        self.screen_rect = screen.get_rect()                            # get the rectangle of the screen

        # start the game character at the center of the screen
        self.rect.centerx = self.screen_rect.centerx                    # set the centerx of the character to that of the screen
        self.rect.centery = self.screen_rect.centery                    # set the centery of the character to that of the screen

    def blitme(self):
        """Draw the character at its current location"""
        self.screen.blit(self.image, self.rect)