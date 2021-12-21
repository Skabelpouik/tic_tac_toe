from class_gameboard import GameBoard


class Game(GameBoard):
# this class contains all the methods needed to run the game
    def new_game(self):
    # this method starts the game, a while loop run the game until there is a winner or a match draw
        self.new_board()
        rounds = 1
        player = "X"
        while True:
            print("Player %s turn" % player)
            self.display_board()
            row, col = list(map(int, input("Enter row and column numbers: ")))
            print("")
            self.board[row][col] = player
            # test if player win
            if self.test_win(player):
                self.display_board()
                print("Player %s wins the game!" % player)
                break
            # test if match draw
            if rounds == 9:
                self.display_board()
                print("Match Draw!")
                break
            # switch the player
            player = self.player_turn(player)
            rounds = rounds + 1

    @classmethod
    def player_turn(self, player):
    # this method switch the current player
        if player == 'O':
            player = "X"
        else:
            player = "O"
        return player

    def test_win(self, player):
    # this methods test if there is a winner
        n = len(self.board)
        # checking rows
        win = True
        for i in range(n):
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win
        # checking column
        win = True
        for i in range(n):
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win
        # checking diagonals top left bottom right
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win
        # cheking diagonals bottom left top right
        win=True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        



