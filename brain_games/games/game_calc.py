import random


GAME_RULE = 'What is the result of the expression?'
MIN_VALUE = 0
MAX_VALUE = 100


def generate_roud():
    number_one = random.randint(MIN_VALUE, MAX_VALUE)
    number_two = random.randint(MIN_VALUE, MAX_VALUE)
    summa = f'{number_one} + {number_two}'
    difference = f'{number_one} - {number_two}'
    composition = f'{number_one} * {number_two}'
    operation_list = {
        summa: number_one + number_two,
        difference: number_one - number_two,
        composition: number_one * number_two,
    }
    question = random.choice(list(operation_list.keys()))
    correct_answer = str(operation_list[question])
    return question, correct_answer
