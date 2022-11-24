import pygame
import random
from .base import BaseScreen
from components.player import Player
from components.zombie import Zombie

class GameScreen(BaseScreen):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # Create the player
        self.player = Player(480, 350, 0.2)

        # Create a zombie
        # self.zombie = Zombie(limits=self.rect)




        # Put all sprites in the group
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.player)
        # self.sprites.add(self.zombie)

    def draw(self):
        self.player.draw(self.window)

    # def update(self):
    #     keys = pygame.key.get_pressed()
    #     if keys[pygame.K_LEFT]:
    #         self.player.move("left")

    #     if keys[pygame.K_RIGHT]:
    #         self.player.move("right")

    #     self.sprites.update()
    #     collided = self.