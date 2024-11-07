import pygame
import colors
import macros
from pygame import Surface, Vector2
from peg import Peg


def is_colliding(pegPos: Vector2, mousePos: Vector2) -> bool:
    """Compares distance from mouse position to the center of the slot with the slot's radius"""
    return pegPos.distance_to(mousePos) <= macros.PEG_RADIUS


class Slot():
    """
        pos: Vector2
        drawPos: Vector2
        peg: Peg | None
    """

    def __init__(self, x: int, y: int):
        self.pos = Vector2(x, y)
        self.drawPos = Vector2(macros.EDGE.x + (x - 1) * macros.SLOT_GAP,
                               macros.EDGE.y + (y - 1) * macros.SLOT_GAP)
        self.peg = Peg()

    def on_resize(self) -> None:
        """Changes slot position accroding to new window's size"""
        self.drawPos = Vector2(macros.EDGE.x + (self.pos.x - 1) * macros.SLOT_GAP,
                               macros.EDGE.y + (self.pos.y - 1) * macros.SLOT_GAP)

    def empty(self) -> None:
        """Removes the peg from the slot"""
        self.peg = None

    def populate(self, peg: Peg) -> None:
        """Assigns peg to the slot"""
        self.peg = peg

    def is_empty(self) -> bool:
        """Returns true if the slot does not contain a peg"""
        return self.peg == None

    def check_mouse_position(self, mousePos: Vector2) -> bool:
        """Returns true if mouse position is inside the slot"""
        collide = is_colliding(self.drawPos, mousePos)
        if self.peg:
            self.peg.hover(collide)
        return collide

    def check_mouse_input(self, mousePos: Vector2) -> bool:
        """Returns true if mouse input is inside the slot"""
        collide = is_colliding(self.drawPos, mousePos)
        if self.peg:
            self.peg.select(collide)
        return collide

    def draw(self, screen: Surface) -> None:
        """Draws a peg or an empty circle"""
        if not self.peg:
            pygame.draw.circle(screen, colors.BLACK,
                               self.drawPos, macros.PEG_RADIUS, macros.SELECTION_RADIUS)
            return
        self.peg.draw(screen, self.drawPos)
