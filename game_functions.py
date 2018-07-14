import sys
import pygame
from pygame.sprite import Sprite
from alien import Alien

def display_title(game_settings, screen, play_button):
    # Display game title
    screen.fill(game_settings.bg_colour)
    title_colour = (100, 100, 100)
    title_font = pygame.font.SysFont(None, 128)
    title_image = title_font.render(
                game_settings.game_title, True,
                title_colour, game_settings.bg_colour)
    title_rect = title_image.get_rect()
    title_rect.centerx = screen.get_rect().centerx
    title_rect.y = screen.get_rect().height*1/3
    screen.blit(title_image, title_rect)
    # Display "Play" button
    play_button.blitme()
    pygame.display.flip()
    

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

def check_events(stats, play_button, ship):
    """ Response to keyboard and mouse events """
    # Supervise the keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        if event.type == pygame.KEYUP:
            if stats.undefeated:
                check_keyup_events(event, ship)
            else:
                stats.game_active = False
                stats.undefeated = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            play_button.check_clicked(stats, mouse_x, mouse_y)
                
def update_screen(game_settings, screen, ship, bullets, aliens, player_score):
    # Fill the background
    screen.fill(game_settings.bg_colour)
    for bullet in bullets.sprites():
        # Draw every bullet on screen
        bullet.update()
        # When a bullet hits an alien, remove both the bullet and the alien
        # from their groups respectively
        # If a bullet is out of the screen, remove it from the group
        bullet_consumed, aliens = bullet.hit_the_target(aliens, player_score)
        if bullet_consumed or (bullet.y < 0):
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

