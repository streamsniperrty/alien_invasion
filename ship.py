import pygame

class Ship:
    # A class to manage the ship.

    def __init__(self, ai_game):
        # Initialize the ship and set starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship and get rectangle
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        # Draw the ship at current location
        self.screen.blit(self.image, self.rect)
