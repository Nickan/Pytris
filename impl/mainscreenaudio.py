import pygame


class MainScreenAudio(object):
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load('res/bgm.ogg')
        self.click = pygame.mixer.Sound('res/click.wav')
        self.soundEnable = True

    def setSoundEnable(self, soundEnable):
        self.soundEnable = soundEnable
        if self.soundEnable:
            self.playBgm()
        else:
            self.stopBgm()

    def isSoundEnable(self):
        return self.soundEnable

    def buttonClick(self):
        if self.soundEnable:
            self.click.play()

    def playBgm(self):
        if self.soundEnable:
            pygame.mixer.music.play(-1, 0.0)

    def stopBgm(self):
        pygame.mixer.music.stop()
