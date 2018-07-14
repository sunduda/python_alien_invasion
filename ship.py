import pygame
import pygame.font
from bullet import Bullet

class Ship():
    """ Draw and operate player's ship """
    def __init__(self, game_settings, screen):
        self.screen = screen
        self.ship_reset(game_settings)
        # Initialise the moving flag
        self.lkey_down = False
        self.rkey_down = False
        self.open_fire = False

        self.ammo_update()
    
    def ship_reset(self, game_settings):
        # Game settings related with the ship
        self.speed_factor = game_settings.ship_speed_factor
        self.ammo_capacity = game_settings.ammo_capacity
        self.ammo_amount = float(game_settings.ammo_amount)
        self.reload_factor = game_settings.reload_factor
        self.fire_interval = game_settings.fire_interval
        self.ammo_count_bg_colour = game_settings.bg_colour
        # Load ship image and get its enclosing rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Put the new ship at the centre-bottom of the screen
        self.rect.centerx = self.screen.get_rect().centerx
        self.rect.bottom = self.screen.get_rect().bottom
        # Player's ship starts from level 1
        self.level = 1
        
    def blitme(self):
        # Draw the ship at the assigned position
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.ammo_count_image, self.ammo_count_rect)


    def update(self):
        # When keys down flag is True, move the ship right hand until it's released
        if self.lkey_down:
            self.rect.centerx -= self.speed_factor
        elif self.rkey_down:
            self.rect.centerx += self.speed_factor
        # When the ship reaches the screen boundary, stop moving
        if self.rect.right > self.screen.get_rect().right:
            self.rect.right = self.screen.get_rect().right
        elif self.rect.left < self.screen.get_rect().left:
            self.rect.left = self.screen.get_rect().left

        self.ammo_update()

    def bullet_firing(self, game_settings, bullets):
        # When firing flag is True, shoot bullets with fixed interval
        next_bullet = False
        if self.open_fire:
            next_bullet = True
            # If the ship just fired a bullet, wait some time to fire again
            for bullet in bullets.sprites():
                if bullet.rect.bottom > self.rect.top - self.fire_interval:
                    next_bullet = False
                    break
            if next_bullet and self.ammo_amount >= 1:
                abullet = Bullet(game_settings, self.screen, self)
                bullets.add(abullet)
                self.ammo_amount -= 1

    def ammo_update(self):
        if self.ammo_amount < self.ammo_capacity:
            self.ammo_amount += self.reload_factor
        if self.ammo_amount > self.ammo_capacity:
            self.ammo_amount = self.ammo_capacity
        # Display ammo count at top-left corner
        self.ammo_count_colour = (120, 120, 120)
        self.ammo_count_font = pygame.font.SysFont(None, 48)
        self.ammo_count_image = self.ammo_count_font.render(
                str(int(self.ammo_amount)), True,
                self.ammo_count_colour, self.ammo_count_bg_colour)
        self.ammo_count_rect = self.ammo_count_image.get_rect()
        self.ammo_count_rect.left = self.screen.get_rect().left + 20
        self.ammo_count_rect.top = 20
        
    #def leveling_up(self, player_score):
        
