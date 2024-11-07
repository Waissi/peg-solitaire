from typing import List
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
        for j in range(1, 8):
            for i in range(1, 8):
                if not (i, j) in BLANK:
                    self.grid.append(Slot(i, j))
        self.grid[16].empty()

    def on_resize(self):
        for slot in self.grid:
            slot.on_resize()

    def check_victory(self) -> bool:
        count = 0
        for slot in self.grid:
            if slot.peg:
                count += 1
        return count == 1

    def get_slot(self, pos: Vector2) -> Slot:
        for slot in self.grid:
            if slot.pos == pos:
                return slot

    def check_mouse_position(self, mousePos: Vector2) -> bool:
        hover = False
        for slot in self.grid:
            if slot.check_mouse_position(mousePos):
                hover = True
        return hover

    def check_mouse_input(self, mousePos: Vector2) -> Slot | None:
        clickedSlot = None
        for slot in self.grid:
            if slot.check_mouse_input(mousePos):
                clickedSlot = slot
        return clickedSlot

    def draw(self, screen: Surface):
        for slot in self.grid:
            slot.draw(screen)
