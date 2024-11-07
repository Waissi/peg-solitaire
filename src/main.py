import pygame
import colors
import macros
from game import Game


pygame.init()
screen = pygame.display.set_mode(macros.WINDOW_SIZE, pygame.RESIZABLE)
pygame.display.set_caption("Peg Solitaire")
clock = pygame.time.Clock()
running = True
victory = False
game = Game()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            macros.on_resize()
            game.on_resize()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if victory:
                game = Game()
                victory = False
            else:
                victory = game.check_mouse_input()
    if not victory:
        game.update()
    screen.fill(color=colors.BROWN)
    game.draw(screen, victory)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
