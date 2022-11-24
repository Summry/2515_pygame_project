import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, scale=1, speed=0):
        pygame.sprite.Sprite.__init__(self)
        self.scale = scale
        self.sprite_animation = []
        self.animation_index = 0
        self.action = 0
        self.update_interval = pygame.time.get_ticks()
        temp_list = []

        for i in range(0, 4):
            image = pygame.image.load(f"images/player/stand/{i}.png").convert_alpha()
            image = pygame.transform.scale(image, (int(image.get_width() * self.scale), int(image.get_height() * self.scale)))
            temp_list.append(image)

        self.sprite_animation.append(temp_list)

        temp_list = []
        for i in range(0, 8):
            image = pygame.image.load(f"images/player/walk/{i}.png").convert_alpha()
            image = pygame.transform.scale(image, (int(image.get_width() * self.scale), int(image.get_height() * self.scale)))
            temp_list.append(image)

        self.sprite_animation.append(temp_list)

        self.image = self.sprite_animation[self.action][self.animation_index]
        self.speed = speed
        self.direction = 1
        self.flip_image = False
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)

    def check_limits(self):
        """Make the object stay within the defined limits"""
        if not self.x or not self.y:
            return

        if self.rect.x < self.limits.left:
            self.rect.x = self.limits.left

        if self.rect.x + self.rect.width > self.limits.right:
            self.rect.x = self.limits.right - self.rect.width

    def move(self, move_left, move_right):
        x_to_change = 0
        y_to_change = 0

        if move_left:
            x_to_change = -self.speed
            self.flip_image = True
            self.direction = -1
        if move_right:
            x_to_change = self.speed
            self.flip_image = False
            self.direction = 1

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
