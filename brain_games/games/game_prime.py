import random


GAME_RULE = 'Answer \"yes\" if given number is prime. Otherwise answer \"no\".'
RANGE = (2, 100)


def is_prime(number):
    k = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            k = k + 1
    if k <= 0:
        return number


def ask_question_get_answer():
    question = random.randint(RANGE[0], RANGE[1])
    correct_answer = 'yes' if is_prime(question) else 'no'
    return question, correct_answer
