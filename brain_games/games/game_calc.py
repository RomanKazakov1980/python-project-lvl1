import random


GAME_RULE = 'What is the result of the expression?'
RANGE = [0, 100]


def ask_question_get_answer():
    number_one = random.randint(RANGE[0], RANGE[1])
    number_two = random.randint(RANGE[0], RANGE[1])
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
