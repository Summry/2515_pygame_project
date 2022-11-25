import pygame

class BaseScreen:

    def __init__(self, window) -> None:
        """Base Screen Attributes

        Args:
            window (window): Window to be display
        """
        self.window = window
        self.next_screen = False
        self.background = pygame.transform.scale(pygame.image.load("images/snow_forest.png").convert_alpha(), (960, 540))

    def run(self):
        """method that runs the screen for all screens
        """

        clock = pygame.time.Clock()
        self.running = True

        while self.running:
            # Clock ticks at 60 FPS
            clock.tick(60)

            # Draw the snow background (same for every screen)
            self.window.blit(self.background, (0, 0))

            # Update screens and drawings of each screen
            self.update()
            self.draw()

            # Event loop
            for event in pygame.event.get():
                # Quitting
                if event.type == pygame.QUIT:
                    self.running = False
                    self.next_screen = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False
                    self.next_screen = False

                self.manage_event(event)

            # Update the entire display
            pygame.display.update()

    @property
    def rect(self):

        return self.window.get_rect()

    def draw(self):
        """Child classes should override this method"""

        print("You should override the DRAW method in your class...")

    def update(self):
        """Child classes should override this method"""

        print("You should override the UPDATE method in your class...")

    def manage_event(self, event):
        """Child classes should override this method"""

        print("You should override the MANAGE_EVENT method in your class...")