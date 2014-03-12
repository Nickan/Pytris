class ScoreHandler(object):

    def __init__(self, filePath):
        self.filePath = filePath
        self.score = 0
        self.scoreList = []
        self.initFile()

    def initFile(self):
        self.readFile()

        # If the file is blank
        if self.scoreList == []:
            self.initList()

    def readFile(self):
        with open(self.filePath, "r") as scoreFile:
            for line in scoreFile:
                self.scoreList.append(int(line.rstrip("\n")))

    def initList(self):
        count = 0
        while count < 10:
            self.scoreList.append(0)
            count += 1

    def recordFile(self):
        self.addScore()

        with open(self.filePath, 'w') as scoreFile:
            for line in self.scoreList:
                scoreFile.write(str(line) + "\n")

    def addScore(self):
        count = 0
        while count < 10:
            if self.score > self.scoreList[count]:
                self.scoreList.insert(count, self.score)
                # Remove the excess score
                self.scoreList.pop(10)
                break
            count += 1

        print(self.scoreList)

    def setScore(self, score):
        self.score = score

    def getScore(self):
        return self.score

    def incScore(self, score):
        self.score += score

    def getScoreList(self):
        return self.scoreList
