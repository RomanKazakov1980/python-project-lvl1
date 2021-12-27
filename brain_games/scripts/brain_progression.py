#!/usr/bin/env python

from brain_games.games.game_progress import ask_question_get_answer, GAME_RULE
from brain_games.engine import run_game


def main():
    return run_game(ask_question_get_answer, GAME_RULE)


if __name__ == '__main__':
    main()
