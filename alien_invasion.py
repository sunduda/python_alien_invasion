import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from bullet import Bullet
from score_board import ScoreBoard
from game_stats import GameStats
from button import Button
import game_functions as gf

def run_game():
    # Pygame window initialization
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(game_settings, screen, "Play")
    
    # Objects initialization
    ship = Ship(game_settings, screen)
    bullets = Group()
    aliens = Group()
    player_score = ScoreBoard(game_settings, screen)
    stats = GameStats(game_settings, screen, ship, aliens)
    
    # The main game process
    while True:
        gf.check_events(stats, play_button, ship)
        
        if stats.game_active:
            ship.update()
            ship.bullet_firing(game_settings, bullets)
            stats.check_aliens_win(game_settings, ship, aliens)
            gf.update_screen(game_settings, screen, ship, bullets, aliens, 
                player_score)
        else:
            gf.display_title(game_settings, screen, play_button)
        
        
        # If any alien succeeds in invasion, game over
        if not stats.undefeated:
            stats.game_over(game_settings)
            pygame.display.flip()
            while stats.game_active:
                gf.check_events(stats, play_button, ship)

#------------------- Main process -----------------------#
run_game()
