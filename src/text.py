import pygame
import macros
from pygame import Surface


pygame.font.init()


class Text():
    def __init__(self, text: str):
        font = pygame.font.Font(
            pygame.font.get_default_font(), int(macros.WINDOW_SIZE.y / 12))
        self.text = text
        self.texture = font.render(text, False, (0, 0, 0))
        self.pos = (macros.WINDOW_SIZE.x / 2 - self.texture.width / 2, 0)

    def on_resize(self):
        font = pygame.font.Font(
            pygame.font.get_default_font(), int(macros.WINDOW_SIZE.y / 12))
        self.texture = font.render(self.text, False, (0, 0, 0))
        self.pos = (macros.WINDOW_SIZE.x / 2 - self.texture.width / 2, 0)

    def draw(self, screen: Surface):
        screen.blit(self.texture, self.pos)
