import sys
import pygame
from pygame.sprite import Sprite
from alien import Alien
from game_stats import GameStats

def check_keydown_events(event, ship):
    # When left/right key is pushed, set the flag to True
    if event.key == pygame.K_LEFT:
        ship.lkey_down = True
    if event.key == pygame.K_RIGHT:
        ship.rkey_down = True
    if event.key == pygame.K_SPACE:
        ship.open_fire = True

def check_keyup_events(event, ship):
    # When left/right key is released, set the flag to True
    if event.key == pygame.K_LEFT:
        ship.lkey_down = False
    if event.key == pygame.K_RIGHT:
        ship.rkey_down = False
    if event.key == pygame.K_SPACE:
        ship.open_fire = False

def check_events(ship):
    """ Response to keyboard and mouse events """
    # Supervise the keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        if event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
                
def update_screen(game_settings, screen, ship, bullets, aliens, player_score):
    # Fill the background
    screen.fill(game_settings.bg_colour)
    for bullet in bullets.sprites():
        # Draw every bullet on screen
        bullet.update()
        # When a bullet hits an alien, remove both the bullet and the alien
        # from their groups respectively
        # If a bullet is out of the screen, remove it from the group
        if bullet.hit_the_target(aliens, player_score) or (bullet.y < 0):
            bullets.remove(bullet)
    ship.blitme()
    check_fleet_edge(game_settings, screen, aliens)
    aliens.update()
    for alien in aliens.sprites():
        alien.blitme()

    player_score.blitme()

    # Display the screen
    pygame.display.flip()

def check_fleet_edge(game_settings, screen, aliens):
    for alien in aliens.sprites():
        if alien.rect.right >= screen.get_rect().right or \
                alien.rect.left <= screen.get_rect().left:
            game_settings.fleet_moving_direction *= -1
            fleet_drop(game_settings, aliens)
            break

def fleet_drop(game_settings, aliens):
    for alien in aliens.sprites():
        alien.y += alien.rect.height*game_settings.fleet_drop_factor
        alien.rect.y = alien.y

