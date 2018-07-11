import pygame

class ScoreBoard():
    """ Record the points earned by players """
    def __init__(self, game_settings, screen):
        self.settings = game_settings
        self.screen = screen