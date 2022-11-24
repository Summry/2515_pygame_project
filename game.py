import pygame
pygame.init()
from screens import WelcomeScreen, GameScreen, GameOverScreen


class Game:
    """Main class for the application"""

    def __init__(self):
        # Creates the window
        self.window = pygame.display.set_mode((960, 540))

    def run(self):
        """Main method, manages interaction between screens"""
        pygame.display.set_caption("Caustic: The Zombie Shooter")


        # These are the available screens
        screens = {
            "welcome": WelcomeScreen,
            "game": GameScreen,
            "game_over": GameOverScreen,
        }

        # Start the loop
        running = True
        current_screen = "welcome"
        while running:

            # Play music
            self.play_music(current_screen)

            # Obtain the screen class
            screen_class = screens.get(current_screen)
            if not screen_class:
                raise RuntimeError(f"Screen {current_screen} not found!")

            # Create a new screen object, "connected" to the window
            screen = screen_class(self.window)

            # Run the screen
            screen.run()

            # When the `run` method stops, we should have a `next_screen` setup
            if screen.next_screen is False:
                running = False
            # Switch to the next screen
            current_screen = screen.next_screen
    
    def play_music(self, screen):
        if (screen):
            pygame.mixer.music.load(f"audio/{screen}.mp3")
            if (screen == "game"):
                pygame.mixer.music.set_volume(0.08)
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.stop()


if __name__ == "__main__":
    zombieshooter = Game()
    zombieshooter.run()
