from typing import List, Optional
from pygame import Surface, Vector2
from slot import Slot


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
        self.grid[16].empty()

    def on_resize(self) -> None:
        """Resizes slots and pegs"""
        for slot in self.grid:
            slot.on_resize()

    def check_victory(self) -> bool:
        """Players wins if only peg remains"""
        count = 0
        for slot in self.grid:
            if slot.peg:
                count += 1
        return count == 1

    def get_slot(self, pos: Vector2) -> Slot:
        """Returns slot given a grid position"""
        for slot in self.grid:
            if slot.pos == pos:
                return slot

    def check_mouse_position(self, mousePos: Vector2) -> bool:
        """Checks mouse pos on every slot"""
        hover = False
        for slot in self.grid:
            if slot.check_mouse_position(mousePos):
                hover = True
        return hover

    def check_mouse_input(self, mousePos: Vector2) -> Optional[Slot]:
        """Checks mouse input on every slot"""
        clickedSlot = None
        for slot in self.grid:
            if slot.check_mouse_input(mousePos):
                clickedSlot = slot
        return clickedSlot

    def draw(self, screen: Surface) -> None:
        """Draws every slots"""
        for slot in self.grid:
            slot.draw(screen)
