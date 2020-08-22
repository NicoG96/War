from War.War import War
import argparse


def main(is_interactive, is_debug):
    War().start_game(is_interactive, is_debug)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--interactive", "-i", action="store_true")
    parser.add_argument("--debug", "-d", action="store_true")
    args = parser.parse_args()
    main(args.interactive, args.debug)