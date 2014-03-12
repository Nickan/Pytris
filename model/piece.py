class Piece(object):

    def __init__(self, rotationMatrice):
        self.currentRotation = 0
        self.rotationMatrice = rotationMatrice
        self.str = 'Piece'

    def getPosOfBlock(self, blockPos):
        return self.rotationMatrice[self.currentRotation][blockPos]

    def rotateLeft(self):
        self.currentRotation += 1
        if self.currentRotation > 3:
            self.currentRotation = 0

    def rotateRight(self):
        self.currentRotation -= 1
        if self.currentRotation < 0:
            self.currentRotation = 3

    def setCurrentRotation(self, currentRotation):
        self.currentRotation = currentRotation

    def __str__(self):
        return self.str
