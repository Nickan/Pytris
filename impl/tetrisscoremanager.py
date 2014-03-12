from framework.scorehandler import ScoreHandler


class TetrisScoreManager(ScoreHandler):

    def __init__(self, filePath):
        super(TetrisScoreManager, self).__init__(filePath)
        self.comboCount = 0
        self.comboScore = 0

    def setComboCount(self, comboCount):
        self.comboCount = comboCount

    def incComboCount(self, inc):
        self.comboCount += inc
        self.incComboScore()

    def getComboCount(self):
        return self.comboCount

    def incComboScore(self):
        self.comboScore = 50 * int(self.comboCount / 2)
        self.score += self.comboScore

    def getComboScore(self):
        return self.comboScore

