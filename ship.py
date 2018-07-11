import pygame
import pygame.font
from bullet import Bullet

class Ship():
    """ Draw and operate player's ship """
    def __init__(self, game_settings, screen):
        # Initialise the ship
        self.screen = screen

        # Load ship image and get its enclosing rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Put the new ship at the centre-bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Initialise the moving flag
        self.lkey_down = False
        self.rkey_down = False
        self.open_fire = False

        # Game settings related with the ship
        self.settings = game_settings
        self.ammo_amount = float(game_settings.ammo_amount)
        self.ammo_count_update()

        
    def blitme(self):
        """ Draw the ship at the assigned position """
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.ammo_count_image, self.ammo_count_rect)


    def update(self):
        # When keys down flag is True, move the ship right hand until it's released
        if self.lkey_down:
            self.rect.centerx -= self.settings.ship_speed_factor
        elif self.rkey_down:
            self.rect.centerx += self.settings.ship_speed_factor

        # When the ship reaches the screen boundary, stop moving
        if self.rect.right > self.screen_rect.right:
            self.rect.right = self.screen_rect.right
        elif self.rect.left < self.screen_rect.left:
            self.rect.left = self.screen_rect.left

        if self.ammo_amount < self.settings.ammo_capacity:
            self.ammo_amount += self.settings.reload_factor
        if self.ammo_amount > self.settings.ammo_capacity:
            self.ammo_amount = self.settings.ammo_capacity

        self.ammo_count_update()

    def bullet_firing(self, bullets):
        # When firing flag is True, shoot bullets with fixed interval
        fire_interval = self.settings.fire_interval
        if self.open_fire:
            next_bullet = True
            # If the ship just fired a bullet, wait some time to fire again
            for bullet in bullets.sprites():
                if bullet.rect.bottom > self.rect.top - fire_interval:
                    next_bullet = False
                    break
            if next_bullet and self.ammo_amount >= 1:
                abullet = Bullet(self.settings, self.screen, self)
                bullets.add(abullet)
                self.ammo_amount -= 1

    def ammo_count_update(self):
        # Display ammo count at top-left corner
        self.ammo_count_colour = (60, 60, 60)
        self.ammo_count_font = pygame.font.SysFont(None, 48)
        self.ammo_count_image = self.ammo_count_font.render(
                str(int(self.ammo_amount)), True,
                self.ammo_count_colour, self.settings.bg_colour)
        self.ammo_count_rect = self.ammo_count_image.get_rect()
        self.ammo_count_rect.left = self.screen_rect.left + 20
        self.ammo_count_rect.top = 20