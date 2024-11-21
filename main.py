from gameOfLife import gameOfLife
import time
import os
import argparse
import csv

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    filename = args.filename

    board = []

    with open("patterns/"+filename, "r") as pattern_file:
        pattern_reader = csv.reader(pattern_file, delimiter=',')
        for row in pattern_reader:
            board.append(row)

    game = gameOfLife.GameOfLife(board)

    while True:
        game.display_board()
        game.define_new_board()
        time.sleep(0.1)
        os.system('cls' if os.name == 'nt' else 'clear')
