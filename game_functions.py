import sys
import pygame
from pygame.sprite import Sprite
from alien import Alien

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
        bullet.draw_bullet()
        # When a bullet hits an alien, remove both the bullet and the alien
        # from their groups respectively
        if bullet_hit(bullet, aliens, player_score):
            bullets.remove(bullet)

        # If a bullet is out of the screen, remove it from the group
        if bullet.y < 0:
            bullets.remove(bullet)
    ship.blitme()
    check_fleet_edge(game_settings, screen, aliens)
    aliens.update()
    for alien in aliens.sprites():
        alien.blitme()

    player_score.blitme()
    # Display the screen
    pygame.display.flip()

def spawn_alien_fleet(game_settings, screen, aliens):
    # Create a fleet of aliens
    new_alien = Alien(game_settings, screen)
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
            new_alien = Alien(game_settings,screen)
            new_alien.x = (2*i + 1)*alien_width
            new_alien.rect.x = new_alien.x
            new_alien.y = (2*j + 1)*alien_height/2
            new_alien.rect.y = new_alien.y
            aliens.add(new_alien)

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

def bullet_hit(bullet, aliens, player_score):
    for alien in aliens.sprites():
        if bullet.rect.top < alien.rect.bottom and \
                bullet.rect.left < alien.rect.right and \
                bullet.rect.right > alien.rect.left:
            player_score.update(alien)
            aliens.remove(alien)
            return True
            break

    return False