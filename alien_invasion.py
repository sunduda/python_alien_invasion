import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from bullet import Bullet
from score_board import ScoreBoard
from game_stats import GameStats
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
    game_stats = GameStats(game_settings, screen, ship, aliens)
    game_stats.spawn_alien_fleet(game_settings, aliens)
    game_runs = True
    # The main game process
    while game_runs:
            gf.check_events(ship)
            ship.bullet_firing(game_settings, bullets)
            ship.update()
            game_runs = game_stats.check_aliens_win(game_settings, ship, aliens)
            gf.update_screen(game_settings, screen, ship, bullets, aliens, player_score)

    # If any alien succeeds in invasion, game over
    game_stats.game_over(game_settings)
    pygame.display.flip()

#------------------- Main process -----------------------#
run_game()
