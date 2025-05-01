"""
Tic-tac-toe controller.
"""

from abc import ABC, abstractmethod


class TicTacToeController(ABC):
    """
    Initialize the abstract base case for representing the user input of a
    tic-tac-toe game.
    """

    def __init__(self, board):
        """
        Takes an instance of a `TicTacToeBoard` as a parameter and stores
        it as a private instance attribute.

        Args:
            board: An instance of a TicTacToe board class.
        """
        self._board = board

    @property
    def board(self):
        """
        A property that returns the tic-tac-toe board stored in the`TicTacToeView` instance.
        """
        return self._board

    # Define your methods here.
    @abstractmethod
    def move(self):
        """
        Initialize the abstract method for getting input from the user and make an
        appropriate move on the board.
        """


class TextController(TicTacToeController):
    """
    A class representing the user input of a tic-tac-toe game.
    """

    def move(self):
        """
        Prompt user to input a move for the current player and mark the
        corresponding cell on the board.
        It raises ValueError if the input is not in the correct format
        or the indices are out of range.

        """

        try:
            index = input("Type your move here: ")
            row_colmn_index = index.split()
            row_index = int(row_colmn_index[0])
            colmn_index = int(row_colmn_index[1])
            if row_index not in range(3) or colmn_index not in range(3):
                raise ValueError
            self._board.mark(row_index, colmn_index)

        except (IndexError, ValueError):
            print(f"Error: '{index}' are not integers or is out of range.")
            self.move()
        
class MinimaxController(TicTacToeController):
    """
    use minimax algorithm to play as the other player.
    """
    def __init__(self, board, is_first_player=True):
        super().__init__(board)
        self.is_first_player = is_first_player

    def move(self):
        row, col = self.find_best_move(self._board.get_board())
        self.board.mark(row, col)

    def find_best_move(self,board_state):
        """
        loops through all available spots and simulating placing "O" or "X" in that spot
        then call minimax to evaluate the score for that spot. Return the i,j position that produces the most points
        """
        i,j = 0,0
        #print(board_state)
        
        if self.is_first_player:#if ai is "X"
            best_score = -float("inf")
            best_move = None, None
            for i in range(3):
                for j in range(3):
                    if board_state[i][j] == " ":# if is empty
                        board_state[i][j] = "X"#fill it in 
                        curr_score = self.minimax(board_state, 0, False)
                        board_state[i][j] = " "#undo
                        if curr_score > best_score:
                            best_score = curr_score
                            best_move = (i,j)
            return best_move
            
        else:#if ai is "O"
            best_score = float("inf")
            best_move = None, None
            for i in range(3):
                for j in range(3):
                    if board_state[i][j] == " ":# if is empty
                        board_state[i][j] = "O"#fill it in 
                        curr_score = self.minimax(board_state,0, True)
                        board_state[i][j] = " "
                        if curr_score < best_score:
                            best_score = curr_score
                            best_move = (i,j)
            return best_move

            
        
 
    def minimax(self, board_state, depth=0, is_maximizing_player_X= None):
        """
        the minimax function that intakes a board state and calculate the score of that board state
        """
        
        if self._board.check_win("X",board_state):
            return 10 - depth# we want the quickest win so we keep track of depth
        if self._board.check_win("O",board_state):
            return depth - 10
        if self._board.is_full(board_state):
            return 0

        if is_maximizing_player_X:
            maxEval = -float("inf")
            for i in range(3):
                for j in range(3):
                    if board_state[i][j] == " ":
                        board_state[i][j] = "X"
                        curr_eval = self.minimax(board_state, depth + 1, False)
                        board_state[i][j] = " "
                        maxEval = max(maxEval, curr_eval)
            return maxEval
        else:
            minEval = float("inf")
            for i in range(3):
                for j in range(3):
                    if board_state[i][j] == " ":
                        board_state[i][j] = "O"
                        curr_eval = self.minimax(board_state, depth + 1, True)
                        board_state[i][j] = " "
                        minEval = min(minEval, curr_eval)
            return minEval


