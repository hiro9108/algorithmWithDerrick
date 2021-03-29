"""
Exercise: Rolling Dice. (Exhaustive Search)

@Write a recursive function rollDice that accepts an int representing a number of 6-sided dice to roll,
and output all possible combinations of values that could appear on the dice.

@parameter n: the number of dice.
if n = 2: [1,1], [1,2], [1,3], ... [6,6]
"""
def rollDiceHelper(n: int, choices: list):
    if n == 0:
        print(choices)
    else:
        # recursive case
        for i in range(6):
            # choose one
            choices.append(i+1)
            # explore
            rollDiceHelper(n-1, choices)
            # un-choose one
            choices.pop()
    return

def rollDice(n: int):
    choices = []
    rollDiceHelper(n, choices)

# rollDice(2)


def rollDiceSumHelper(n: int, desiredSum: int, choices: list):
    if n == 0:
        if sum(choices) == desiredSum:
            print(choices)
    else:
        for i in range(6):
            choices.append(i+1)
            rollDiceSumHelper(n-1, desiredSum, choices)
            choices.pop()


def rollDiceSum(n: int, desiredSum: int):
    choices = []
    rollDiceSumHelper(n, desiredSum, choices)

rollDiceSum(2, 10)