from pygame.locals import *


class InputHandler(object):

    def __init__(self, world):
        self.world = world

    def update(self, eventList, delta):
        self.currentState = self.world.currentState

        for event in eventList:
            # Key down
            if event.type == KEYDOWN:
                self.keyDown(event)
            elif event.type == KEYUP:
                self.keyUp(event)

    def keyDown(self, event):
        if event.key == K_ESCAPE:
            self.world.escapeKeyPressed()

        if not(self.currentState == 'GAME_OVER'):
            if event.key == K_UP:
                self.world.rotatePiece()

            if event.key == K_LEFT:
                self.world.movePieceLeft()

            if event.key == K_RIGHT:
                self.world.movePieceRight()

            if event.key == K_DOWN:
                self.world.downButtonPressed(True)

            if event.key == K_SPACE:
                self.world.dropPiece()

            if event.key == K_LSHIFT:
                self.world.storePiece()

            if event.key == K_r:
                self.world.resume()

    def keyUp(self, event):
        if not(self.currentState == 'GAME_OVER'):
            self.world.downButtonPressed(False)
