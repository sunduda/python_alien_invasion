import sys
import pygame
from pygame.sprite import Sprite
from alien import Alien

def display_title(game_settings, screen, play_button, quit_button):
    # Display game title
    screen.fill(game_settings.bg_colour)
    title_colour = (100, 100, 100)
    title_font = pygame.font.SysFont(None, 128)
    title_image = title_font.render(
                game_settings.game_title, True,
                title_colour, game_settings.bg_colour)
    title_rect = title_image.get_rect()
    title_rect.centerx = screen.get_rect().centerx
    title_rect.centery = screen.get_rect().height*1/3
    screen.blit(title_image, title_rect)
    # Display "Play" button
    play_button.rect.centery = screen.get_rect().height*2/3 - 50
    play_button.blitme()
    
    # Display "Quit" button
    quit_button.rect.centery = screen.get_rect().height*2/3 + 50
    quit_button.blitme()
    pygame.display.flip()

def check_keydown_events(event, stats, ship):
    # When left/right key is pushed, set the flag to True
    if event.key == pygame.K_LEFT:
        ship.lkey_down = True
    if event.key == pygame.K_RIGHT:
        ship.rkey_down = True
    if event.key == pygame.K_SPACE:
        ship.open_fire = True
    if event.key == pygame.K_ESCAPE:
        stats.game_pause()
        stats.paused = not stats.paused

def check_keyup_events(event, ship):
    # When left/right key is released, set the flag to True
    if event.key == pygame.K_LEFT:
        ship.lkey_down = False
    if event.key == pygame.K_RIGHT:
        ship.rkey_down = False
    if event.key == pygame.K_SPACE:
        ship.open_fire = False

def check_events(game_settings, stats, play_button, quit_button, ship, 
        aliens, bullets, player_score):
    """ Response to keyboard and mouse events """
    # Supervise the keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, stats, ship)
        if event.type == pygame.KEYUP:
            if not stats.undefeated:
                stats.game_active = False
                stats.undefeated = True
            check_keyup_events(event, ship)
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if not stats.game_active:
                if play_button.check_clicked(stats, mouse_x, mouse_y):
                    stats.game_active = True
                elif quit_button.check_clicked(stats, mouse_x, mouse_y):
                    sys.exit()
            elif stats.game_active and stats.paused:
                if stats.resume_button.check_clicked(stats, mouse_x, \
                        mouse_y):
                    stats.paused = False
                elif stats.mm_button.check_clicked(stats, mouse_x, \
                        mouse_y):
                    stats.reset_stats(game_settings, ship, aliens, \
                            bullets, player_score)
                    stats.game_active = False
                elif stats.quit_button.check_clicked(stats, mouse_x, \
                        mouse_y):
                    sys.exit()
                
def update_screen(game_settings, screen, stats, ship, bullets, aliens, player_score):
    # Fill the background
    screen.fill(game_settings.bg_colour)
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.blitme()
    
    for alien in aliens.sprites():
        alien.blitme()
    
    if stats.paused:
        stats.blitme()
        
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
        
def enemy_neutralized(game_settings, stats, ship, aliens, bullets, player_score):
    for bullet in bullets.sprites():
        # When a bullet hits an alien, remove both the bullet and the alien
        # from their groups respectively
        # If a bullet is out of the screen, remove it from the group
        bullet_consumed, aliens = bullet.hit_the_target(aliens, player_score)
        if bullet_consumed or (bullet.y < 0):
            bullets.remove(bullet)

