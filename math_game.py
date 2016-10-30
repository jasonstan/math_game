# Huge help from this SO discussion:
# http://stackoverflow.com/questions/26260950/how-can-i-randomly-choose-a-maths-operator-and-ask-recurring-maths-questions-wit


import random
import operator
import time
import numpy


def get_random_operators(div, factors):
    """
    Get mathematical operators. Retrieve one less than the number of 
    factors that user has requested for equations. Parameter 'div' 
    allows user to exclude division operator.
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
        op_key = random.choice(list(operators.keys()))
        op_value = operators.get(op_key)
        ops.append({op_key: op_value})
    return ops


def get_random_numbers(N, low, high):
    """Get N random numbers between low and high."""
    return numpy.random.randint(low, high, size=N)


def get_random_equation(div, factors, low, high):
    """
    Generate a random equation with N random numbers and N-1 randomly
    selected math operators.
    """

    nums = get_random_numbers(factors, low, high)
    ops = get_random_operators(div, factors)

    answer = nums[0]
    ques = 'What is {}'.format(nums[0])
    for i in range(factors-1):
        answer = ops[i].values()[0](answer, nums[i])
        ques = ques + ' ' + ops[i].keys()[0] + ' ' + str(nums[i])
    ques = ques + '?'
    
    print ques
    return answer
    

def evaluate_response(div, factors, low, high):
    """
    Get correct answer and user response, evaluate equivalence, return
    True if correct, False otherwise, and return correct answer.
    """

    answer = get_random_equation(div, factors, low, high)
    guess = float(input())
    return {'correct': guess == answer,
            'answer': answer}


def quiz(N=10, div=True, factors=2, low=1, high=15):
    """
    Loop through N questions, store number of correct responses.
    """

    print('Welcome. This is a {} question math quiz\n'.format(N))
    score = 0
    for i in range(N):
        eval = evaluate_response(div, factors, low, high)
        correct = eval['correct']
        if correct:
            score += 1
            print('Correct!\n')
        else:
            print('Incorrect! The correct answer is {}.\n'.format(eval['answer']))
        time.sleep(2)
    print('Your score was {}/{}'.format(score, N))
