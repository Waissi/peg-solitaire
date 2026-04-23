from enum import Enum
import pygame
import colors
import macros
from pygame import Surface, Vector2


class PegState(Enum):
    IDLE = 1
    HOVER = 2
    SELECTED = 3


class Peg():
    def __init__(self):
        self.state = PegState.IDLE

def select_peg(peg: Peg, hover: bool) -> None:
    """Changes peg state"""
    peg.state = PegState.SELECTED if hover else PegState.IDLE

def hover_peg(peg: Peg, hover: bool) -> None:
    """Changes peg state"""
    if peg.state == PegState.SELECTED:
        return
    peg.state = PegState.HOVER if hover else PegState.IDLE

def draw_peg(peg: Peg, screen: Surface, drawPos: Vector2) -> None:
    """Draws peg on screen and a surrounding circle when hovered or selected"""
    pygame.draw.circle(screen, colors.BLACK, drawPos, macros.PEG_RADIUS)
    if peg.state == PegState.SELECTED:
        pygame.draw.circle(screen, colors.YELLOW,
                           drawPos, macros.PEG_RADIUS + 2, macros.SELECTION_RADIUS)
    elif peg.state == PegState.HOVER:
        pygame.draw.circle(screen, colors.GREY,
                           drawPos, macros.PEG_RADIUS + 2, macros.SELECTION_RADIUS)
