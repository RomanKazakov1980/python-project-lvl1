#!/usr/bin/env python


import prompt


def run_game(ask_question_get_answer, game_rule):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    print(game_rule)
    for i in range(3):
        question, correct_answer = ask_question_get_answer()
        print(f'Question: {question}')
        answer = prompt.string('You answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f'"{answer}" is wrong answer ;( '
                  f'Correct answer was "{correct_answer}".')
            print(f'Let\'s try again, {user_name}!')
            return
    print(f'Congratulation, {user_name}!')
