from pygame import *
from sys import *
from impl.tetrisscoremanager import *
from framework.settings import *


class Game(object):
    def __init__(self):
        self.screen = 'null'
        self.soundEnable = True

    def setScreen(self, screen):
        self.screen = screen

    def getScreen(self):
        return self.screen

    def update(self, eventList, delta):
        self.screen.update(eventList, delta)

    def render(self, DISPLAYSURF):
        self.screen.render(DISPLAYSURF)

    def setScoreManager(self, fileName):
        self.scoreManager = TetrisScoreManager(fileName)

    def getScoreManager(self):
        return self.scoreManager

    def setSettings(self, fileName):
        self.settings = Settings(fileName)
        # Setting up the sound
        self.soundEnable = self.settings.getSoundSettings()

    def setSoundEnable(self, enable):
        self.soundEnable = enable

        # Saving the sound setting in text file
        self.settings.setSoundSettings(self.soundEnable)

    def isSoundEnable(self):
        return self.soundEnable

    def exit(self):
        quit()
        exit()

