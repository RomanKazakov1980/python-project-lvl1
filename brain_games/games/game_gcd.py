import random


GAME_RULE = 'Find the greatest common division of given numbers'
RANGE = [0, 100]


def is_gcd(num_one, num_two):
    if num_two == 0:
        return num_one
    else:
        return is_gcd(num_two, num_one % num_two)


def ask_question_get_answer():
    number_one = random.randint(RANGE[0], RANGE[1])
    number_two = random.randint(RANGE[0], RANGE[1])
    question = f'{number_one} {number_two}'
    correct_answer = str(is_gcd(number_one, number_two))
    return question, correct_answer
