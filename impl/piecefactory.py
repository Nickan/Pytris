import pygame
from framework.vector2i import *
from model.piece import *
from random import *
pygame.init()


class PieceFactory(object):

    def __init__(self):
        self.randomizer = 0

        self.TRotationMatrice = (
        (Vector2i(0, 0), Vector2i(1, 0), Vector2i(-1, 0), Vector2i(0, -1)),
        (Vector2i(0, 0), Vector2i(0, -1), Vector2i(0, 1), Vector2i(-1, 0)),
        (Vector2i(0, 0), Vector2i(-1, 0), Vector2i(1, 0), Vector2i(0, 1)),
        (Vector2i(0, 0), Vector2i(0, 1), Vector2i(0, -1), Vector2i(1, 0))
        )

        self.SRotationMatrice = (
        (Vector2i(0, 0), Vector2i(1, 0), Vector2i(0, -1), Vector2i(-1, -1)),
        (Vector2i(0, 0), Vector2i(0, 1), Vector2i(1, 0), Vector2i(1, -1)),
        (Vector2i(0, 0), Vector2i(1, 0), Vector2i(0, -1), Vector2i(-1, -1)),
        (Vector2i(0, 0), Vector2i(0, 1), Vector2i(1, 0), Vector2i(1, -1))
        )

        self.ZRotationMatrice = (
        (Vector2i(0, 0), Vector2i(-1, 0), Vector2i(0, -1), Vector2i(1, -1)),
        (Vector2i(0, 0), Vector2i(0, 1), Vector2i(-1, 0), Vector2i(-1, -1)),
        (Vector2i(0, 0), Vector2i(-1, 0), Vector2i(0, -1), Vector2i(1, -1)),
        (Vector2i(0, 0), Vector2i(0, 1), Vector2i(-1, 0), Vector2i(-1, -1))
        )

        self.ORotationMatrice = (
        (Vector2i(0, 0), Vector2i(1, 0), Vector2i(0, -1), Vector2i(1, -1)),
        (Vector2i(0, 0), Vector2i(1, 0), Vector2i(0, -1), Vector2i(1, -1)),
        (Vector2i(0, 0), Vector2i(1, 0), Vector2i(0, -1), Vector2i(1, -1)),
        (Vector2i(0, 0), Vector2i(1, 0), Vector2i(0, -1), Vector2i(1, -1))
        )

        self.IRotationMatrice = (
        (Vector2i(0, 0), Vector2i(-1, 0), Vector2i(1, 0), Vector2i(2, 0)),
        (Vector2i(0, 0), Vector2i(0, -1), Vector2i(0, 1), Vector2i(0, 2)),
        (Vector2i(0, 0), Vector2i(-1, 0), Vector2i(1, 0), Vector2i(2, 0)),
        (Vector2i(0, 0), Vector2i(0, -1), Vector2i(0, 1), Vector2i(0, 2))
        )

        self.LRotationMatrice = (
        (Vector2i(0, 0), Vector2i(1, 0), Vector2i(-1, 0), Vector2i(-1, -1)),
        (Vector2i(0, 0), Vector2i(0, -1), Vector2i(0, 1), Vector2i(-1, 1)),
        (Vector2i(0, 0), Vector2i(-1, 0), Vector2i(1, 0), Vector2i(1, 1)),
        (Vector2i(0, 0), Vector2i(0, 1), Vector2i(0, -1), Vector2i(1, -1))
        )

        self.JRotationMatrice = (
        (Vector2i(0, 0), Vector2i(-1, 0), Vector2i(1, 0), Vector2i(1, -1)),
        (Vector2i(0, 0), Vector2i(0, 1), Vector2i(0, -1), Vector2i(-1, -1)),
        (Vector2i(0, 0), Vector2i(1, 0), Vector2i(-1, 0), Vector2i(-1, 1)),
        (Vector2i(0, 0), Vector2i(0, -1), Vector2i(0, 1), Vector2i(1, 1))
        )

    def createPiece(self, pieceType):
        if pieceType == 't':
            return Piece(self.TRotationMatrice)
        elif pieceType == 's':
            return Piece(self.SRotationMatrice)
        elif pieceType == 'z':
            return Piece(self.ZRotationMatrice)
        elif pieceType == 'o':
            return Piece(self.ORotationMatrice)
        elif pieceType == 'i':
            return Piece(self.IRotationMatrice)
        elif pieceType == 'l':
            return Piece(self.LRotationMatrice)
        elif pieceType == 'j':
            return Piece(self.JRotationMatrice)
        else:
            print("No such piece type")

    def createRandomPiece(self):
        self.randomizer += pygame.time.get_ticks()
        seed(self.randomizer)
        pieceNum = randint(0, 6)
        if pieceNum == 0:
            return self.createPiece('t')
        elif pieceNum == 1:
            return self.createPiece('s')
        elif pieceNum == 2:
            return self.createPiece('z')
        elif pieceNum == 3:
            return self.createPiece('o')
        elif pieceNum == 4:
            return self.createPiece('i')
        elif pieceNum == 5:
            return self.createPiece('l')
        elif pieceNum == 6:
            return self.createPiece('j')
