import pygame
from .base import BaseScreen
from globalvars import HEIGHT, WIDTH

class SignInScreen(BaseScreen):
    def __init__(self, window) -> None:
        super().__init__(window)
        self.final_score = None

        # Display the username message and frame
        self.username = ""
        self.password = ""
        self.username_check = False

        # 
        self.username_msg = pygame.image.load("images/username.png").convert_alpha()
        userframe = pygame.image.load("images/username-frame.png").convert_alpha()
        self.input_frame = pygame.transform.scale(userframe, (330, 100))

        # Display the username font
        self.username_font = pygame.font.Font("fonts/minecraft.ttf", 30)
        self.empty_username = True

        # Display the password font
        self.password_font = pygame.font.Font("fonts/minecraft.ttf", 30)
        self.empty_password = True

    def draw(self):
        """Method to draw the username frame and message"""
        self.window.blit(self.username_msg, (90, 180))

        # Display the username information
        self.username_text_surface = self.username_font.render(f"{self.username}", False, "Black")
        self.window.blit(self.input_frame, (330, 290))
        self.window.blit(self.username_text_surface, (375, 325))

        # Display the password information
        self.password_text_surface = self.password_font.render(f"{self.password}", False, "Black")
        self.window.blit(self.input_frame, (330, 340))
        self.window.blit(self.password_text_surface, (375, 375))

    def update(self):
        if self.empty_username is True or self.empty_password is True:
            self.display_retry()

    def display_retry(self):
        """Method to display the retry notice
        """
        retry = pygame.font.Font("fonts/minecraft.ttf", 50)
        retry_text_surface = retry.render("Please try again.", False, "Red")
        self.window.blit(retry_text_surface, (WIDTH // 1.85, HEIGHT - 50))

    def manage_event(self, event):
        if event.type == pygame.KEYDOWN:

            # Erase the last character of the username string
            if event.key == pygame.K_BACKSPACE:
                self.username = self.username[:-1]

            # Confirm that username was typed
            elif event.key == pygame.K_RETURN and self.empty_username is False:
                self.username_check = True

            # Username is empty and return key is pressed
            elif event.key == pygame.K_RETURN and self.username == "":
                self.empty_username = True

            # Password is empty and return key is pressed
            elif event.key == pygame.K_RETURN and self.password == "":
                self.empty_password = True

            # Password is not empty and return key is pressed
            elif self.password != "" and event.key == pygame.K_RETURN:
                self.next_screen = "welcome"
                self.running = False

            # Make sure the username is not longer than 10 characters
            elif len(self.username) > 9:
                self.username = self.username

            # Type username
            elif self.username_check is False:
                if event.unicode.isalnum():
                    if self.empty_username is True:
                        self.empty_username = False
                    self.username += event.unicode

            # Type password
            elif self.username_check is True:
                if event.unicode.isalnum():
                    if self.empty_password is True:
                        self.empty_password = False
                    self.password += event.unicode