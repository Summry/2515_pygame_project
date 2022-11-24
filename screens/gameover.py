import pygame
from .base import BaseScreen

class GameOverScreen(BaseScreen):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)