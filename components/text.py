import pygame

pygame.font.init()

default_font = pygame.font.get_default_font()


def render_text(text, size, color=(0, 0, 0)):
    """Returns a surface with rendered text"""
    font = pygame.font.Font(default_font, size)
    return font.render(text, True, color)


def center_text(text_surface, surface):
    """Centers text_surface in surface"""
    text_rect = text_surface.get_rect()
    text_size = text_rect.width, text_rect.height

    surface_rect = surface.get_rect()
    pos_x = (surface_rect.width - text_size[0]) / 2
    pos_y = (surface_rect.height - text_size[1]) / 2
    surface.blit(text_surface, (pos_x, pos_y))
