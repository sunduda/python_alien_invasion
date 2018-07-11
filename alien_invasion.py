import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from bullet import Bullet
import game_functions as gf

def run_game():
    # Pygame window initialization
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(game_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.spawn_alien_fleet(game_settings, screen, aliens)
    # The main game process
    while True:
            gf.check_events(ship)
            ship.bullet_firing(bullets)
            ship.update()
            bullets.update()
            
            gf.update_screen(game_settings, screen, ship, bullets, aliens)

run_game()
