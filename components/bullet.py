import pygame
from .sprite import MySprite

class Bullet(MySprite):
    def __init__(self, limits=None):
        super().__init__(limits)