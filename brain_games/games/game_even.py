import random
from typing import Set, Tuple

GAME_RULE = 'Answer \"yes\" if the number is even, otherwise answer \"no\".'
RANGE = (0, 100)


def even(number):
    return number % 2 == 0


def ask_question_get_answer():
    question = random.randint(RANGE[0], RANGE[1])
    correct_answer = 'yes' if even(question) else 'no'
    return question, correct_answer
