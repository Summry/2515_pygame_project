import pygame
from .sprite import MySprite

class Zombie(MySprite):
    def __init__(self, limits=None):
        super().__init__(limits)