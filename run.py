from War.War import War
import argparse


def main(is_interactive):
    War().start_game(is_interactive)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--interactive", "-i", action="store_true")
    args = parser.parse_args()
    main(args.interactive)