"""
Tic-tac-toe game view.
"""

from abc import ABC, abstractmethod


class TicTacToeView(ABC):
    """
    Initialize the abstract base case for representing the tic-tac-toe board state.
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

    @abstractmethod
    def draw(self):
        """
        Initialize the abstract method for printing the board and stating the next player's turn.
        """


class TextView(TicTacToeView):
    """
    A class that inherits from the 'TicTacToeView' class to implements the view of the
    current board interface.
    """

    def draw(self):
        """
        Print the board, followed by a string stating whose turn it is.
        """
        print(repr(self._board))
        # print(f"It is now {self._board.next_move()}'s turn.")
