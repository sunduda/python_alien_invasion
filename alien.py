import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ Define the enemy aliens """
    def __init__(self, game_settings, screen):
        # Alien initialisation
        super().__init__()
        self.settings = game_settings
        self.screen = screen

        # Load alien image
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Every alien starts at the top-left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height/2

        # Store the accurate position of the alien
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        # Aliens move downwards as a row.
        x_factor = self.settings.fleet_speed_factor
        x_direction = self.settings.fleet_moving_direction
        self.x += self.rect.width*x_factor*x_direction;
        self.rect.x = self.x

    def blitme(self):
        # Draw the alien at designate position
        self.screen.blit(self.image, self.rect)