import random


GAME_RULE = 'Answer \"yes\" if the number is even, otherwise answer \"no\".'
RANGE = (0, 100)


def is_even(number):
    return number % 2 == 0


def generate_round():
    question = random.randint(RANGE[0], RANGE[1])
    correct_answer = 'yes' if is_even(question) else 'no'
    return question, correct_answer
