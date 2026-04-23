from typing import List, Optional
from pygame import Surface, Vector2
from slot import *


BLANK = [
    (1, 1), (1, 2), (2, 1), (2, 2),
    (6, 1), (6, 2), (7, 1), (7, 2),
    (1, 6), (1, 7), (2, 6), (2, 7),
    (6, 6), (6, 7), (7, 6), (7, 7)
]


class Board():
    """
        grid: List[Slot]
    """

    def __init__(self):
        self.grid: List[Slot] = []
        # Building the grid
        for j in range(1, 8):
            for i in range(1, 8):
                if not (i, j) in BLANK:
                    self.grid.append(Slot(i, j))
        # Central slot is empty
        empty_slot(self.grid[16])

def resize_board(board: Board) -> None:
    """Resizes slots and pegs"""
    for slot in board.grid:
        resize_slot(slot)

def check_victory(board: Board) -> bool:
    """Players wins if only peg remains"""
    count = 0
    for slot in board.grid:
        if slot.peg:
            count += 1
    return count == 1

def get_slot_on_board(board: Board, pos: Vector2) -> Slot:
    """Returns slot given a grid position"""
    for slot in board.grid:
        if slot.pos == pos:
            return slot

def check_mouse_position_on_board(board: Board, mousePos: Vector2) -> bool:
    """Checks mouse pos on every slot"""
    hover = False
    for slot in board.grid:
        if check_mouse_position_on_slot(slot, mousePos):
            hover = True
    return hover

def check_mouse_input_on_board(board: Board, mousePos: Vector2) -> Optional[Slot]:
    """Checks mouse input on every slot"""
    clickedSlot = None
    for slot in board.grid:
        if check_mouse_input_on_slot(slot, mousePos):
            clickedSlot = slot
    return clickedSlot

def draw_board(board: Board, screen: Surface) -> None:
    """Draws every slots"""
    for slot in board.grid:
        draw_slot(slot, screen)
