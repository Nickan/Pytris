from pygame.locals import *
from screen.gamescreen import *
from framework.image import *
from impl.mainscreenaudio import *


class MainScreen(object):
    def __init__(self, game):
        self.game = game
        self.allImages = Image('res/menuimages.png', 'alpha')
        self.START_X = 250
        self.START_Y = 70
        self.START_WIDTH = 216
        self.START_HEIGHT = 33
        self.EXIT_WIDTH = 77
        self.rectStart = (5, 325, self.START_WIDTH, self.START_HEIGHT)
        self.rectExit = (143, 360, self.EXIT_WIDTH, self.START_HEIGHT)
        self.rectBg = (0, 0, 480, 320)

        self.soundOptionX = 10
        self.soundOptionY = 255
        self.rectSoundDisable = (0, 400, 55, 55)
        self.rectSoundOption = (55, 400, 55, 55)
        self.adjNum = 40

        self.audio = MainScreenAudio()
        self.audio.setSoundEnable(self.game.isSoundEnable())
        self.audio.playBgm()
        self.initScoreList()

    def update(self, eventList, delta):
        for event in eventList:
            if event.type == MOUSEBUTTONDOWN:
                self.mouseDown(event.pos)
            elif event.type == MOUSEBUTTONUP:
                self.mouseUp(event.pos)

    def render(self, DISPLAYSURF):
        # Background
        self.allImages.draw(DISPLAYSURF, 0, 0, self.rectBg)

        # Start button
        self.allImages.draw(DISPLAYSURF, self.START_X, self.START_Y,
            self.rectStart)

        # Exit button
        self.allImages.draw(DISPLAYSURF, self.START_X, self.START_Y
            + self.adjNum, self.rectExit)

        # Sound Option
        self.allImages.draw(DISPLAYSURF, self.soundOptionX, self.soundOptionY,
            self.rectSoundOption)

        # Disable image
        if not(self.audio.isSoundEnable()):
            self.allImages.draw(DISPLAYSURF, self.soundOptionX,
            self.soundOptionY, self.rectSoundDisable)

        self.drawScoreList(DISPLAYSURF)

    def mouseDown(self, pos):
        mouseX, mouseY = pos
        # Start button
        if (mouseX > self.START_X and mouseX < self.START_X +
            self.START_WIDTH) and (mouseY > self.START_Y and
                mouseY < self.START_Y + self.START_HEIGHT):
            self.audio.buttonClick()

        # Exit button
        if (mouseX > self.START_X and mouseX < self.START_X +
            self.EXIT_WIDTH) and (mouseY > self.START_Y + self.adjNum and
                mouseY < self.START_Y + self.START_HEIGHT + self.adjNum):
            self.game.exit()
            self.audio.buttonClick()

        # Sound button
        if (mouseX > self.soundOptionX and mouseX < self.soundOptionX +
            self.rectSoundOption[2]) and (mouseY > self.soundOptionY and
            mouseY < self.soundOptionY + self.rectSoundOption[3]):
                enable = self.audio.isSoundEnable()
                self.audio.setSoundEnable(not(enable))
                self.game.setSoundEnable(self.audio.isSoundEnable())

    def mouseUp(self, pos):
        mouseX, mouseY = pos
        # Start button
        if (mouseX > self.START_X and mouseX < self.START_X +
            self.START_WIDTH) and (mouseY > self.START_Y and
                mouseY < self.START_Y + self.START_HEIGHT):
            self.audio.stopBgm()
            self.game.setScreen(GameScreen(self.game))
            self.game.getScoreManager().setScore(0)

    def initScoreList(self):
        scoreManager = self.game.getScoreManager()
        self.scoreList = scoreManager.getScoreList()

        WHITE = (255, 255, 255)

        self.textList = []
        count = 0
        while count < 10:
            self.textList.append(Text(str(self.scoreList[count]), 12, WHITE))
            count += 1

    def drawScoreList(self, DISPLAYSURF):
        count = 0
        while count < 10:
            self.textList[count].draw(DISPLAYSURF, 70, 155 + (15 * count))
            count += 1
