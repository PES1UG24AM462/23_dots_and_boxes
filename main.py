import argparse

from game import DotsAndBoxes


def parse_args():
    parser = argparse.ArgumentParser(description="Play a game of Dots and Boxes.")
    parser.add_argument("--rows", type=int, default=2, help="number of boxes vertically")
    parser.add_argument("--cols", type=int, default=2, help="number of boxes horizontally")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    DotsAndBoxes(args.rows, args.cols).run()
