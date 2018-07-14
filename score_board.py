import pygame

class ScoreBoard():
    """ Record the points earned by players """
    def __init__(self, game_settings, screen):
        self.settings = game_settings
        self.screen = screen
        self.score_colour = (30, 30, 30)
        self.score_font = pygame.font.SysFont(None, 48)
        self.score_reset()
        self.update()

    def score_reset(self):
        self.score = 0
        
    def update(self, alien = None):
        if alien != None:
            self.score += alien.score_value
        
        self.score_image = self.score_font.render(
                str(int(self.score)), True,
                self.score_colour, self.settings.bg_colour)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen.get_rect().right - 20
        self.score_rect.top = 20

    def blitme(self):
        """ Draw the ship at the assigned position """
        self.screen.blit(self.score_image, self.score_rect)
