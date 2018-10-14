#!/usr/bin/env python
""" board.py for othello game
"""
import copy
from config import BLACK, WHITE, EMPTY, ROW_SIZE, COLUMN_SIZE, TOTAL_SPOTS


class Board:

    def __init__(self, num):

        # TODO: allow config to be switched

        self.board = [[-1, -1, -1, -1, -1, -1, -1, -1],
                      [-1, -1, -1, -1, -1, -1, -1, -1],
                      [-1, -1, -1, -1, -1, -1, -1, -1],
                      [-1, -1, -1, -1, -1, -1, -1, -1],
                      [-1, -1, -1, -1, -1, -1, -1, -1],
                      [-1, -1, -1, -1, -1, -1, -1, -1],
                      [-1, -1, -1, -1, -1, -1, -1, -1],
                      [-1, -1, -1, -1, -1, -1, -1, -1]]

        self.lastBoard = [[]]
        if(BLACK==num):
            self.board[3][4] = BLACK
            self.board[4][3] = BLACK
            self.board[3][3] = WHITE
            self.board[4][4] = WHITE
        else:
            self.board[3][4] = WHITE
            self.board[4][3] = WHITE
            self.board[3][3] = BLACK
            self.board[4][4] = BLACK

    def __getitem__(self, i, j):
        return self.board[i][j]

    def make_move(self, move, color):

        valid_moves = self.get_valid_coordinates(color)
        self.lastBoard = copy.deepcopy(self.board)
        if move in valid_moves:
            self.board[move[0]][move[1]] = color
            for direction in range(1, 9):
                self.change(direction, move, color)
        else:
            # TODO: throw error or something
            print("This is an impossible move.")

    def change(self, direction, position, color):
        # TODO: try to chage it a little/comment alot
        if direction == 1:
            # north
            row_inc = -1
            col_inc = 0
        if direction == 2:
            # northeast
            row_inc = -1
            col_inc = 1
        if direction == 3:
            # east
            row_inc = 0
            col_inc = 1
        if direction == 4:
            # southeast
            row_inc = 1
            col_inc = 1
        if direction == 5:
            # south
            row_inc = 1
            col_inc = 0
        if direction == 6:
            # southwest
            row_inc = 1
            col_inc = -1
        if direction == 7:
            # west
            row_inc = 0
            col_inc = -1
        if direction == 8:
            # northwest
            row_inc = -1
            col_inc = -1

        spots = []
        i = position[0] + row_inc
        j = position[1] + col_inc

        if color == WHITE:
            other = BLACK
        else:
            other = WHITE

        if i in range(8) and j in range(8) and self.board[i][j] == other:
            spots = spots + [(i, j)]
            i = i + row_inc
            j = j + col_inc
            while i in range(8) and j in range(8) and self.board[i][j] == other:
                spots = spots + [(i, j)]
                i = i + row_inc
                j = j + col_inc
            if i in range(8) and j in range(8) and self.board[i][j] == color:
                for pos in spots:
                    self.board[pos[0]][pos[1]] = color

    def get_valid_coordinates(self, color):

        valid_coords = []

        for i in range(8):
            for j in range(8):
                if self.board[i][j] == color:
                    valid_coords += self.check_coordinate(i, j, color)

        # get the duplicates out of the list
        valid_coords = list(set(valid_coords))

        # return the list of valid moves
        return valid_coords

    def check_coordinate(self, i, j, color):
        # initiallize list of coordinates
        list_of_coords = []

        # see whose turn to see what color to check valid moves for
        if color == BLACK:
            other_color = WHITE
        else:
            other_color = BLACK

        # now we must check up, down, left, right, left diagonal, right diagonal

        # up
        # if there is one or more whites above black and then black again
        row_above = i - 1
        if row_above >= 0 and self.board[row_above][j] == other_color:
            while row_above >= 0 and self.board[row_above][j] == other_color:
                row_above -= 1
            if row_above >= 0 and self.board[row_above][j] == EMPTY:
                list_of_coords.append((row_above, j))

        # down
        # if there if a line below spot
        row_below = i + 1
        if row_below <= 7 and self.board[row_below][j] == other_color:
            while row_below <= 7 and self.board[row_below][j] == other_color:
                row_below += 1
            if row_below <= 7 and self.board[row_below][j] == EMPTY:
                list_of_coords.append((row_below, j))

        # left
        column_left = j - 1
        if column_left >= 0 and self.board[i][column_left] == other_color:
            while column_left >= 0 and self.board[i][column_left] == other_color:
                column_left -= 1
            if column_left >= 0 and self.board[i][column_left] == EMPTY:
                list_of_coords.append((i, column_left))

        # right
        column_right = j + 1
        if column_right <= 7 and self.board[i][column_right] == other_color:
            while column_right <= 7 and self.board[i][column_right] == other_color:
                column_right += 1
            if column_right <= 7 and self.board[i][column_right] == EMPTY:
                list_of_coords.append((i, column_right))

        # up and right diagonal
        column_up_right = j + 1
        row_up_right = i - 1
        if (column_up_right <= 7 and row_up_right >= 0
                and self.board[row_up_right][column_up_right] == other_color):
            while (column_up_right <= 7 and row_up_right >= 0
                   and self.board[row_up_right][column_up_right] == other_color):
                column_up_right += 1
                row_up_right -= 1
            if (column_up_right <= 7 and row_up_right >= 0
                    and self.board[row_up_right][column_up_right] == EMPTY):
                list_of_coords.append((row_up_right, column_up_right))

        # up and left diagonal
        row_up_left = i - 1
        column_up_left = j - 1
        if (row_up_left >= 0 and column_up_left >= 0
                and self.board[row_up_left][column_up_left] == other_color):
            while (row_up_left >= 0 and column_up_left >= 0
                   and self.board[row_up_left][column_up_left] == other_color):
                row_up_left -= 1
                column_up_left -= 1
            if (row_up_left >= 0 and column_up_left >= 0
                    and self.board[row_up_left][column_up_left] == EMPTY):
                list_of_coords.append((row_up_left, column_up_left))

        # down and right diagonal
        row_down_right = i + 1
        column_down_right = j + 1
        if (row_down_right <= 7 and column_down_right <= 7
                and self.board[row_down_right][column_down_right] == other_color):
            while (row_down_right <= 7 and column_down_right <= 7
                   and self.board[row_down_right][column_down_right] == other_color):
                row_down_right += 1
                column_down_right += 1
            if (row_down_right <= 7 and column_down_right <= 7
                    and self.board[row_down_right][column_down_right] == EMPTY):
                list_of_coords.append((row_down_right, column_down_right))

        # down and left diagonal
        row_down_left = i + 1
        column_down_left = j - 1
        if (row_down_left <= 7 and column_down_left >= 0
                and self.board[row_down_left][column_down_left] == other_color):
            while (row_down_left <= 7 and column_down_left >= 0
                   and self.board[row_down_left][column_down_left] == other_color):
                row_down_left += 1
                column_down_left -= 1
            if (row_down_left <= 7 and column_down_left >= 0
                    and self.board[row_down_left][column_down_left] == EMPTY):
                list_of_coords.append((row_down_left, column_down_left))

        return list_of_coords

    def get_scores(self):
        black_peices = 0
        white_peices = 0

        for i in range(ROW_SIZE):
            for j in range(COLUMN_SIZE):
                if self.board[i][j] == BLACK:
                    black_peices += 1
                elif self.board[i][j] == WHITE:
                    white_peices += 1

        return white_peices, black_peices

    def is_board_full(self):
        whites, blacks = self.get_scores()

        spots_left = TOTAL_SPOTS - (whites + blacks)

        if spots_left == 0:
            return True
        elif (self.get_valid_coordinates(BLACK) == [] and self.get_valid_coordinates(WHITE) == []):
            return True
        else:
            return False

    def print_board(self):
        print("     A     B     C     D     E    F      G     H")
        for i in range(ROW_SIZE):
            print(i+1, '|', end=" ")
            for j in range(COLUMN_SIZE):
                if self.board[i][j] == BLACK:
                    print(' B ', end=" ")
                elif self.board[i][j] == WHITE:
                    print(' W ', end=" ")
                else:
                    print(' - ', end=" ")
                print('|', end=" ")
            print()

    def print_board2(self):
        print("     A     B     C     D     E    F      G     H")
        for i in range(ROW_SIZE):
            print(i + 1, '|', end=" ")
            for j in range(COLUMN_SIZE):
                if self.board[i][j] == BLACK:
                    if(self.board[i][j] == self.lastBoard[i][j]):
                        print(' B ', end=" ")
                    else:
                        print(' b ', end=" ")
                elif self.board[i][j] == WHITE:
                    if (self.board[i][j] == self.lastBoard[i][j]):
                        print(' W ', end=" ")
                    else:
                        print(' w ', end=" ")
                else:
                    print(' - ', end=" ")
                print('|', end=" ")
            print()

            # TODO: Do we need this?

    def get_changes(self):
        whites, blacks, empty = self.count_stones()
        return (self.board, blacks, whites)

    # TODO: Do we need this?
    # def next_states(self, color):
    #     valid_moves = self.get_valid_moves(color)
    #     for move in valid_moves:
    #         newBoard = deepcopy(self)
    #         newBoard.apply_moves(move, color)
    #     yield newBoard

    def next_states(self, color):

        valid_moves = self.get_valid_coordinates(color)
        board_list = []
        for move in valid_moves:
            newBoard = copy.deepcopy(self)
            newBoard.make_move(move, color)
            board_list.append(newBoard)

        return board_list

    # TODO: Do we need this?
    def get_adjacent_count(self, color):
        """Return how many empty squares there are on the board adjacent to
            the specified color."""
        adjCount = 0
        for x, y in [(a, b) for a in range(8) for b in range(8) if self.board[a][b] == color]:
            for i, j in [(a, b) for a in [-1, 0, 1] for b in [-1, 0, 1]]:
                if 0 <= x + i <= 7 and 0 <= y + j <= 7:
                    if self.board[x + i][y + j] == EMPTY:
                        adjCount += 1
        return adjCount
    def undo(self):
        self.board = self.lastBoard

    def getBoard(self):
        t = [[]]
        t = self.board
        return t

    def setBoard(self, newBoard):
        self.board = newBoard



def main():
    new_board = Board()
    # new_board.print_board()
    # x, y = new_board.get_scores()
    # print(x, y)
    # vc = new_board.get_valid_coordinates(BLACK)
    # print(vc)
    # new_board.make_move((5, 4), BLACK)
    # new_board.print_board()
    # print(new_board.is_board_full())
    # score1, score2 = new_board.get_scores()
    # print(score1, score2)


if __name__ == "__main__":
    main()






