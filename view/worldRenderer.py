from framework.image import *
from framework.text import *


class WorldRenderer(object):

    def __init__(self, world):
        self.world = world

        # Other initialization
        self.allImages = Image('res/gameimages.png', 'alpha')
        self.rectBg = (450, 0, 480, 320)
        self.rectContainer = (0, 0, 178, 380)
        self.rectTransGlassTop = (185, 70, 170, 22)
        self.rectTransGlassBot = (185, 100, 170, 18)
        self.rectPieceSlot = (185, 0, 83, 68)
        self.rectScoreSlot = (270, 0, 150, 43)

        WHITE = (255, 255, 255)
        GREEN = (0, 255, 0)

        self.scoreText = Text(str(0), 15, WHITE)
        self.menuTexts = []
        self.menuTexts.append(Text('Press Esc to go back ',
                                15, WHITE))
        self.menuTexts.append(Text('      to Main Menu', 15, WHITE))
        self.menuTexts.append(Text('    or R to continue', 15, WHITE))

        self.comboText = Text(str(0), 15, WHITE)

    def render(self, DISPLAYSURF):
        self.currentPiece = self.world.currentPiece
        self.secondPiece = self.world.secondPiece
        self.thirdPiece = self.world.thirdPiece
        self.reservedPiece = self.world.reservedPiece
        self.piecePos = self.world.piecePos
        self.pit = self.world.pit
        self.currentState = self.world.currentState

        self.drawBackground(DISPLAYSURF)
        count = 0
        while count < 4:
            # Current piece
            posX = self.currentPiece.getPosOfBlock(count).x
            posY = self.currentPiece.getPosOfBlock(count).y
            self.allImages.draw(DISPLAYSURF,
                150 + (17 * (posX + self.piecePos.x)),
                    13 + (15 * (-posY - self.piecePos.y + 19)),
                        (185, 120 + (15 * count), 17, 15)
                )

            # Second piece
            posX = self.secondPiece.getPosOfBlock(count).x
            posY = self.secondPiece.getPosOfBlock(count).y
            self.allImages.draw(DISPLAYSURF,
                350 + (17 * posX), 95 + (15 * -posY),
                    (185, 120 + (15 * count), 17, 15)
                )

            # Third piece
            posX = self.thirdPiece.getPosOfBlock(count).x
            posY = self.thirdPiece.getPosOfBlock(count).y
            self.allImages.draw(DISPLAYSURF,
                350 + (17 * posX), 170 + (15 * -posY),
                    (185, 120 + (15 * count), 17, 15)
                )

            # Reserved piece
            if self.reservedPiece != 'null':
                posX = self.reservedPiece.getPosOfBlock(count).x
                posY = self.reservedPiece.getPosOfBlock(count).y
                self.allImages.draw(DISPLAYSURF,
                    90 + (17 * posX), 20 + (15 * -posY),
                        (185, 120 + (15 * count), 17, 15)
                    )

            count += 1

        self.drawPit(DISPLAYSURF)

        self.scoreText.draw(DISPLAYSURF, 395, 40, self.world.getScore())

        comboCount = self.world.getComboCount()
        if comboCount > 0:
            self.comboText.draw(DISPLAYSURF, 240, 160, comboCount)

        if self.world.isShowedMenu():
            self.drawMenuText(DISPLAYSURF)

        if self.currentState == 'GAME_OVER':
            self.showGameOverText(DISPLAYSURF)

    def drawPit(self, DISPLAYSURF):
        # My solution to make a nested for loop that operates like in
        # java and c++
        lineNum = 0
        while lineNum < self.pit.getNumOfLines():
            # Supply the current number of the line
            self.drawLines(DISPLAYSURF, lineNum)
            lineNum += 1

    def drawLines(self, DISPLAYSURF, lineNum):
        colNum = 0
        while colNum < self.pit.getNumOfColumns():
            blockID = self.pit.getContainerStatusAt(lineNum, colNum)

            # -1 means empty slot
            if blockID != -1:
                self.allImages.draw(DISPLAYSURF,
                150 + (17 * colNum), 298 - (15 * lineNum),
                    (185, 120 + (15 * blockID), 17, 15)
                )
            colNum += 1

    def drawBackground(self, DISPLAYSURF):
        # Background
        self.allImages.draw(DISPLAYSURF, 0, 0, self.rectBg)
        # Container
        self.allImages.draw(DISPLAYSURF, 145, 7, self.rectContainer)
        # TransUpper glass
        self.allImages.draw(DISPLAYSURF, 150, 10, self.rectTransGlassTop)
        # TransLower glass
        self.allImages.draw(DISPLAYSURF, 150, 296, self.rectTransGlassBot)
        # Reserve piece slot
        self.allImages.draw(DISPLAYSURF, 60, 7, self.rectPieceSlot)
        # Second piece slot
        self.allImages.draw(DISPLAYSURF, 325, 75, self.rectPieceSlot)
        # Third piece slot
        self.allImages.draw(DISPLAYSURF, 325, 150, self.rectPieceSlot)
        # Score slot
        self.allImages.draw(DISPLAYSURF, 325, 25, self.rectScoreSlot)

    def drawMenuText(self, DISPLAYSURF):
        count = 0
        while count < 3:
            self.menuTexts[count].draw(DISPLAYSURF, 155, 150 + (count * 15))
            count += 1

    def showGameOverText(self, DISPLAYSURF):
        count = 0
        while count < 2:
            self.menuTexts[count].draw(DISPLAYSURF, 155, 150 + (count * 15))
            count += 1

