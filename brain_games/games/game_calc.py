import random


GAME_RULE = 'What is the result of the expression?'
MIN_VALUE = 0
MAX_VALUE = 100


def count_expression(question):
    elements = question.split()
    number_one, expression, number_two = elements
    if expression == '+':
        return int(number_one) + int(number_two)
    elif expression == '-':
        return int(number_one) - int(number_two)
    else:
        return int(number_one) * int(number_two)


def generate_rounds():
    number_one = random.randint(MIN_VALUE, MAX_VALUE)
    number_two = random.randint(MIN_VALUE, MAX_VALUE)
    expression = random.choice(['+', '-', '*'])
    question = f'{number_one} {expression} {number_two}'
    correct_answer = str(count_expression(question))
    return question, correct_answer
