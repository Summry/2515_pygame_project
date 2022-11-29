import pygame
import requests
from .base import BaseScreen
from components.button import Button
from globalvars import HEIGHT, WIDTH

class GameOverScreen(BaseScreen):
    """Game Over Screen

    Args:
        BaseScreen (screen): parent class of the GameOverScreen
    """
    def __init__(self, window, final_score, username) -> None:
        super().__init__(window)
        self.final_score = final_score
        self.username = username
        image = pygame.image.load("images/game_over.png").convert_alpha()
        self.image = pygame.transform.scale(image, (WIDTH // 1.6, HEIGHT // 3.6))
        self.retry = Button(pygame.image.load("images/retry.png").convert_alpha(), WIDTH // 4, HEIGHT // 1.8, 0.66)
        self.exit = Button(pygame.image.load("images/red_exit.png").convert_alpha(), WIDTH // 1.92, HEIGHT // 1.8, 0.64)
        self.score_recorded = False
        
    def display_final_score(self):
        score_font = pygame.font.Font("fonts/minecraft.ttf", 50)
        score_text_surface = score_font.render(f"Your score: {self.final_score}", False, "Black")
        self.window.blit(score_text_surface, (280, 430))

    def draw(self):
        """Constantly draw the gameover screen
        """
        self.window.blit(self.image, (180, HEIGHT // 6.75))
        self.display_final_score()
        self.retry.draw(self.window)
        self.exit.draw(self.window)

    def manage_event(self, event):
        """Event manager

        Args:
            event (pygame event): a pygame event
        """
        if self.retry.draw(self.window):
            button_sound = pygame.mixer.Sound("audio/button-click.mp3")
            button_sound.set_volume(0.3)
            button_sound.play()
            self.final_score = 0
            self.next_screen = "game"
            self.running = False
        if self.exit.draw(self.window):
            self.running = False

    def upload_score(self):
        """Method to get the score object and posts it to url
        """
        flask_url = "http://127.0.0.1:5000/add"

        game = {
            "username": self.username, 
            "score": self.final_score
        }

        requests.post(flask_url, json=game)

    def update(self):
        # If score has not been recorded yet
        if self.score_recorded == False:
            self.score_recorded = True # Score has been recorded
            self.upload_score() # Upload the score