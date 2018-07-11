import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Inherit from pygame class Sprite """
    def __init__(self, game_settings, screen, ship):
        # Initialise bullet properties
        super().__init__()
        self.screen = screen

        # Draw a rectangle representing the bullet at (0,0)
        # Correctly position the bullet
        self.rect = pygame.Rect(0, 0, game_settings.bullet_width,
                game_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the position of the bullet in floating number
        self.y = float(self.rect.y)
        self.colour = game_settings.bullet_colour
        self.speed_factor = game_settings.bullet_speed_factor

    def update(self):
        """ Move the bullet upwards """
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """ Draw the bullet on the screen """
        pygame.draw.rect(self.screen, self.colour, self.rect)
