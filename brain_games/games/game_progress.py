import random

GAME_RULE = 'What number is missing in the progression?'


def ask_question_get_answer():
    step = random.randint(1, 5)
    start_collect = random.randint(0, 50)
    collection = list(range(start_collect, start_collect + step * 10, step))
    correct_answer = str(collection[step])
    collection[step] = '..'
    question = collection
    return question, correct_answer
