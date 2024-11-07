from typing import Optional
import pygame
from pygame import Surface, Vector2
from board import Board
from slot import Slot
from text import Text

mousePos = Vector2()
arrow = pygame.SYSTEM_CURSOR_ARROW
hand = pygame.SYSTEM_CURSOR_HAND


def is_movement_allowed(slot1: Slot, slot2: Slot) -> bool:
    """Only 2 slots vertical or horizontal movements are allowed"""
    return (abs(slot1.pos.x - slot2.pos.x) == 2 and slot1.pos.y == slot2.pos.y) \
        or (abs(slot1.pos.y - slot2.pos.y) == 2 and slot1.pos.x == slot2.pos.x)


def get_middle_slot_pos(slot1: Slot, slot2: Slot) -> Optional[Vector2]:
    """Returns position of the slot to be emptied if the movement is allowed"""
    if not is_movement_allowed(slot1, slot2):
        return
    if slot1.pos.x == slot2.pos.x:
        # movement is vertical
        if slot1.pos.y > slot2.pos.y:
            # movement is upward
            return Vector2(slot1.pos.x, slot1.pos.y - 1)
        # movement is downward
        return Vector2(slot1.pos.x, slot1.pos.y + 1)
    elif slot1.pos.y == slot2.pos.y:
        # movement is horizontal
        if slot1.pos.x > slot2.pos.x:
            # movement is on the left
            return Vector2(slot1.pos.x - 1, slot1.pos.y)
        # movement is on the right
        return Vector2(slot1.pos.x + 1, slot1.pos.y)


class Game():
    """
        board: Board
        selectedSlot: Slot?
    """

    def __init__(self):
        self.board = Board()
        self.selectedSlot: Slot = None
        self.victoryText = Text('You Win!')

    def on_resize(self) -> None:
        """Resize game elements to new window size"""
        self.victoryText.on_resize()
        self.board.on_resize()

    def update(self) -> None:
        """Tracks mouse movement"""
        mousePos.x, mousePos.y = Vector2(pygame.mouse.get_pos())
        hover = self.board.check_mouse_position(mousePos)
        cursor = hand if hover else arrow
        pygame.mouse.set_cursor(cursor)

    def check_mouse_input(self) -> Optional[bool]:
        """Handle user's mouse input"""
        slot = self.board.check_mouse_input(mousePos)
        if not slot:
            self.selectedSlot = None
            return
        if self.selectedSlot:
            if not slot.is_empty():
                self.selectedSlot = slot
                return

            # Middle peg should be removed from board
            middleSlotPos = get_middle_slot_pos(self.selectedSlot, slot)
            if not middleSlotPos:
                self.selectedSlot = None
                return
            middleSlot = self.board.get_slot(middleSlotPos)
            if middleSlot.is_empty():
                self.selectedSlot = None
                return
            middleSlot.empty()
            peg = self.selectedSlot.peg
            self.selectedSlot.empty()
            slot.populate(peg)
            if self.board.check_victory():
                return True
            return
        if slot.is_empty():
            return
        self.selectedSlot = slot
        return

    def draw(self, screen: Surface, victory: bool) -> None:
        """Draws game elements and displays 'You win!' if player wins"""
        self.board.draw(screen)
        if victory:
            self.victoryText.draw(screen)
