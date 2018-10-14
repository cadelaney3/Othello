
class Player():

    def __init__(self, color):
        self.color = color
        self.score = 2

    def getScore(self):
        return self.score

    def setScore(self, newscore):
        self.score = newscore

    def addScore(self, points):
        self.score = self.score + points

    def getColor(self):
        return self.color
