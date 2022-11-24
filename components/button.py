import pygame


class Button:
    """buttons for welcome and game over screen
    """
    def __init__(self, image, x, y, scale) -> None:
        """constructor for buttons

        Args:
            image (image): image surface
            x (float): x-position
            y (float): y-position
            scale (float): scalor to scale image width and height
        """
        w = image.get_width()
        h = image.get_height()

        self.image = pygame.transform.scale(image, (int(w * scale), int(h * scale)))
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


    def draw(self, surface):
        """draw method for buttons

        Args:
            surface (surface): item surface to be drawn

        Returns:
            boolean: if button is clicked or not
        """
        is_clicked = False
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                is_clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))
        return is_clicked