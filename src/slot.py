import pygame
import colors
import macros
from pygame import Surface, Vector2
from peg import Peg


def is_colliding(pegPos: Vector2, mousePos: Vector2) -> bool:
    return pegPos.distance_to(mousePos) <= macros.PEG_RADIUS


class Slot():
    """
        pos: Vector2
        drawPos: Vector2
        peg: Peg
    """

    def __init__(self, x: int, y: int):
        self.pos = Vector2(x, y)
        self.drawPos = Vector2(macros.EDGE.x + (x - 1) * macros.SLOT_GAP,
                               macros.EDGE.y + (y - 1) * macros.SLOT_GAP)
        self.peg = Peg()

    def on_resize(self):
        self.drawPos = Vector2(macros.EDGE.x + (self.pos.x - 1) * macros.SLOT_GAP,
                               macros.EDGE.y + (self.pos.y - 1) * macros.SLOT_GAP)

    def empty(self):
        self.peg = None

    def populate(self, peg: Peg):
        self.peg = peg

    def is_empty(self) -> bool:
        return self.peg == None

    def check_mouse_position(self, mousePos: Vector2):
        collide = is_colliding(self.drawPos, mousePos)
        if self.peg:
            self.peg.hover(collide)
        return collide

    def check_mouse_input(self, mousePos: Vector2):
        collide = is_colliding(self.drawPos, mousePos)
        if self.peg:
            self.peg.select(collide)
        return collide

    def draw(self, screen: Surface):
        if not self.peg:
            pygame.draw.circle(screen, colors.BLACK,
                               self.drawPos, macros.PEG_RADIUS, macros.SELECTION_RADIUS)
            return
        self.peg.draw(screen, self.drawPos)
