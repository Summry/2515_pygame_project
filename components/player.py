import pygame
from .bullet import Bullet
import os

class Player(pygame.sprite.Sprite):
    """Player sprite class

    Args:
        pygame (Sprite): pygame Sprite
    """
    def __init__(self, x, y, scale=1, speed=1):
        pygame.sprite.Sprite.__init__(self)
        self.health = 3
        self.is_alive = True
        self.scale = scale

        # Setup the player animation
        self.frame_interval = pygame.time.get_ticks()
        self.frames = []
        self.frame_index = 0
        self.action = 0
        
        # Get all images for the player - standing, walking, and jumping
        animation_category = ['stand', 'walk', 'jump']
        for animation in animation_category:

            temp_list = []
            num_of_files = len(os.listdir(f"images/player/{animation}"))

            for i in range(0, num_of_files):
                image = pygame.image.load(f"images/player/{animation}/{i}.png").convert_alpha()
                image = pygame.transform.scale(image, (int(image.get_width() * self.scale), int(image.get_height() * self.scale)))
                temp_list.append(image)

            self.frames.append(temp_list)

        # Basic player variables
        self.speed = speed
        self.gravity = 0.75
        self.shoot_cd = 0
        self.y_velocity = 0
        self.direction = 1
        self.in_the_air = True
        self.jump = False

        # Set the player image
        self.flip_image = False
        self.image = self.frames[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        # Create sprite group for bullets
        self.bullet_group = pygame.sprite.Group()

    def check_limits(self):
        """Make the player stay within the defined limits"""
        if self.rect.left < -5:
            self.rect.left = -5
        elif self.rect.right > 970:
            self.rect.right = 970

    def update(self):
        """Update animation and shoot cooldown
        """
        self.update_animation()
        if self.shoot_cd > 0:
            self.shoot_cd -= 1

    def move(self, move_left, move_right):
        """Keep moving the player

        Args:
            move_left (boolean): move left if True
            move_right (boolean): move right if True
        """
        x_to_change = 0
        y_to_change = 0

        # Jump
        if self.jump == True and self.in_the_air == False:
            self.y_velocity = -20
            self.jump = False
            self.in_the_air = True
            # Play jump sound
            jump_sound = pygame.mixer.Sound("audio/jump.mp3")
            jump_sound.set_volume(0.3)
            jump_sound.play()
        
        # Gravity
        self.y_velocity += self.gravity
        if self.y_velocity > 10:
            self.y_velocity = 10
        y_to_change += self.y_velocity

        # Check for collision from the ground
        if self.rect.bottom + self.y_velocity > 400:
            y_to_change = 400 - self.rect.bottom
            self.in_the_air = False

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

        # Update the player position
        self.rect.x += x_to_change
        self.rect.y += y_to_change

        self.check_limits()
        
    def shoot(self):
        """Shoot bullets
        """
        if self.shoot_cd == 0:
            self.shoot_cd = 90

            # Play shoot sound
            shoot_sound = pygame.mixer.Sound("audio/shoot.mp3")
            shoot_sound.set_volume(0.2)
            shoot_sound.play()

            # Create a bullet
            self.bullet = Bullet(self.rect.centerx + (0.7 * self.rect.width * self.direction), self.rect.centery, self.direction, 0.5)
            self.bullet_group.add(self.bullet)
            
    def update_animation(self):
        """Animate the player animation (move, jump)
        """
        
        animation_interval = 100
        # Update the image on the current frame
        self.image = self.frames[self.action][self.frame_index]
        # Check if a certain time has passed since the last update
        if pygame.time.get_ticks() - self.frame_interval > animation_interval:
            self.frame_interval = pygame.time.get_ticks()
            self.frame_index += 1
        
        # If animation list is done, reset
        if self.frame_index >= len(self.frames[self.action]):
            self.frame_index = 0

    def update_action(self, new_action):
        """Updates the action of the player (jump/move/stand)

        Args:
            new_action (string): an action to update the current player action to
        """
        # Check if the new action is different from the previous one
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.frame_interval = pygame.time.get_ticks()

    def draw(self, window):
        """Draw the player

        Args:
            window (surface): the window's display surface
        """
        window.blit(pygame.transform.flip(self.image, self.flip_image, False), self.rect)
        self.bullet_group.draw(window)
        self.bullet_group.update()