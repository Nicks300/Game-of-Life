class GameOfLife:
    ROW = 25
    COL = 50

    def __init__(self, initial_board):
        self.initial_board = [row.copy() for row in initial_board]

    def define_new_board(self):
        new_board = [row.copy() for row in self.initial_board]
        for i in range(0, self.ROW):
            for j in range(0, self.COL):
                lived_neighbors = self.count_lived_neighbors(i, j)
                if lived_neighbors > 3 or lived_neighbors < 2:
                    new_board[i][j] = "0"
                elif lived_neighbors == 3:
                    new_board[i][j] = "1"

        self.initial_board = [row.copy() for row in new_board]

    def count_lived_neighbors(self, pos1, pos2):
        lived_neighbors_number = 0
        for i in range(pos1-1, pos1+2):
            for j in range(pos2-1, pos2+2):
                if i != pos1 or j != pos2:
                    if self.initial_board[(i + self.ROW) % self.ROW][(j + self.COL) % self.COL] == "1":
                        lived_neighbors_number += 1
        return lived_neighbors_number

    def display_board(self):
        for elem in self.initial_board:
            for el in elem:
                if el == "1":
                    print("@", end="")
                else:
                    print(".", end="")
            print("\n", end="")



