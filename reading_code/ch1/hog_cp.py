"""CS 61A Presents The Game of Hog."""

from dice_cp import six_sided, four_sided, make_test_dice

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    outcome_sum = 0
    exit_one = False
    while(num_rolls > 0):
        score = dice()
        if(score == 1):
            exit_one = True
        else:
            outcome_sum += score
        num_rolls -= 1
    if(exit_one):
        return 1
    else:
        return outcome_sum

    # END PROBLEM 1


def free_bacon(score):
    """Return the points scored from rolling 0 dice (Free Bacon).

    score:  The opponent's current score.
    """
    assert score < 100, 'The game should be over.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    n = 0
    sum = score*score*score
    while(sum != 0):
        sum = sum//10
        n += 1
    sum = score*score*score
    first_op = 0
    if(n % 2 == 0):
        first_op = 1
    k = 0
    result = 0
    while(sum != 0):
        if(first_op == 1):
            if(k % 2 == 0):
                num = 0-sum % 10
            else:
                num = sum % 10
        else:
            if(k % 2 == 0):
                num = sum % 10
            else:
                num = 0-sum % 10
        result = result+num
        k = k+1
        sum = sum//10
    # print(abs(result))
    return 1+abs(result)
    # END PROBLEM 2


print(free_bacon(45))
