# Imports
import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    # Overall class to manage game assets and behavior

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def _check_events(self):
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
        # Update images on screen, and flip to new screen
        # Redraw background color during the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            pygame.display.flip()

    def run_game(self):
        # Start main loop for game
        while True:
            # Events method
            self._check_events()
            self._update_screen()

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
