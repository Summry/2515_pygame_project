import pygame
from .base import BaseScreen
from components.button import Button


class WelcomeScreen(BaseScreen):
    """Welcome screen of the game

    Args:
        BaseScreen (Screen): base screen of the game
    """
    def __init__(self, *args, **kwargs):
        """constructor"""
        super().__init__(*args, **kwargs)
        self.sprites = pygame.sprite.Group()
        self.start = Button(pygame.image.load("images/red_start.jpg"), 700, 170, 0.3)
        self.exit = Button(pygame.image.load("images/red_exit.png"), 700, 300, 0.64)
        self.title = pygame.image.load("images/title.png")

    def draw(self):
        """drawing welcome screen's surfaces
        """
        self.window.blit(self.title, (0,0))
        self.start.draw(self.window)
        self.exit.draw(self.window)

    def update(self):
        pass

    def manage_event(self, event):
        """manages the events in welcome screen

        Args:
            event (event): an event in pygame
        """
        if self.start.draw(self.window):
            button_sound = pygame.mixer.Sound("audio/button-click.mp3")
            button_sound.set_volume(0.3)
            button_sound.play()
            self.next_screen = "game"
            self.running = False
        if self.exit.draw(self.window):
            self.running = False