import pygame
import sys

from framework.game import *
from screen.mainscreen import *
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((480, 320), DOUBLEBUF | HWSURFACE, 32)
pygame.display.set_caption('Tetris Clone')

clock = pygame.time.Clock()

game = Game()
game.setScoreManager('res/score.txt')
game.setSettings('res/settings.txt')
game.setScreen(MainScreen(game))

while True:
    eventList = pygame.event.get()
    delta = clock.tick() / 1000.0

    game.update(eventList, delta)
    game.render(DISPLAYSURF)

    pygame.display.flip()

    for event in eventList:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
