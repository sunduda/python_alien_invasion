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
    quit_button = Button(game_settings, screen, "Quit")
    
    # Objects initialization
    ship = Ship(game_settings, screen)
    bullets = Group()
    aliens = Group()
    player_score = ScoreBoard(game_settings, screen)
    stats = GameStats(game_settings, screen, ship, aliens, bullets, player_score)
    
    # The main game process
    while True:
        gf.check_events(game_settings, stats, play_button, quit_button, 
                ship, aliens, bullets, player_score)
        
        if stats.game_active:
            pygame.mouse.set_visible(False)
            if stats.paused:
                pygame.mouse.set_visible(True)
            else:
                ship.update()
                ship.bullet_firing(game_settings, bullets)
                bullets.update()
                gf.check_fleet_edge(game_settings, screen, aliens)
                aliens.update()
                stats.check_aliens_win(game_settings, ship, aliens)
            gf.update_screen(game_settings, screen, stats, ship, bullets, aliens, 
                    player_score)
        else:
            pygame.mouse.set_visible(True)
            gf.display_title(game_settings, screen, play_button, 
                    quit_button)
        
        
        # If any alien succeeds in invasion, game over
        if not stats.undefeated:
            stats.game_over(game_settings)
            pygame.display.flip()
            while stats.game_active:
                gf.check_events(game_settings, stats, play_button, 
                        quit_button, ship, aliens, bullets, 
                        player_score)
                stats.reset_stats(game_settings, ship, aliens, bullets, player_score)

#------------------- Main process -----------------------#
run_game()
