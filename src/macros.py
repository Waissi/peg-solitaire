from math import floor
import pygame
from pygame import Vector2

WINDOW_SIZE = Vector2(600, 600)
SLOT_GAP = WINDOW_SIZE.y / 8 \
    if WINDOW_SIZE.x > WINDOW_SIZE.y \
    else WINDOW_SIZE.x / 8
PEG_RADIUS = floor(SLOT_GAP / 4)
SELECTION_RADIUS = int(PEG_RADIUS / 4)
EDGE = Vector2(WINDOW_SIZE.x / 2 - SLOT_GAP * 3,
               WINDOW_SIZE.y / 2 - SLOT_GAP * 3)


def on_resize() -> None:
    """Gets new window size and updates macros"""
    global WINDOW_SIZE, SLOT_GAP, PEG_RADIUS, SELECTION_RADIUS, EDGE
    WINDOW_SIZE = Vector2(pygame.display.get_surface().get_size())
    SLOT_GAP = WINDOW_SIZE.y / 8 if WINDOW_SIZE.x > WINDOW_SIZE.y else WINDOW_SIZE.x / 8
    PEG_RADIUS = floor(SLOT_GAP / 4)
    SELECTION_RADIUS = int(PEG_RADIUS / 4)
    EDGE = Vector2(WINDOW_SIZE.x / 2 - SLOT_GAP * 3,
                   WINDOW_SIZE.y / 2 - SLOT_GAP * 3)
