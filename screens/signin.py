import pygame
from .base import BaseScreen
from globalvars import HEIGHT, WIDTH

class SignInScreen(BaseScreen):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.final_score = None

        # Display the username message and frame
        self.username = ""
        self.password = ""
        self.check_username = False

        # Load username message and frame images
        self.username_msg = pygame.image.load("images/username.png").convert_alpha()
        input_frame_image = pygame.image.load("images/username-frame.png").convert_alpha()
        self.input_frame = pygame.transform.scale(input_frame_image, (330, 100))

        # Display the username font
        self.username_font = pygame.font.Font("fonts/minecraft.ttf", 30)
        self.retry = False

        # Display the password font
        self.password_font = pygame.font.Font("fonts/minecraft.ttf", 30)

    def draw(self):
        """Method to draw the username frame and message"""
        self.window.blit(self.username_msg, (90, 180))

        # Display the username information
        username_text_surface = self.username_font.render(f"{self.username}", False, "Black")
        self.window.blit(self.input_frame, (330, 290))
        self.window.blit(username_text_surface, (375, 325))

        # Display the password information
        password_text_surface = self.password_font.render(f"{'*' * len(self.password)}", False, "Black")
        self.window.blit(self.input_frame, (330, 365))
        self.window.blit(password_text_surface, (375, 400))

    def update(self):
        if self.retry == True:
            self.display_retry()

    def display_retry(self):
        """Method to display the retry notice
        """
        retry = pygame.font.Font("fonts/minecraft.ttf", 50)
        retry_text_surface = retry.render("Please try again.", False, "Red")
        self.window.blit(retry_text_surface, (WIDTH // 1.85, HEIGHT - 50))

    def manage_event(self, event):
        if event.type == pygame.KEYDOWN:

            if self.check_username == False:

                # Erase the last character of the username string
                if event.key == pygame.K_BACKSPACE:
                    self.username = self.username[:-1]

                # Confirm that username was typed
                if event.key == pygame.K_RETURN and len(self.username) > 0:
                    self.check_username = True

                # Username is empty and return key is pressed
                if event.key == pygame.K_RETURN and len(self.username) == 0:
                    self.retry = True

                # Type username
                if event.unicode.isalnum() and len(self.username) < 10:
                    self.username += event.unicode

            else:
                
                # Erase the last character of the password
                if event.key == pygame.K_BACKSPACE:
                    self.password = self.password[:-1]

                # Password is empty and return key is pressed
                if event.key == pygame.K_RETURN and len(self.password) == 0:
                    self.retry = True

                # Password is not empty and return key is pressed
                if len(self.password) > 0 and event.key == pygame.K_RETURN:
                    self.running = False
                    self.next_screen = "welcome"
                    
                # Type password
                if event.unicode.isalnum() and len(self.password) < 12:
                    self.password += event.unicode