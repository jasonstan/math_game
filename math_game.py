"""
Game to test user's arithmetic abilities. Allows user to determine 
number of questions in quiz, whether or not division is included in
quiz, the number of factors included in each question of quiz, and both
the low and high of the ranges from which random numbers are chosen
when assembling each new equation.

Author: Jason Stanley
"""


import random
import operator
import time
import numpy


def get_random_operators(ops_exclude, factors):
    """
    Get mathematical operators. Retrieve one less than the number of 
    factors that user has requested for equations. Parameter 'div' 
    allows user to exclude division operator.
    """

    operators = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul,
                 '/': operator.truediv}

    for o in ops_exclude:
        operators.pop(o)

    ops = []
    for i in range(factors-1):
        op_key = random.choice(list(operators.keys()))
        op_value = operators.get(op_key)
        ops.append({op_key: op_value})
    return ops


def get_random_numbers(N, low, high):
    """Get N random numbers between low and high."""
    return numpy.random.randint(low, high, size=N)


def get_random_equation(ops_exclude, factors, low, high):
    """
    Generate a random equation with N random numbers and N-1 randomly
    selected math operators.

    BUG: not yet evaluating order of operations correctly
    """

    nums = get_random_numbers(factors, low, high)
    ops = get_random_operators(ops_exclude, factors)

    answer = nums[0]
    ques = 'What is {}'.format(nums[0])
    for i in range(1, factors):
        answer = ops[i-1].values()[0](answer, nums[i])
        ques = ques + ' ' + ops[i-1].keys()[0] + ' ' + str(nums[i])
    ques = ques + '?'
    
    print ques
    return answer
    

def evaluate_response(ops_exclude, factors, low, high):
    """
    Get correct answer and user response, evaluate equivalence, return
    True if correct, False otherwise, and return correct answer.
    """

    answer = get_random_equation(ops_exclude, factors, low, high)
    guess = float(input())
    return {'correct': guess == answer,
            'answer': answer}


def quiz(N=10, ops_exclude=None, factors=2, low=1, high=15):
    """
    Loop through N questions, store number of correct responses.
    """

    print("Welcome. This is a {} question math quiz. Operators excluded: {}\n"
        .format(N, ops_exclude))
    score = 0
    for i in range(N):
        print('Question #{} of {}:'.format(i+1, N))
        eval = evaluate_response(ops_exclude, factors, low, high)
        correct = eval['correct']
        if correct:
            score += 1
            print('Correct!\n')
        else:
            print('Incorrect! The correct answer is {}.\n'.format(eval['answer']))
        time.sleep(1)
    print('Your score was {}/{}'.format(score, N))
