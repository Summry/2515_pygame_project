import pygame
import requests
from datetime import datetime
from .base import BaseScreen
from components.button import Button
from globalvars import HEIGHT, WIDTH

class GameOverScreen(BaseScreen):
    """Game Over Screen

    Args:
        BaseScreen (screen): parent class of the GameOverScreen
    """
    def __init__(self, window, final_score, username, password) -> None:
        super().__init__(window)

        # Finally assign the final score and username to be stored
        self.username = username
        self.password = password
        self.final_score = final_score
        self.score_recorded = False

        # Load the image
        image = pygame.image.load("images/game_over.png").convert_alpha()
        self.image = pygame.transform.scale(image, (WIDTH // 1.6, HEIGHT // 3.6))

        # Create the buttons
        self.retry = Button(pygame.image.load("images/retry.png").convert_alpha(), WIDTH // 4, HEIGHT // 1.8, 0.66)
        self.exit = Button(pygame.image.load("images/red_exit.png").convert_alpha(), WIDTH // 1.92, HEIGHT // 1.8, 0.64)
        
    def display_final_score(self):
        """Method to display the final score"""
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
        """Manage the events of the gameover screen

        Args:
            event (pygame event): a pygame event
        """

        # If the user clicks on the retry button, go back to the game screen
        if self.retry.draw(self.window):
            button_sound = pygame.mixer.Sound("audio/button-click.mp3")
            button_sound.set_volume(0.3)
            button_sound.play()
            self.final_score = 0
            self.next_screen = "game"
            self.running = False

        # If the user clicks on the exit button
        if self.exit.draw(self.window):
            self.running = False

    def upload_score(self):
        """Method to get the score object and posts it to url
        """
        flask_url = "http://127.0.0.1:5000/add" # Reference to the flask server

        # Create the game object
        game = {
            "username": self.username,
            "password": self.password, # Exclude password when getting scores
            "score": self.final_score,
            "date": str(datetime.now())
        }

        # Post the game object to the url
        requests.post(flask_url, json=game)

    def update(self):
        # If score has not been recorded yet
        if self.score_recorded == False:
            self.score_recorded = True # Score has been recorded
            self.upload_score() # Upload the score