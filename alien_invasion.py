import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from bullet import Bullet
from score_board import ScoreBoard
import game_functions as gf

def run_game():
    # Pygame window initialization
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(game_settings, screen)
    player_score = ScoreBoard(game_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.spawn_alien_fleet(game_settings, screen, aliens)

    game_runs = True
    # The main game process
    while game_runs:
            gf.check_events(ship)
            ship.bullet_firing(bullets)
            ship.update()
            bullets.update()
            game_runs = gf.check_aliens_win(screen, ship, aliens)
            gf.update_screen(game_settings, screen, ship, bullets, aliens, play_score)

    # If any alien succeeds in invasion, game over
    gf.game_over(game_settings, screen)
    pygame.display.flip()

#------------------- Main process -----------------------#
run_game()
