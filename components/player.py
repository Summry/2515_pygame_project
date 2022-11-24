import pygame
from .sprite import MySprite

class Player(MySprite):
    def __init__(self, limits=None):
        super().__init__(limits)

        self.image = pygame.image.load("images/player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (480, 500)

    def draw(self, window):
        window.blit(self.image, self.rect)