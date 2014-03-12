from pygame.font import *


class Text(object):

    def __init__(self, text, fontSize, color):
        self.textStr = text
        self.color = color
        self.font = Font('freesansbold.ttf', fontSize)
        self.text = self.font.render(self.textStr, True, self.color)

    def draw(self, DISPLAYSURF, x=0, y=0, textStr=''):
        if textStr != '':
            self.text = self.font.render(str(textStr), True, self.color)
            DISPLAYSURF.blit(self.text, (x, y))
        else:
            DISPLAYSURF.blit(self.text, (x, y))

    def append(self, addText):
        self.textStr = self.textStr + addText
        self.text = self.font.render(self.textStr, True, self.color)

    def setColor(self, color):
        self.text = self.font.render(self.textStr, True, color)
