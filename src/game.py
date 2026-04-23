import pygame
from pygame import Surface, Vector2
from typing import Optional
from board import *
from slot import *
from text import *

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

def resize_game(game: Game) -> None:
    """Resize game elements to new window size"""
    resize_text(game.victoryText)
    resize_board(game.board)

def update_game(game: Game) -> None:
    """Tracks mouse movement"""
    mousePos.x, mousePos.y = Vector2(pygame.mouse.get_pos())
    hover = check_mouse_position_on_board(game.board, mousePos)
    cursor = hand if hover else arrow
    pygame.mouse.set_cursor(cursor)

def check_mouse_input(game: Game) -> Optional[bool]:
    """Handle user's mouse input"""
    slot = check_mouse_input_on_board(game.board, mousePos)
    if not slot:
        game.selectedSlot = None
        return
    if game.selectedSlot:
        if not is_slot_empty(slot):
            game.selectedSlot = slot
            return

        # Middle peg should be removed from board
        middleSlotPos = get_middle_slot_pos(game.selectedSlot, slot)
        if not middleSlotPos:
            game.selectedSlot = None
            return
        middleSlot = get_slot_on_board(game.board, middleSlotPos)
        if is_slot_empty(middleSlot):
            game.selectedSlot = None
            return
        empty_slot(middleSlot)
        peg = game.selectedSlot.peg
        empty_slot(game.selectedSlot)
        populate_slot(slot, peg)
        if check_victory(game.board):
            return True
        return
    if is_slot_empty(slot):
        return
    game.selectedSlot = slot
    return

def draw_game(game: Game, screen: Surface, victory: bool) -> None:
    """Draws game elements and displays 'You win!' if player wins"""
    draw_board(game.board, screen)
    if victory:
        draw_text(game.victoryText, screen)
