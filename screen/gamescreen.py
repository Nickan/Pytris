from pygame.locals import *

from view.worldRenderer import *
from view.world import *
from view.inputhandler import *


class GameScreen(object):

    def __init__(self, game):
        self.game = game
        self.world = World(self.game)
        self.worldRenderer = WorldRenderer(self.world)
        self.inputHandler = InputHandler(self.world)

    def update(self, eventList, delta):
        self.inputHandler.update(eventList, delta)
        self.world.update(delta)

    def render(self, DISPLAYSURF):
        self.worldRenderer.render(DISPLAYSURF)


