from brain_games.games.game_gcd import generate_round, GAME_RULE
from brain_games.engine import run_game


def main():
    return run_game(generate_round, GAME_RULE)


if __name__ == '__main__':
    main()
