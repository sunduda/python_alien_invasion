import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Inherit from pygame class Sprite """
    def __init__(self, game_settings, screen, ship):
        super().__init__()
        self.screen = screen
        self.width = game_settings.bullet_width
        self.height = game_settings.bullet_height
        self.colour = game_settings.bullet_colour
        self.speed_factor = game_settings.bullet_speed_factor
        # Draw a rectangle representing the bullet at (0,0)
        # Correctly position the bullet
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # Store the position of the bullet in floating number
        self.y = float(self.rect.y)

    def update(self):
        # Move the bullet upwards
        self.y -= self.speed_factor
        self.rect.y = self.y
        # Draw the bullet on the screen
        pygame.draw.rect(self.screen, self.colour, self.rect)

    def hit_the_target(self, aliens, player_score):
        # Check if the bullet hits (an) alien(s)
        bullet_consumed = False
        for alien in aliens.sprites():
            if (self.rect.top < alien.rect.bottom and \
                    self.rect.bottom > alien.rect.bottom) and \
                    (self.rect.left < alien.rect.right and \
                    self.rect.right > alien.rect.left):
                player_score.update(alien)
                aliens.remove(alien)
                bullet_consumed = True
        return bullet_consumed, aliens
