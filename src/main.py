import pygame
import colors
from macros import *
from game import *


def run():
    """
    Initializes PyGame and variables, then runs the main game loop:\n
    1/ listen to events\n
    2/ update the game\n
    3/ draw the game\n
    4/ refresh at 60FPS
    """

    ####    INIT    ####
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
    pygame.display.set_caption("Peg Solitaire")
    clock = pygame.time.Clock()
    running = True
    victory = False
    game = Game()
    FPS = 60
    ####################

    while running:
        ####    EVENTS  ####
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                # Resize all game elements when window is resized
                on_resize()
                resize_game(game)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if victory:
                    game = Game()
                    victory = False
                else:
                    victory = check_mouse_input(game)
        #####################

        ####    UPDATE  ###
        if not victory:
            update_game(game)
        ###################

        ####    DRAW    ####
        screen.fill(color=colors.BROWN)
        draw_game(game, screen, victory)
        pygame.display.flip()
        ####################

        ####    60FPS   ####
        clock.tick(FPS)
        ####################


if __name__ == "__main__":
    run()
    pygame.quit()
