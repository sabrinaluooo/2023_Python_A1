"""
Implements the functionality related to the role of Bird
"""
import random


def getBirdChallenge1Score():
    # Bird's ability number is from rolling a 6-sided dice
    birdFindingAbility = random.randint(1, 6)
    # In the challenge, the score of Bird role would be the Rolling number from two 6-sided dices
    # plus the ability number
    birdChallenge1Number = random.randint(2, 12) + birdFindingAbility
    return birdChallenge1Number

def getBirdChallenge2Score():
    # Bird's ability number is from rolling a 6-sided dice
    birdCatchingAbility = random.randint(1, 6)
    # In the challenge, the score of Bird role would be the Rolling number from two 6-sided dices
    # plus the ability number
    birdChallenge2Number = random.randint(2, 12) + birdCatchingAbility
    return birdChallenge2Number

def getBirdChallenge3Score():
    # Bird's ability number is from rolling a 6-sided dice
    birdFlyingAbility = random.randint(1, 6)
    # In the challenge, the score of Bird role would be the Rolling number from two 6-sided dices
    # plus the ability number
    birdChallenge3Number = random.randint(2, 12) + birdFlyingAbility
    return birdChallenge3Number

def getBirdTotalScore():
    birdTotalScore = getBirdChallenge1Score() + getBirdChallenge2Score() + getBirdChallenge3Score()
    return birdTotalScore

