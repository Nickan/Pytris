import screen.mainscreen

from model.pit import *
from model.piece import *
from framework.vector2i import *
from impl.worldaudio import *
from impl.piecefactory import *
from impl.tetrisscoremanager import *


class World(object):

    def __init__(self, game):
        self.game = game
        self.loadPieces()
        self.x = 0
        self.pit = Pit()
        self.GameStateList = ('START', 'UPDATE_PIECE', 'UPDATE_PIT',
            'CREATE_NEW_PIECE', 'PAUSE_GAME', 'GAME_OVER')
        self.currentState = self.GameStateList[1]
        self.firstStorage = True

        self.scoreManager = self.game.getScoreManager()
        self.pit.setScoreManager(self.scoreManager)

        self.showMenu = False
        self.soundEnable = self.game.isSoundEnable()
        self.audio = WorldAudio()
        self.audio.setSoundEnable(self.game.isSoundEnable())
        self.audio.playBgm()
        self.downSpeed = 1.0
        self.buttonDownSpeed = 15.0
        self.tempX = 0
        self.buttonDown = False

    def update(self, delta):
        # Game loop
        if self.currentState == 'START':
            pass

        elif self.currentState == 'UPDATE_PIECE':
            self.x += (self.downSpeed * delta)

            # For the button down being pressed
            if not(self.buttonDown):
                # Update once every 1 second
                if self.x > 1:
                    self.x = 0

                    # Current piece
                    self.piecePos.y -= 1
                    if not(self.pit.isPieceInsertableAt(self.currentPiece,
                            self.piecePos)):
                        self.piecePos.y += 1
                        self.currentState = 'UPDATE_PIT'
            else:
                self.movePieceDown(delta)

        elif self.currentState == 'UPDATE_PIT':
            self.pit.insertPieceAt(self.currentPiece, self.piecePos)
            self.pit.checkContainer()
            if self.pit.isDestroyed():
                self.pit.setDestroyed(False)
                if self.soundEnable:
                    self.audio.playDestroyed()
            self.firstStorage = True
            self.currentState = 'CREATE_NEW_PIECE'

        elif self.currentState == 'PAUSE_GAME':
            pass

        elif self.currentState == 'CREATE_NEW_PIECE':
            self.createNewPiece()

            if not(self.pit.isPieceInsertableAt(self.currentPiece,
                    self.piecePos)):
                self.currentState = 'GAME_OVER'
            else:
                self.currentState = 'UPDATE_PIECE'

        elif self.currentState == 'GAME_OVER':
            pass

    def rotatePiece(self):
        self.currentPiece.rotateLeft()
        if not(self.pit.isPieceInsertableAt(self.currentPiece, self.piecePos)):
            self.currentPiece.rotateRight()
            if self.soundEnable:
                self.audio.playDenied()
        else:
            if self.soundEnable:
                self.audio.playRotate()

    def movePieceLeft(self):
        self.piecePos.x -= 1
        if not(self.pit.isPieceInsertableAt(self.currentPiece, self.piecePos)):
            self.piecePos.x += 1
            if self.soundEnable:
                self.audio.playDenied()
        else:
            if self.soundEnable:
                self.audio.playMove()

    def movePieceRight(self):
        self.piecePos.x += 1
        if not(self.pit.isPieceInsertableAt(self.currentPiece, self.piecePos)):
            self.piecePos.x -= 1
            self.audio.playDenied()
        else:
            self.audio.playMove()

    def movePieceDown(self, delta):
        self.tempX += (self.buttonDownSpeed * delta)
        if (self.tempX > 1):
            self.tempX = 0
            self.piecePos.y -= 1
            if not(self.pit.isPieceInsertableAt(self.currentPiece,
                self.piecePos)):
                self.piecePos.y += 1
                self.currentState = 'UPDATE_PIT'
                self.audio.playDrop()
            else:
                self.audio.playDown()

    def downButtonPressed(self, buttonDown):
        self.buttonDown = buttonDown

    def dropPiece(self):
        lineCount = 0
        self.audio.playDrop()
        while lineCount < self.pit.getNumOfLines():
            self.piecePos.y -= 1
            if not(self.pit.isPieceInsertableAt(
                self.currentPiece, self.piecePos)):
                self.piecePos.y += 1
                self.currentState = 'UPDATE_PIT'
                break
            lineCount += 1

    def escapeKeyPressed(self):
        # If the menu is currently showing
        if self.showMenu:
            # Go back to main menu
            self.scoreManager.recordFile()
            self.game.getScoreManager().setComboCount(0)
            self.game.setScreen(screen.mainscreen. MainScreen(self.game))
        else:
            # If the game is not over
            if self.currentState != 'GAME_OVER':
                self.showMenu = True
                self.currentState = 'PAUSE_GAME'
            else:
                self.scoreManager.recordFile()
                self.game.getScoreManager().setComboCount(0)
                self.game.setScreen(screen.mainscreen. MainScreen(self.game))

    def storePiece(self):
        # Ensures that swapping or storing piece be done one at a time
        if self.firstStorage:
            self.storeCurrentPiece()
            self.firstStorage = False
            self.audio.playSwap()
        else:
            self.audio.playDenied()

    def resume(self):
        self.showMenu = False
        if self.currentState == 'PAUSE_GAME':
            self.currentState = 'UPDATE_PIECE'

    def createNewPiece(self):
        self.audio.playDrop()
        self.piecePos.set(5, 19)
        self.currentPiece = self.secondPiece
        self.secondPiece = self.thirdPiece
        self.thirdPiece = self.pieceFactory.createRandomPiece()

    def loadPieces(self):
        self.piecePos = Vector2i(5, 19)
        self.pieceFactory = PieceFactory()
        self.currentPiece = self.pieceFactory.createRandomPiece()
        self.secondPiece = self.pieceFactory.createRandomPiece()
        self.thirdPiece = self.pieceFactory.createRandomPiece()
        self.reservedPiece = 'null'

    def storeCurrentPiece(self):
        self.piecePos.x = 5
        self.piecePos.y = 19
        if self.reservedPiece == 'null':
            self.currentPiece.setCurrentRotation(0)
            self.reservedPiece = self.currentPiece
            self.createNewPiece()
        else:
            self.reservedPiece.setCurrentRotation(0)
            self.currentPiece.setCurrentRotation(0)
            tempCurrentPiece = self.currentPiece
            tempReservedPiece = self.reservedPiece
            self.reservedPiece = tempCurrentPiece
            self.currentPiece = tempReservedPiece

    def isShowedMenu(self):
        return self.showMenu

    def getScore(self):
        return self.scoreManager.getScore()

    def getComboCount(self):
        return self.scoreManager.getComboCount()
