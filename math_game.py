# Huge help from this SO discussion:
# http://stackoverflow.com/questions/26260950/how-can-i-randomly-choose-a-maths-operator-and-ask-recurring-maths-questions-wit


import random
import operator
import time
import numpy


def get_random_operators(div, factors):
    """
    Get mathematical operator. Parameter 'div' allows user to exclude
    division operator.
    """

    operators = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul,
                 '/': operator.truediv}

    # if div preference is false, exclude division
    if div == False:
        operators.pop('/')

    ops = []
    for i in range(factors-1):
        op_key = random.choice(list(operators.keys()))  # must be easier way to randomly same key value pair(s) from dict... randomly sample factors - 1 with replacement
        op_value = operators.get(op_key)
        ops.append({op_key: op_value})
    return ops


def get_random_numbers(N, low, high):
    """Get N random numbers between low and high."""
    return numpy.random.randint(low, high, size=N)


def get_random_equation(div, factors, low, high):
    """
    Generate a random equation with two random numbers and a randomly
    selected math operator.
    """

    if div == False:
        ops.pop('/')

    nums = get_random_numbers(factors, low, high)
    ops = get_operator(div)

    answer = op_math(nums[0], nums[1])
    print('What is {} {} {}?'.format(nums[0], op_str, nums[1]))
    return answer


def evaluate_response(div, factors, low, high):
    """
    Get correct answer and user response, evaluate equivalence.
    """

    answer = random_equation(div, factors, low, high)
    guess = float(input())
    return guess == answer


def quiz(N=10, div=True, factors=2, low=1, high=15):
    """
    Loop through N questions, store number of correct responses.
    """

    print('Welcome. This is a {} question math quiz\n'.format(N))
    score = 0
    for i in range(N):
        correct = evaluate_response(div, factors, low, high)
        if correct:
            score += 1
            print('Correct!\n')
        else:
            print('Incorrect!\n')
        time.sleep(2)
    print('Your score was {}/{}'.format(score, N))
