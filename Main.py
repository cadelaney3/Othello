from config import BLACK, WHITE, EMPTY
import Player
import Board
import  time
import copy
from threading import Thread


class Othello:

    def __init__(self):
        # ignore for now
        # self.gui = gui.Gui()
        self.game_board = Board.Board(1)
        self.whosturn = BLACK
        self.player = None
        self.keepPlayin = True

    def start(self):
        # ignore for now
        # self.gui.show_game()
        # self.gui.update(self.board.board, 2, 2)

        # get colors of players
        keepPlaying = True
        x = True
        while(x):
            try:
                color = int(input("What color do you want to be? 1 = black, 0 = white: "))
                # test
                if(not(color == 1 or color == 0)):
                    self.setPlayers(g)
                    print("you must select either 1 or 0")

                self.setPlayers(color)

            except Exception as e:
                print("you must select either 1 or 0")
            else:
                x = False

        if (self.player.color == BLACK):
            print("You get to go first.")
        else:
            print("The CPU gets to go first")

        # print the board


        while self.game_board.is_board_full() == False:

            if self.whosturn == self.player.getColor():
                self.player_hand()
                # make sure game isn't done
                # AKA no more moves or board is full
                # note: is_board_full also tests if there are no more moves


                if self.game_board.is_board_full == True:
                    print("Board is full. GAME OVER")
                    print("FINAL SCORE: ")
                    self.showScore()
                    self.keepPlaying = False
            else:
                self.cpu_hand()
                # make sure game isn't done
                # AKA no more moves or board is full
                # note: is_board_full also tests if there are no more moves

                if self.game_board.is_board_full == True:
                    print("Board is full. GAME OVER")
                    print("FINAL SCORE: ")
                    self.showScore()
                    self.keepPlaying = False


        print("Board is full. GAME OVER")
        print("FINAL SCORE: ")
        self.showScore()
        self.keepPlaying = False
        # TODO: ask if they want to play again

    def cpu_hand(self):
        # TODO: change once we develop our cpu class that will
        # play itself without input, for now its just another player
        # TODO: Add a timer
        keep = True
        while (keep):
            print("Computer's Turn: ")
            self.game_board.print_board()
            oldBoard = copy.deepcopy(self.game_board.getBoard())

            listofBoards = self.game_board.next_states(self.whosturn);
            n = 0
            best = 0
            bestNum = 0
            for b in listofBoards:
                howgood = self.alphabeta(b, 4, float("inf"), -float("inf"), True, self.whosturn)
                if(howgood > best):
                    best = howgood
                    bestNum = n
                n = n+1


            lst = self.game_board.get_valid_coordinates(self.whosturn)
            i, j = lst[bestNum]

            if(i != -1 and j != -1):
                move = (i, j)
                # TEST
                print(i, j)
                # 2. Make move
                self.game_board.make_move(move, self.cpu.getColor())
                # 3. Display board
                self.game_board.print_board2()


                #ask the user if they want to confirm the move
                r = True
                while (r):
                    try:
                        doit = int(input("are you sure you want to go There? (1 = yes, 0 = no): "))

                        if (doit == 0):
                            self.game_board.setBoard(oldBoard)

                        elif (doit == 1):
                            whites, blacks = self.game_board.get_scores()
                            self.update_scores(whites, blacks)
                            # 5. Print the score
                            self.showScore()
                            # 6 switch whose turn it is
                            self.endTurn()
                            keep = False
                            r = False
                        else:
                            print("You must enter in a possible number")

                    except Exception as e:
                        print("You must enter in a possible number")
            else:
                self.keepPlayin = False

    def player_hand(self):
        # TODO: Add a timer

        # STEPS
        # 1. Display moves they can make
        # 2. Once move is selected, make the move
        # 3. Display the board after the move is made
        # 4. Update the score
        # 5. Print the score
        # 6. Check to see if the board is full
        # 7. Switch whose turn it is
        keep = True
        while (keep):
            print("Player's Turn: ")
            self.game_board.print_board()
            oldBoard = copy.deepcopy(self.game_board.getBoard())

            i, j = self.display_moves(self.player)


            if (i != -1 and j != -1):
                move = (i, j)
                # 2. Make move
                self.game_board.make_move(move, self.player.getColor())
                # 3. Display board
                self.game_board.print_board2()
                # 4. Update the scores

                # ask the user if they want to confirm the move
                r = True
                while(r):
                    try:
                        doit = int(input("are you sure you want to go There? (1 = yes, 0 = no): "))

                        if (doit == 0):
                            self.game_board.setBoard(oldBoard)

                        elif(doit == 1):
                            whites, blacks = self.game_board.get_scores()
                            self.update_scores(whites, blacks)
                            # 5. Print the score
                            self.showScore()
                            # 6 switch whose turn it is
                            self.endTurn()
                            keep = False
                            r = False
                        else:
                            print("You must enter in a possible number")

                    except Exception as e:
                        print("You must enter in a possible number")




            else:
                self.keepPlayin = False

    def update_scores(self, white_pieces, black_pieces):

        if (self.player.getColor() == BLACK):
            self.player.setScore(black_pieces)
            self.cpu.setScore(white_pieces)
        else:
            self.player.setScore(white_pieces)
            self.cpu.setScore(black_pieces)

    def display_moves(self, current_player):
        # TODO: Do something if they do not have any moves

        # print the coordinates the player can select
        lst = self.game_board.get_valid_coordinates(current_player.getColor())
        n = 1
        for coord in lst:
            i, j = coord
            j = self.get_letter(j)
            print(n, ". ", "(",i+1,",",j,")")

            n = n + 1

        # ask the user what move they want to make
        # TODO: add error input handling
        move = 1000


        x = True

        while(x or move == 0):
            try:
                move = None
                if(n == 1):
                    i = -1
                    j = -1
                    break;
                def check():
                    time.sleep(10)
                    time.process_time()
                    if move != None:
                        return
                    print("Too Slow")


                Thread(target=check).start()

                move = int(input("Enter the move you want to make(you have 10 seconds starting now): "))



                if(move >= n or move<= 0):
                    print("You can't make that move please choose an actual option")

            # return the coordinates of the move to make
                i, j = lst[move - 1]
            except Exception as e:
                print("you cant do that please choose an actual option")
            else:
                x = False;


        return i, j

    # TODO: update once we create the cpu class
    def setPlayers(self, color):
        if (color == BLACK):
            self.player = Player.Player(BLACK)
            self.cpu = Player.Player(WHITE)

        elif (color == WHITE):
            self.player = Player.Player(WHITE)
            self.cpu = Player.Player(BLACK)

        else:
            print("You didn't enter 1 or 0.")

    def endTurn(self):
        if (self.whosturn == BLACK):
            self.whosturn = WHITE
        else:
            self.whosturn = BLACK

    def showScore(self):
        print("//////////////////////////")
        print("| Player: ", self.player.getScore(), "|")
        print("| CPU: ", self.cpu.getScore(), "|")
        print("/////////////////////////")
    def get_letter(self,int):
        if(int == 0):
            return 'A'
        if (int == 1):
            return 'B'
        if (int == 2):
            return 'C'
        if (int == 3):
            return 'D'
        if (int == 4):
            return 'E'
        if (int == 5):
            return 'F'
        if (int == 6):
            return 'G'
        if (int == 7):
            return 'H'

    def alphabeta(self, board, depth, a, b, minOrMax, color):
        if (depth == 0 or board.next_states(color) == []):
            return self.mobility_heuristic(board, color);

        elif (minOrMax == True):
            nexBoards = board.next_states(color)
            for boards in nexBoards:
                a = max(a, self.alphabeta(boards, depth - 1, a, b, False,color))
                if a >= b:
                    break
            return a

        elif (minOrMax == False):
            nexBoards = board.next_states(color)
            for boards in nexBoards:
                b = max(b, self.alphabeta(boards, depth - 1, a, b, True,color))
                if a >= b:
                    break
            return b


    def mobility_heuristic(self, board, color):
        my_color = color
        badguy_color = 0
        if my_color == BLACK:
            badguy_color = WHITE
        else:
            badguy_color = BLACK

        my_moves = board.next_states(my_color)
        badguy_moves = board.get_valid_coordinates(badguy_color)

        position_weights = [[100, -20, 10, 5, 5, 10, -20, 100],
                            [-20, -50, -2, -2, -2, -2, -50, -20],
                            [10, -2, -1, -1, -1, -1, -2, 10],
                            [5, -2, -1, -1, -1, -1, -2, 5],
                            [5, -2, -1, -1, -1, -1, -2, 5],
                            [10, -2, -1, -1, -1, -1, -2, 10],
                            [-20, -50, -2, -2, -2, -2, -50, -20],
                            [100, -20, 10, 5, 5, 10, -20, 100]]
        my_spots = 0
        badguy_spots = 0
        num_empty = 0
        for row in range(8):
            for col in range(8):
                if board.board[row][col] == my_color:
                    my_spots += 1
                elif board.board[row][col] == badguy_color:
                    badguy_spots += 1
                else:
                    num_empty += 1
        return 100 * (my_spots - badguy_spots) / (my_spots + badguy_spots)


def main():
    game = Othello()
    dir(game)
    game.start()


if __name__ == '__main__':
    main()