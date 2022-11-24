import pygame
from .text import render_text, center_text

pygame.font.init()


class TextBox(pygame.sprite.Sprite):
    """
    Text box class:
    - size is a tuple (dimensions of the box)
    - text_size is the size of the text (default = 24)
    - color is the color of the text (default = black)
    - bgcolor is the background color of the box (default = white)
    """

    def __init__(
        self, size, text="", text_size=24, color=(0, 0, 0), bgcolor=(255, 255, 255)
    ):
        super().__init__()
        self.text = text
        self.text_size = text_size
        self.color = color
        self.bgcolor = bgcolor
        self.image = pygame.Surface(size)
        self.draw()
        self.rect = self.image.get_rect()

    def draw(self):
        """Renders and centers the text"""
        self.image.fill(self.bgcolor)
        text_surface = render_text(self.text, self.text_size, self.color)
        center_text(text_surface, self.image)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = str(value)
