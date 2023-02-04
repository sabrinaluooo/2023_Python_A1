"""
Implements the functionality related to the role of Spider
"""
import random


def getSpiderChallenge1Score():
    # Spider's ability number is from rolling a 6-sided dice
    spiderChangeColorAbility = random.randint(1, 6)
    # In the challenge, the score of Bird role would be the Rolling number from two 6-sided dices
    # plus the ability number
    spiderChallenge1Number = random.randint(2, 12) + spiderChangeColorAbility
    return spiderChallenge1Number

def getSpiderChallenge2Score():
    # Bird's ability number is from rolling a 6-sided dice
    spiderJumpAbility = random.randint(1, 6)
    # In the challenge, the score of Bird role would be the Rolling number from two 6-sided dices
    # plus the ability number
    spiderChallenge2Number = random.randint(2, 12) + spiderJumpAbility
    return spiderChallenge2Number

def getSpiderChallenge3Score():
    # Bird's ability number is from rolling a 6-sided dice
    spiderPoisonStingAbility = random.randint(1, 6)
    # In the challenge, the score of Bird role would be the Rolling number from two 6-sided dices
    # plus the ability number
    spiderChallenge3Number = random.randint(2, 12) + spiderPoisonStingAbility
    return spiderChallenge3Number

def getSpiderTotalScore():
    spiderTotalScore = getSpiderChallenge1Score() + getSpiderChallenge2Score() + getSpiderChallenge3Score()
    return spiderTotalScore
