# (137, 207, 240)
import pygame
from .base import BaseScreen
from components.button import Button


class WelcomeScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sprites = pygame.sprite.Group()
        self.start = Button(pygame.image.load("images/red_start.jpg"), 700, 170, 0.3)
        self.exit = Button(pygame.image.load("images/red_exit.png"), 700, 300, 0.64)


    def draw(self):
        self.start.draw(self.window)
        self.exit.draw(self.window)

    def update(self):
        pass

    def manage_event(self, event):
        print(event)
        if self.start.draw(self.window):
            # add click sound
            self.next_screen = "game"
            self.running = False
        if self.exit.draw(self.window):
            # add click sound
            self.running = False