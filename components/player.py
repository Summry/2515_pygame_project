import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, scale=1, speed=0):
        pygame.sprite.Sprite.__init__(self)
        self.is_alive = True
        self.scale = scale
        self.sprite_animation = []
        self.animation_index = 0
        self.action = 0
        self.update_interval = pygame.time.get_ticks()
        
        # Get all images for the player
        animation_category = ['stand', 'walk', 'jump']
        for animation in animation_category:

            temp_list = []
            num_of_files = len(os.listdir(f"images/player/{animation}"))

            for i in range(0, num_of_files):
                image = pygame.image.load(f"images/player/{animation}/{i}.png").convert_alpha()
                image = pygame.transform.scale(image, (int(image.get_width() * self.scale), int(image.get_height() * self.scale)))
                temp_list.append(image)

            self.sprite_animation.append(temp_list)

        self.image = self.sprite_animation[self.action][self.animation_index]
        self.speed = speed
        self.jump = False
        self.in_the_air = True
        self.y_velocity = 0
        self.direction = 1
        self.flip_image = False
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def check_limits(self):
        """Make the object stay within the defined limits"""
        pass

    def move(self, move_left, move_right, gravity=1):
        x_to_change = 0
        y_to_change = 0

        # Move left
        if move_left:
            x_to_change = -self.speed
            self.flip_image = True
            self.direction = -1

        # Move right
        if move_right:
            x_to_change = self.speed
            self.flip_image = False
            self.direction = 1

        # Jump
        if self.jump == True and self.in_the_air == False:
            self.y_velocity = -17
            self.jump = False
            self.in_the_air = True

        # Gravity
        self.y_velocity += gravity
        if self.y_velocity > 10:
            self.y_velocity = 10
        y_to_change += self.y_velocity

        # Check for collision from the ground
        if self.rect.bottom + self.y_velocity > 400:
            y_to_change = 400 - self.rect.bottom
            self.in_the_air = False
        
        self.rect.x += x_to_change
        self.rect.y += y_to_change

    def update_animation(self):
        # Animate
        animation_interval = 100
        # Update the image on the current frame
        self.image = self.sprite_animation[self.action][self.animation_index]
        # Check if a certain time has passed since the last update
        if pygame.time.get_ticks() - self.update_interval > animation_interval:
            self.update_interval = pygame.time.get_ticks()
            self.animation_index += 1
        
        # If animation list is done, reset
        if self.animation_index >= len(self.sprite_animation[self.action]):
            self.animation_index = 0

    def update_action(self, new_action):
        # Check if the new action is different from the previous one
        if new_action != self.action:
            self.action = new_action
            self.animation_index = 0
            self.update_interval = pygame.time.get_ticks()

    def draw(self, window):
        window.blit(pygame.transform.flip(self.image, self.flip_image, False), self.rect)
