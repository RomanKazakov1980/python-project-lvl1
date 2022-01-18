from brain_games.games.game_calc import generate_roud, GAME_RULE
from brain_games.engine import run_game


def main():
    return run_game(generate_roud, GAME_RULE)


if __name__ == '__main__':
    main()
