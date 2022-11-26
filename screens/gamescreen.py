import pygame
import random
from .base import BaseScreen
from components.player import Player
from components.zombie import Zombie

class GameScreen(BaseScreen):
    """Screen for the game

    Args:
        BaseScreen (screen): base screen of the game
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # Create the player
        self.player = Player(480, 350, 0.2, speed=5)
        self.move_left = False
        self.move_right = False
        self.shoot = False

        # Create zombie group and spawn timer
        self.zombie_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.zombie_timer, 1500)
        self.zombie_group = pygame.sprite.Group()

        # Create player sprite
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)

        text_font = pygame.font.Font("fonts/minecraft.ttf", 50)
        self.score = 0
        self.text_surface = text_font.render(f"Score: {self.score}", False, "Black")

    def draw(self):
        """Keep drawing the player, zombie, the score, and the health point
        """
        if self.player.is_alive:
            # Shoot bullets
            if self.shoot:
                self.player.shoot()
            if self.player.in_the_air:
                # Jump animation
                self.player.update_action(2)
            elif self.move_left or self.move_right:
                # Run animation
                self.player.update_action(1)
            else:
                # Stand animation
                self.player.update_action(0)

            self.player.move(self.move_left, self.move_right)
        
        self.player.draw(self.window)
        self.zombie_group.update()
        self.zombie_group.draw(self.window)
        
        # Draw the score count
        self.window.blit(self.text_surface, (10, 490))

    def update(self):
        """Keep updating any changes made during the game
        """
        self.player_group.update()
        
    def manage_event(self, event):
        """Manage all events done during the game screen

        Args:
            event (event): a pygame event
        """
        if event.type == self.zombie_timer:
            self.zombie_group.add(Zombie(0.3))

        if event.type == pygame.KEYDOWN:
            # If player presses left key
            if event.key == pygame.K_a:
                self.move_left = True
            # If player presses right key
            if event.key == pygame.K_d:
                self.move_right = True
            # If player presses L key
            if event.key == pygame.K_l:
                self.shoot = True
            # If player presses space key
            if event.key == pygame.K_SPACE and self.player.is_alive:
                self.player.jump = True
    
        if event.type == pygame.KEYUP:
            # If player lets go of left key
            if event.key == pygame.K_a:
                self.move_left = False
            # If player lets go of right key
            if event.key == pygame.K_d:
                self.move_right = False
            # If player lets go of the L key
            if event.key == pygame.K_l:
                self.shoot = False