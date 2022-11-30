import pygame
import os
import random
from globalvars import HEIGHT, WIDTH

class Zombie(pygame.sprite.Sprite):
    """zombie class

    Args:
        pygame (Sprite): pygame Sprite
    """
    def __init__(self, scale=1):
        pygame.sprite.Sprite.__init__(self)
        self.scale = scale
        self.speed = 5
        
        # Setup the zombie animation
        self.frame_interval = pygame.time.get_ticks()
        self.frames = []
        self.frame_index = 0

        # Load the images for left-side spawn
        num_of_files = len(os.listdir(f"images/zombie/walk/left"))
        tmp_list = []
        for i in range(0, num_of_files):
            image = pygame.image.load(f"images/zombie/walk/left/{i}.png").convert_alpha()
            image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
            tmp_list.append(image)
        self.frames.append(tmp_list)

        # Load the images for right-side spawn
        tmp_list = []
        for i in range(0, num_of_files):
            image = pygame.image.load(f"images/zombie/walk/right/{i}.png").convert_alpha()
            image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
            tmp_list.append(image)
        self.frames.append(tmp_list)

        # Set the initial image
        self.spawn_side = random.choice([0, 1])
        self.image = self.frames[self.spawn_side][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (0,0)

        # Determine which side the zombie will spawn
        if self.spawn_side == 0:
            self.rect.center = (0, HEIGHT - 230)
        if self.spawn_side == 1:
            self.rect.center = (WIDTH, HEIGHT - 230)

    def move(self):
        """Movement method for the zombie
        """
        x_to_change = 0
        y_to_change = 0

        # If the zombie is on the left side of the screen
        if self.spawn_side == 0:
            x_to_change = self.speed

        # If the zombie is on the right side of the screen
        if self.spawn_side == 1:
            x_to_change = -self.speed

        # Constantly move the zombie
        self.rect.x += x_to_change
        self.rect.y += y_to_change

    def update(self):      
        """Keep updating the zombie animation/movement/limit-checks
        """
        self.update_animation()
        self.move()

        # Check if the zombie is off the screen
        if self.rect.left > 960 and self.spawn_side == 0:
            self.kill()
        if self.rect.right < 0 and self.spawn_side == 1:
            self.kill()
        
    def update_animation(self):
        """Animate zombie sprite
        """
        animation_interval = 100
        self.image = self.frames[self.spawn_side][self.frame_index]

        # Check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.frame_interval > animation_interval:
            self.frame_interval = pygame.time.get_ticks()
            self.frame_index += 1
        
        # Reset the animation
        if self.frame_index >= len(self.frames[self.spawn_side]):
            self.frame_index = 0

    def draw(self, window):
        """Draw zombie

        Args:
            window (surface): window display surface
        """
        window.blit(self.image, self.rect)