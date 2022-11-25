import pygame

class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y, scale=0.2, speed=0):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.transform.flip(pygame.image.load("images/zombie2.png").convert_alpha(), flip_x=True, flip_y=False)
        self.scale = scale
        self.speed = speed
        self.direction = 1
        self.flip_image = False
        self.image = pygame.transform.scale(image, (
            int(image.get_width() * self.scale), int(image.get_height() * self.scale
        )))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

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

    def draw(self, window):
        window.blit(pygame.transform.flip(self.image, self.flip_image, False), self.rect)
