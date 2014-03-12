import pygame

pygame.init()


class Image(object):
    def __init__(self, filePath, conversion_type=''):
        if conversion_type == 'alpha':
            self.image = pygame.image.load(filePath).convert_alpha()
        else:
            self.image = pygame.image.load(filePath).convert()

    def draw(self, DISPLAYSURF, x, y, area=None):
        DISPLAYSURF.blit(self.image, (x, y), area)
