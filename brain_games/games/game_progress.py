import random

GAME_RULE = 'What number is missing in the progression?'


MIN_STEP = 1
MAX_STEP = 5
MIN_VALUE = 0
MAX_VALUE = 50


def ask_question_get_answer():
    step = random.randint(MIN_STEP, MAX_STEP)
    start_progression = random.randint(MAX_VALUE, MAX_VALUE)
    progression = list(range(start_progression, start_progression + step * 10, step))
    correct_answer = str(progression[step])
    progression[step] = '..'
    question = (' '.join(map(str, progression)))
    return question, correct_answer
