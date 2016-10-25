# Huge help from this SO discussion:
# http://stackoverflow.com/questions/26260950/how-can-i-randomly-choose-a-maths-operator-and-ask-recurring-maths-questions-wit


import random
import operator
import time
import numpy


def get_operator(div=True):
    """Get mathematical operator."""

    ops = {'+': operator.add,
           '-': operator.sub,
           '*': operator.mul,
           '/': operator.truediv}

    # if div preference is false, exclude division
    if div == False:
        ops.pop('/')

    op = random.choice(list(ops.keys()))
    print op
    print ops.get(op)


def get_random_numbers(N, low, high):
    """Get N random numbers between low and high."""
    return numpy.random.randint(low, high, size=N)


def random_equation(div):
    """
    Generate a random equation with two random numbers and a randomly
    selected math operator.
    """

    ops = {'+': operator.add,
       '-': operator.sub,
       '*': operator.mul,
       '/': operator.truediv}

    # if div preference is false, exclude division
    if div == False:
        ops.pop('/')

    num1 = random.randint(0,13)
    num2 = random.randint(1,12)   # exclude 0 to prevent division by zero
    num3 = random.randint(0,49)
    op = random.choice(list(ops.keys()))
    answer = ops.get(op)(num1,num2)
    print('What is {} {} {}?'.format(num1, op, num2))
    return answer


def evaluate_response(div):
    """Get correct answer and user response, evaluate equivalence."""

    answer = random_equation(div)
    guess = float(input())
    return guess == answer


def quiz(N, div=True):
    """Loop through N questions, log number of correct responses."""

    print('Welcome. This is a {} question math quiz\n'.format(N))
    score = 0
    for i in range(N):
        correct = evaluate_response(div)
        if correct:
            score += 1
            print('Correct!\n')
        else:
            print('Incorrect!\n')
        time.sleep(2)
    print('Your score was {}/{}'.format(score, N))
