import random


GAME_RULE = 'Answer \"yes\" if given number is prime. Otherwise answer \"no\".'
MIN_VALUE = 2
MAX_VALUE = 100


def is_prime(number):
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True


def ask_question_get_answer():
    question = random.randint(MIN_VALUE, MAX_VALUE)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return question, correct_answer
