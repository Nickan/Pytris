class Pit(object):

    def __init__(self):
        self.numOfColumns = 10
        self.numOfLines = 23
        self.clear()
        self.destroy = False

    def checkContainer(self):
        lineNum = 0
        linesDestroyed = 0
        while lineNum < self.numOfLines:
            if self.isLineFull(lineNum):
                self.container.pop(lineNum)
                self.createNewLine()
                linesDestroyed += 1
            else:
                lineNum += 1

        self.setLineDestroyed(linesDestroyed)

    def setLineDestroyed(self, linesDestroyed):
        if linesDestroyed == 1:
            self.scoreManager.incScore(10)
        elif linesDestroyed == 2:
            self.scoreManager.incScore(25)
        elif linesDestroyed == 3:
            self.scoreManager.incScore(50)
        elif linesDestroyed == 4:
            self.scoreManager.incScore(100)
        else:
            pass

        if linesDestroyed != 0:
            self.scoreManager.incComboCount(1)
            self.destroy = True
        else:
            self.scoreManager.setComboCount(0)

    def isDestroyed(self):
        return self.destroy

    def setDestroyed(self, destroy):
        self.destroy = destroy

    def isLineFull(self, lineNum):
        full = True
        colNum = 0
        while colNum < self.numOfColumns:
            # Prevent checking out of range value
            # If there is an empty slot, it is still not full
            if self.getContainerStatusAt(lineNum, colNum) == -1:
                full = False
                break
            colNum += 1
        return full

    def isPieceInsertableAt(self, piece, piecePos):
        isInsertable = True
        count = 0
        while count < 4:
            blockPosX = piece.getPosOfBlock(count).x
            blockPosY = piece.getPosOfBlock(count).y
            colNum = blockPosX + piecePos.x
            lineNum = blockPosY + piecePos.y

            # Checking if the piece can be placed
            if ((colNum >= 0 and colNum < self.numOfColumns) and
                # Just to prevent checking above the container
                (lineNum >= 0 and lineNum < self.numOfLines)):
                if (self.getContainerStatusAt(lineNum, colNum) != -1):
                    isInsertable = False
            else:
                isInsertable = False

            count += 1
        return isInsertable

    def insertPieceAt(self, piece, piecePos):
        blockNum = 0
        while blockNum < 4:
            blockPos = piece.getPosOfBlock(blockNum)
            colNum = blockPos.x + piecePos.x
            lineNum = blockPos.y + piecePos.y

            self.setContainerStatusAt(lineNum, colNum, blockNum)
            blockNum += 1

    def setContainerStatusAt(self, line, colNum, statusNum):
        self.container[line][colNum] = statusNum

    def getContainerStatusAt(self, line, colNum):
        return self.container[line][colNum]

    def clear(self):
        self.container = []
        lineNum = 0
        while lineNum < self.numOfLines:
            self.createNewLine()
            lineNum += 1

    def createNewLine(self):
        tempContainer = []
        colNum = 0
        while colNum < self.numOfColumns:
            tempContainer.append(-1)
            colNum += 1

        self.container.append(tempContainer)

    def getNumOfLines(self):
        return self.numOfLines

    def getNumOfColumns(self):
        return self.numOfColumns

    def setScoreManager(self, scoreManager):
        self.scoreManager = scoreManager
