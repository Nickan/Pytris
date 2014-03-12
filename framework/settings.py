class Settings(object):

    def __init__(self, fileName):
        self.fileName = fileName

    def getSoundSettings(self):
        soundEnable = 'True'
        with open(self.fileName, 'r') as fileSettings:
            for line in fileSettings:
                soundEnable = line

        if soundEnable == 'True':
            return True
        return False

    def setSoundSettings(self, soundEnable):
        with open(self.fileName, 'w') as fileSettings:
            fileSettings.write(str(soundEnable))

    # More to come...
