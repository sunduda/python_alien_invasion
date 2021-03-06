import pygame.font

class Button():
    def __init__(self, game_settings, screen, msg):
        self.screen = screen
        self.width, self.height = 200, 50
        self.bg_colour = (0, 255, 0)
        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen.get_rect().center
        
        self.prep_msg(msg)
        
    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_colour, \
                self.bg_colour)
        self.msg_image_rect = self.msg_image.get_rect()
    
    def blitme(self):
        self.msg_image_rect.center = self.rect.center
        self.screen.blit(self.msg_image, self.msg_image_rect)
    
    def check_clicked(self, stats, mouse_x, mouse_y):
        if mouse_x > self.rect.left and mouse_x < self.rect.right and \
                mouse_y > self.rect.top and mouse_y < self.rect.bottom:
            return True
        else:
            return False
