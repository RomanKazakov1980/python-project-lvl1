import random

GAME_RULE = 'What number is missing in the progression?'


STEP_VALUE = (1, 5)
RANGE_COLLECTION = (0, 50)


def ask_question_get_answer():
    step = random.randint(STEP_VALUE[0], STEP_VALUE[1])
    start_collect = random.randint(RANGE_COLLECTION[0], RANGE_COLLECTION[10])
    collection = list(range(start_collect, start_collect + step * 10, step))
    correct_answer = str(collection[step])
    collection[step] = '..'
    question = collection
    return question, correct_answer
