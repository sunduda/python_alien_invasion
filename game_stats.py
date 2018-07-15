import pygame
import time

from alien import Alien
from button import Button

class GameStats():
    """ """
    def __init__(self, game_settings, screen, ship, aliens, bullets, 
            player_score):
        self.screen = screen
        self.settings = game_settings
        self.ship_limit = game_settings.ship_limit
        self.reset_stats(game_settings, ship, aliens, bullets, 
                player_score)
        self.game_active = False
        self.undefeated = True
        self.paused = False
        self.game_over_message = \
                "Something went wrong, you are not defeated yet"

    def reset_stats(self, game_settings, ship, aliens, bullets, 
            player_score):
        self.ship_remains = self.ship_limit
        ship.ship_reset(game_settings)
        player_score.score_reset()
        aliens.empty()
        bullets.empty()
        self.spawn_alien_fleet(game_settings, aliens)
        self.game_over_message = \
                "Something went wrong, you are not defeated yet"
        self.paused = False

    def blitme(self):
        self.screen.blit(self.pbg_mask, self.pbg_mask_rect)
        self.resume_button.blitme()
        self.mm_button.blitme()
        self.quit_button.blitme()
        
    def lose_a_ship(self, game_settings, ship, aliens):
        ship.rect.bottom = self.screen.get_rect().bottom
        ship.rect.centerx = self.screen.get_rect().centerx
        aliens_pos = []
        for alien in aliens.sprites():
            aliens_pos.append(alien.y)
        y_dist = min(aliens_pos) - alien.rect.height/2
        for alien in aliens.sprites():
            alien.y -= y_dist
            alien.rect.y = alien.y
        time.sleep(0.2)

    def spawn_alien_fleet(self, game_settings, aliens):
        # Create a fleet of aliens
        new_alien = Alien(game_settings, self.screen)
        aliens.add(new_alien)
        alien_width = new_alien.rect.width
        alien_height = new_alien.rect.height
        num_aliens_row = int((game_settings.screen_width - \
                alien_width)/2/alien_width)
        num_aliens_col = int(game_settings.screen_height/3/alien_height)
        for j in range(num_aliens_col):
            for i in range(0, num_aliens_row):
                if (j == 0) and (i == 0):
                    continue
                # Create an alien and assign it to the current row fleet
                new_alien = Alien(game_settings, self.screen)
                new_alien.x = (2*i + 1)*alien_width
                new_alien.rect.x = new_alien.x
                new_alien.y = (2*j + 1)*alien_height/2
                new_alien.rect.y = new_alien.y
                aliens.add(new_alien)

    def check_aliens_win(self, game_settings, ship, aliens):
        # Check if any alien reaches the bottom of the screen, or bumps 
        # into the ship
        for alien in aliens.sprites():
            if self.ship_remains > 1 and \
                    (alien.rect.bottom >= self.screen.get_rect().bottom\
                     or (alien.rect.bottom >= ship.rect.top and \
                    alien.rect.left < ship.rect.right and \
                    alien.rect.right > ship.rect.left)):
                self.ship_remains -= 1
                self.lose_a_ship(game_settings, ship, aliens)
                break
            elif self.ship_remains <= 1 and \
                    (alien.rect.bottom >= self.screen.get_rect().bottom\
                     and (alien.rect.left >= ship.rect.right or \
                    alien.rect.right <= ship.rect.left)):
                self.undefeated = False
                self.game_over_message = "You failed to protect the" \
                        " Earth from alien invasion"
                break
            elif self.ship_remains <= 1 and \
                    (alien.rect.bottom >= ship.rect.top and \
                    alien.rect.left < ship.rect.right and \
                    alien.rect.right > ship.rect.left):
                self.undefeated = False
                self.game_over_message = "You died and aliens now" \
                        " take over the Earth"
                break


    def game_over(self, game_settings):
        gg_colour = (255, 0, 0)
        gom_colour = (200, 0, 100)
        gg_font = pygame.font.SysFont(None, 64)
        gom_font = pygame.font.SysFont(None, 32)
        gg_image = gg_font.render(
                "Game Over!", True,
                gg_colour, game_settings.bg_colour)
        gom_image = gom_font.render(
                self.game_over_message, True,
                gg_colour, game_settings.bg_colour)
        gg_rect = gg_image.get_rect()
        gom_rect = gom_image.get_rect()
        gg_rect.center = self.screen.get_rect().center
        gg_rect.y -= gg_rect.height / 2
        gom_rect.center = self.screen.get_rect().center
        gom_rect.y += gom_rect.height /2
        self.screen.blit(gg_image, gg_rect)
        self.screen.blit(gom_image, gom_rect)

    def game_pause(self):
        screen_width = self.screen.get_rect().width
        screen_height = self.screen.get_rect().height
        screen_y = self.screen.get_rect().centery
        self.pbg_mask = pygame.Surface([screen_width, screen_height], \
                pygame.SRCALPHA, 32)
        self.pbg_mask.convert_alpha()
        self.pbg_mask.fill((100,100,100,128))
        self.pbg_mask_rect = self.pbg_mask.get_rect()
        self.pbg_mask_rect.center = self.screen.get_rect().center
        self.resume_button = \
                Button(self.settings, self.screen, "Resume")
        self.mm_button = \
                Button(self.settings, self.screen, "Main Menu")
        self.quit_button = \
                Button(self.settings, self.screen, "Quit")
        
        rb_height = self.resume_button.rect.height
        mmb_height = self.mm_button.rect.height
        qb_height = self.quit_button.rect.height
        
        
        self.resume_button.rect.centery = \
                screen_y - mmb_height/2 - 10 - rb_height/2
        self.mm_button.rect.centery = self.screen.get_rect().centery
        self.quit_button.rect.centery = \
                screen_y + mmb_height/2 + 10 + qb_height/2
