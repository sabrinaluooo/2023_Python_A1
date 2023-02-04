"""
This is a two-role game, called Bird and Spider.
This module implements the interactivity with the users.
"""
import game


# Welcome message and game instructions
print("Welcome to the Bird and Spider Game.")
print("Please pay attention to the instruction of the game. \n")
print("You can either choose the role of Bird or the role of Spider.")
print("The bird and spider each has three abilities to compete with each other in every challenge.")
print("There are three challenges that determined by randomly picking up number from 1 to 3.")
print("In the challenge 1, the spider has the ability of changing body color to hide from the bird;")
print("    while the bird has the radar-eyes to find the hidding spider.")
print("In the challenge 2, the spider has the ability of quick jump to avoid the bird; ")
print("    while the bird can catch the jumping spider.")
print("In challenge 3, the spider has the poisonous sting to hurt the bird")
print("while the bird can quickly fly away from the spider.")
print("Each ability of the two roles has a number which is determined by rolling a 6-sided dice.")
print("Each challenge has a score that is the role's ability number plus the number determined by rolling two 6-sided dices.")
print("The win or lose criteria is decided by the difference between the two roles' total scores through the three challenges.")

# Make role-choice
roleChoice = input("Please choose your role. Enter 'b' if choose role of Bird. Enter 's' if choose role of Spider.").lower
if roleChoice == 'b':
    print("great! You choose the Bird role. Let's continue to choose the first challenge.")
elif roleChoice == 's':
    print("great! You choose the Spicer role. Let's continue to choose the first challenge.")


availablePickNumber = [1, 2, 3]
gameName = ""

# Choose the first challenge
firstPickNumber = int(input("Please enter a number from 1 to 3 to play your first challenge or enter 0 to exit "))

if firstPickNumber != 0 and firstPickNumber in availablePickNumber:
    if firstPickNumber == 1:
        firstChallenge = game.WhenChangeColor()
        gameName = "WhenChangeColor"   
    elif firstPickNumber == 2:
        firstChallenge = game.WhenJumping()
        gameName = "WhenJumping"   
    elif firstPickNumber == 3:
        firstChallenge = game.usePoisonouSting()
        gameName = "usePoisonouStin"
    print(f"Let's play the first one, the {gameName} game. Good luck.")
    availablePickNumber.remove(firstPickNumber)
    number1 = availablePickNumber[0]
    number2 = availablePickNumber[1]
    
    # Choose the second challenge
    secondPickNumber = int(input(f"Please enter {number1} or {number2} to play the second challege "))
    if secondPickNumber == 1:
        secondChallenge = game.WhenChangeColor()
        gameName = "WhenChangeColor"
    elif secondPickNumber == 2:
        secondChallenge = game.WhenJumping()
        gameName = "WhenJumping" 
    elif secondPickNumber == 3:
        secondChallenge = game.usePoisonouSting()
        gameName = "usePoisonouStin"
    print(f"Let's play the second one, the {gameName} game. Good luck.")
    availablePickNumber.remove(secondPickNumber)

    # Play the third challenge
    number3 = availablePickNumber[0]
    thirdPickNumber = int(input(f"Please enter {number3} to play the last challege."))
    if thirdPickNumber == 1: 
        thirdChallenge = game.WhenChangeColor()
        gameName = "WhenChangeColor"
    elif thirdPickNumber == 2:
        thirdChallenge = game.WhenJumping()
        ameName = "WhenJumping"
    elif thirdPickNumber == 3:
        thirdChallenge = game.usePoisonouSting()
        gameName = "usePoisonouStin"
    print(f"Let's play the last one, the {gameName} game. Good luck!")

elif firstPickNumber == 0:
        print("Good bye!")
elif firstPickNumber not in availablePickNumber:
    print("Invalid input")
