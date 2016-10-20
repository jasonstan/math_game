# Huge help from this SO discussion:
# http://stackoverflow.com/questions/26260950/how-can-i-randomly-choose-a-maths-operator-and-ask-recurring-maths-questions-wit


import random
import operator
import time


def random_equation():
    """
    Generate a random equation with two random numbers and a randomly
    selected math operator.
    """

    ops = {'+': operator.add,
           '-': operator.sub,
           '*': operator.mul,
           '/': operator.truediv}
    num1 = random.randint(0,12)
    num2 = random.randint(1,10)   # exclude 0 to prevent division by zero
    op = random.choice(list(ops.keys()))
    answer = ops.get(op)(num1,num2)
    print('What is {} {} {}?'.format(num1, op, num2))
    return answer


def evaluate_response():
    """Get correct answer and user response, evaluate equivalence."""

    answer = random_equation()
    guess = float(input())
    return guess == answer


def quiz(N):
    """Loop through N questions, log number of correct responses."""

    print('Welcome. This is a %i question math quiz\n', (N))
    score = 0
    for i in range(N):
        correct = evaluate_response()
        if correct:
            score += 1
            print('Correct!\n')
        else:
            print('Incorrect!\n')
        time.sleep(2)
    print 'Your score was {}/10'.format(score)
