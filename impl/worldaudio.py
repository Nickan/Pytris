import pygame


class WorldAudio(object):

    def __init__(self):
        pygame.mixer.music.load('res/gameplaybgm.ogg')
        self.swap = pygame.mixer.Sound('res/swap.wav')
        self.move = pygame.mixer.Sound('res/move.wav')
        self.drop = pygame.mixer.Sound('res/drop.wav')
        self.rotate = pygame.mixer.Sound('res/rotate.wav')
        self.denied = pygame.mixer.Sound('res/denied.wav')
        self.lineDestroyed = pygame.mixer.Sound('res/linedestroyed.wav')
        self.down = pygame.mixer.Sound('res/down.wav')
        self.soundEnable = True

    def setSoundEnable(self, soundEnable):
        self.soundEnable = soundEnable
        if self.soundEnable:
            self.playBgm()
        else:
            self.stopBgm()

    def isSoundEnable(self):
        return self.soundEnable

    def playBgm(self):
        if self.soundEnable:
            pygame.mixer.music.play(-1, 0.0)

    def stopBgm(self):
        pygame.mixer.music.stop()

    def playSwap(self):
        if self.soundEnable:
            self.swap.play()

    def playMove(self):
        if self.soundEnable:
            self.move.play()

    def playRotate(self):
        if self.soundEnable:
            self.rotate.play()

    def playDenied(self):
        if self.soundEnable:
            self.denied.play()

    def playDrop(self):
        if self.soundEnable:
            self.drop.play()

    def playDestroyed(self):
        if self.soundEnable:
            self.lineDestroyed.play()

    def playDown(self):
        if self.soundEnable:
            self.down.play()
