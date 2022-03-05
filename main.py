"""
Angel Zarate
Personal Project Wordle

Runs all processes to keep track of wordle
"""
from game import Game


def main():
    curr = Game("short.txt")
    curr.add_word([("f", "grey"), ("r", "green"), ("i", "green"), ("e", "yellow"), ("d", "yellow")])


if __name__ == '__main__':
    main()
