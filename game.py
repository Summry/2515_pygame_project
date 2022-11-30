import pygame
from screens import WelcomeScreen, GameScreen, GameOverScreen, SignInScreen
from globalvars import HEIGHT, WIDTH


class Game:
    """Main class for the application"""

    def __init__(self):
        # Creates the window
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))

    def run(self):
        """Main method, manages interaction between screens"""
        pygame.display.set_caption("Caustic: Jumper and Zombie Shooter")


        # These are the available screens
        screens = {
            "signin": SignInScreen,
            "welcome": WelcomeScreen,
            "game": GameScreen,
            "game_over": GameOverScreen,
        }

        # Start the loop
        running = True
        current_screen = "signin"

        # Initialize game data
        username = None
        password = None
        final_score = None

        while running:

            # Play music
            self.play_music(current_screen)

            # Obtain the screen class
            screen_class = screens.get(current_screen)
            if not screen_class:
                raise RuntimeError(f"Screen {current_screen} not found!")

            # Create a new screen object, "connected" to the window
            if current_screen == "game_over":
                screen = screen_class(self.window, final_score, username, password)
            else:
                screen = screen_class(self.window)

            # Run the screen
            screen.run()

            # Keep the final score
            if screen.final_score is not None:
                final_score = screen.final_score

            # Keep the username from signin screen
            if screen.username is not None:
                username = screen.username

            # Keep the password from signin screen
            if screen.password is not None:
                password = screen.password

            # When the `run` method stops, we should have a `next_screen` setup
            if screen.next_screen is False:
                running = False

            # Switch to the next screen
            current_screen = screen.next_screen
    
    def play_music(self, screen):
        """Method that plays unique music per screen

        Args:
            screen (surface): screen that is currently running
        """
        if (screen):
            pygame.mixer.music.load(f"audio/{screen}.mp3")
            if (screen == "signin"):
                pygame.mixer.music.set_volume(0.02)
            elif (screen == "welcome"):
                pygame.mixer.music.set_volume(0.5)
            elif (screen == "game"):
                pygame.mixer.music.set_volume(0.02)
            elif (screen == "game_over"):
                pygame.mixer.music.set_volume(1.1)
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.stop()


if __name__ == "__main__":
    zombieshooter = Game()
    zombieshooter.run()
