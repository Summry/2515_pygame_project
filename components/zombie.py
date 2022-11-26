import pygame
import os
import random

class Zombie(pygame.sprite.Sprite):
    """zombie class

    Args:
        pygame (Sprite): pygame Sprite
    """
    def __init__(self, scale=1):
        pygame.sprite.Sprite.__init__(self)
        self.scale = scale
        
        self.speed = 4
        self.frames = []
        self.frame_index = 0
        self.frame_interval = pygame.time.get_ticks()
        self.spawn_side = random.choice([0, 1])

        # Load the images for left-side spawn and right-side spawn
        tmp_list = []
        num_of_files = len(os.listdir(f"images/zombie/walk/left"))
        for i in range(0, num_of_files):
            image = pygame.image.load(f"images/zombie/walk/left/{i}.png").convert_alpha()
            image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
            tmp_list.append(image)
        self.frames.append(tmp_list)

        tmp_list = []
        for i in range(0, num_of_files):
            image = pygame.image.load(f"images/zombie/walk/right/{i}.png").convert_alpha()
            image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
            tmp_list.append(image)
        self.frames.append(tmp_list)

        # Determine which side the zombie will spawn
        self.image = self.frames[self.spawn_side][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (0,0)
        if self.spawn_side == 0:
            self.rect.center = (0, 310)
        if self.spawn_side == 1:
            self.rect.center = (960, 310)

    def move(self):
        """Movement method for the zombie
        """
        x_to_change = 0
        y_to_change = 0

        if self.spawn_side == 0:
            x_to_change = self.speed

        if self.spawn_side == 1:
            x_to_change = -self.speed

        self.rect.x += x_to_change
        self.rect.y += y_to_change

    def update(self):      
        """Keep updating the zombie animation/movement/limit-checks
        """
        self.update_animation()
        self.move()
        if self.rect.left > 960 and self.spawn_side == 0:
            self.kill()
        if self.rect.right < 0 and self.spawn_side == 1:
            self.kill()
        
    def update_animation(self):
        """Animate zombie sprite
        """
        animation_interval = 100
        self.image = self.frames[self.spawn_side][self.frame_index]
        if pygame.time.get_ticks() - self.frame_interval > animation_interval:
            self.frame_interval = pygame.time.get_ticks()
            self.frame_index += 1
        
        if self.frame_index >= len(self.frames[self.spawn_side]):
            self.frame_index = 0

    def draw(self, window):
        """Draw zombie

        Args:
            window (surface): window display surface
        """
        window.blit(self.image, self.rect)