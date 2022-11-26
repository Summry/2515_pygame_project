import pygame
import os
from .base import BaseScreen
from components.button import Button

class WelcomeScreen(BaseScreen):
    """Welcome screen of the game

    Args:
        BaseScreen (Screen): base screen of the game
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.frames = []
        self.frame_index = 0
        self.frame_interval = pygame.time.get_ticks()

        num_of_files = len(os.listdir("images/player/stand"))

        for i in range(0, num_of_files):
            image = pygame.image.load(f"images/player/stand/{i}.png").convert_alpha()
            image = pygame.transform.scale(image, (int(image.get_width() * 0.5), int(image.get_height() * 0.5)))
            self.frames.append(image)
        
        self.image = self.frames[self.frame_index]

        self.start = Button(pygame.image.load("images/red_start.jpg").convert_alpha(), 700, 170, 0.3)
        self.exit = Button(pygame.image.load("images/red_exit.png").convert_alpha(), 700, 300, 0.64)
        self.title = pygame.image.load("images/title.png").convert_alpha()

    def draw(self):
        """drawing welcome screen's surfaces
        """
        self.window.blit(self.title, (0,0))
        self.window.blit(self.image, (100, 150))
        self.start.draw(self.window)
        self.exit.draw(self.window)

    def update(self):
        animation_interval = 100
        self.image = self.frames[self.frame_index]
        if pygame.time.get_ticks() - self.frame_interval > animation_interval:
            self.frame_interval = pygame.time.get_ticks()
            self.frame_index += 1

        if self.frame_index >= len(self.frames):
            self.frame_index = 0

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