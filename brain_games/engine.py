import prompt
from brain_games.cli import welcome_user

ROUNDS = 3


def run_game(ask_question_get_answer, game_rule):
    user_name = welcome_user()
    print(game_rule)
    for i in range(ROUNDS):
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
    print(f'Congratulations, {user_name}!')
