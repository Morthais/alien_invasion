import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/starship resized.bmp')   # load ship image
        self.rect = self.image.get_rect()                       # get the rectangle of the ship image
        self.screen_rect = screen.get_rect()                    # get the rectangle of the screen

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx            # set the centerx of screen rectangle to the centerx of the ship image
        self.rect.bottom = self.screen_rect.bottom              # set the bottom of the screen rectangle to the bottom of the ship image

        # store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # movement flags
        self.moving_right = False                               # we set False because we don't want the ship to move right by default
        self.moving_left = False                                # we set False because we don't want the ship to move left by default
        # self.moving_up = False                                  # we set False because we don't want the ship to move up by default
        # self.moving_down = False                                # we set False because we don't want the ship to move down by default

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left  and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # if self.moving_up:
        #     self.rect.centery -= 1
        # if self.moving_down:
        #     self.rect.centery += 1

        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)