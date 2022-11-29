import pygame
import os
from .base import BaseScreen
from components.button import Button
from globalvars import HEIGHT, WIDTH

class WelcomeScreen(BaseScreen):
    """Welcome screen of the game

    Args:
        BaseScreen (Screen): base screen of the game
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.frames = []
        self.frame_index = 0
        self.final_score = None
        self.username = None
        self.frame_interval = pygame.time.get_ticks()

        num_of_files = len(os.listdir("images/player/stand"))

        for i in range(0, num_of_files):
            image = pygame.image.load(f"images/player/stand/{i}.png").convert_alpha()
            image = pygame.transform.scale(image, (int(image.get_width() * 0.3), int(image.get_height() * 0.3)))
            self.frames.append(image)
        
        self.image = self.frames[self.frame_index]

        self.start = Button(pygame.image.load("images/red_start.jpg").convert_alpha(), 700, HEIGHT // 1.8, 0.3)
        self.exit = Button(pygame.image.load("images/red_exit.png").convert_alpha(), 700, HEIGHT // 1.3, 0.64)

    def display_title(self):
        """Method to display the title
        """
        title_image = pygame.image.load("images/title.png").convert_alpha()
        title = pygame.transform.scale(title_image, (title_image.get_width() * 1.1, title_image.get_height() * 1.05))
        self.window.blit(title, (0, 0))

    def draw(self):
        """drawing welcome screen's surfaces
        """
        self.display_title()
        self.window.blit(self.image, (WIDTH // 9.6, WIDTH // 3.6))
        self.start.draw(self.window)
        self.exit.draw(self.window)

    def update(self):
        """Updates the animation of the character
        """
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