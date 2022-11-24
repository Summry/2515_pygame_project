import pygame
from .sprite import MySprite

# class Player(MySprite):
#     def __init__(self, limits=None):
#         super().__init__(limits)

#         self.image = pygame.image.load("images/player.png")
#         self.scale = 0.2
#         self.image = pygame.transform.scale(self.image, (
#             self.image.get_width() * self.scale, self.image.get_height() * self.scale
#             ))
#         self.rect = self.image.get_rect()
#         self.rect.center = (480, 350)

#     def draw(self, window):
#         window.blit(self.image, self.rect)



class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, scale=1):
        pygame.sprite.Sprite.__init__(self)

        image = pygame.image.load("images/player.png")
        self.scale = 0.2
        self.image = pygame.transform.scale(image, (
            int(image.get_width() * self.scale), int(image.get_height() * self.scale
        )))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self, window):
        window.blit(self.image, self.rect)