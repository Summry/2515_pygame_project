import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, scale=1):
        pygame.sprite.Sprite.__init__(self)
        self.animation_index = 0
        self.update_interval = pygame.time.get_ticks()
        
        # Get all images for the bullet
        image = pygame.image.load("images/laser.png").convert_alpha()
        self.image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.speed = 10
        self.direction = direction

    def update(self):
        self.rect.x += (self.direction * self.speed)
        # Delete bullets that go off screen
        if self.rect.right < 0 or self.rect.left > 960:
            self.kill()
        
        # Collision checking
        # if pygame.sprite.spritecollide(player):