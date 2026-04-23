import pygame
import colors
import macros
from pygame import Surface, Vector2
from peg import *


def _is_colliding(pegPos: Vector2, mousePos: Vector2) -> bool:
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

def resize_slot(slot: Slot) -> None:
    """Changes slot position according to new window's size"""
    slot.drawPos = Vector2(macros.EDGE.x + (slot.pos.x - 1) * macros.SLOT_GAP,
                           macros.EDGE.y + (slot.pos.y - 1) * macros.SLOT_GAP)

def empty_slot(slot: Slot) -> None:
    """Removes the peg from the slot"""
    slot.peg = None

def populate_slot(slot: Slot, peg: Peg) -> None:
    """Assigns peg to the slot"""
    slot.peg = peg

def is_slot_empty(slot: Slot) -> bool:
    """Returns true if the slot does not contain a peg"""
    return slot.peg == None

def check_mouse_position_on_slot(slot: Slot, mousePos: Vector2) -> bool:
    """Returns true if mouse position is inside the slot"""
    collide = _is_colliding(slot.drawPos, mousePos)
    if slot.peg:
        hover_peg(slot.peg, collide)
    return collide

def check_mouse_input_on_slot(slot: Slot, mousePos: Vector2) -> bool:
    """Returns true if mouse input is inside the slot"""
    collide = _is_colliding(slot.drawPos, mousePos)
    if slot.peg:
        select_peg(slot.peg, collide)
    return collide

def draw_slot(slot: Slot, screen: Surface) -> None:
    """Draws a peg or an empty circle"""
    if not slot.peg:
        pygame.draw.circle(screen, colors.BLACK,
                           slot.drawPos, macros.PEG_RADIUS, macros.SELECTION_RADIUS)
        return
    draw_peg(slot.peg, screen, slot.drawPos)
