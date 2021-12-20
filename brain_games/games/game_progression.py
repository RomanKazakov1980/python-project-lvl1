import random
import math


GAME_RULE = 'What number is missing in the progression?'


def ask_question_get_answer():
    step = random.randint(1, 10)
    start_collection = random.randint(0, 50)
    collection = list(range(start_collection, start_collection + step * 10, step))
    correct_answer = str(collection[step])
    collection[step] = '..'
    question = collection
    return question, correct_answer
