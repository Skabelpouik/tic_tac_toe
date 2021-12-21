class GameBoard:
# this class contains all the methods necessary to set up the grid and to display it
    def __init__(self):
        self.board = []
    
    def new_board(self):
        # this method fills the board list with three new lists that represent the rows
        for i in range(3):
            row = []
            for j in range(3):
                row.append("_")
            self.board.append(row)

    def display_board(self):
        # this method display the grid 
        for row in self.board:
            for item in row:
                print(item, end= " ")
            print("")