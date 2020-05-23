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
    return 1+abs(result)
    # END PROBLEM 2


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if(num_rolls == 0):
        return free_bacon(opponent_score)
    else:
        return roll_dice(num_rolls, dice)
    # END PROBLEM 3


# print(free_bacon(47))
# print(take_turn(0, 47))
print(take_turn(3, 0, make_test_dice(4, 6, 1)))
