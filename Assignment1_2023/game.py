"""
Implements core logic of the game
"""

import bird
import spider


birdWinSum = 0
spiderWinSum = 0

def WhenChangeColor():
    if bird.getBirdChallenge1Score() != spider.getSpiderChallenge1Score():
        if bird.getBirdChallenge1Score() > spider.getSpiderChallenge1Score():
            birdWinSum += 1
        else:
            spiderWinSum += 1
            return spiderWinSum
        return birdWinSum
    
def WhenJumping():
     if bird.getBirdChallenge2Score() != spider.getSpiderChallenge2Score():
        if bird.getBirdChallenge2Score() > spider.getSpiderChallenge2Score():
            birdWinSum += 1
        else:
            spiderWinSum += 1
            return spiderWinSum
        return birdWinSum
    
def usePoisonouSting():
    if bird.getBirdChallenge2Score() != spider.getSpiderChallenge2Score():
        if bird.getBirdChallenge2Score() > spider.getSpiderChallenge2Score():
            birdWinSum += 1
        else:
            spiderWinSum += 1
            return spiderWinSum
        return birdWinSum

def showFinalResult():
    if birdWinSum == 3:
        print("Congradulations, you are a super winner as the role of bird.")
    elif spiderWinSum == 3:
        print("Congradulations, you are a super winner as the role of spider.")
    else: 
        scoreDifference = bird.getBirdTotalScore() - spider.getSpiderTotalScore()
        if scoreDifference == 0:
            print("The final result is a tie.")
        elif scoreDifference >= 20:
            print("Bird wins in high level.")
        elif 10 <= scoreDifference < 20:
            print("Bird wins in medium level.")
        elif 0 < scoreDifference < 10:
            print("Bird wins in low level.")
        elif (-10) < scoreDifference < 0:
            print("Spider wins in low level.")
        elif (-20) < scoreDifference <= (-10):
            print("Spider wins in medium level.")
        elif scoreDifference <= (-20):
            print("Spider wins in high level.")






    