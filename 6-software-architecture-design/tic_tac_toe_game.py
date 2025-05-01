"""
Main program to set up and run a tic-tac-toe game.
"""

from tic_tac_toe_board import TicTacToeBoard
from tic_tac_toe_view import TextView
from tic_tac_toe_controller import TextController
from tic_tac_toe_controller import MinimaxController


def main():
    """
    Set up and run a Tic-Tac-Toe game between two players. 
    Prints either X won, O won or Tie when the game ends.
    """
    board = TicTacToeBoard()
    view = TextView(board)
    choice = input("Do you want to go first? (y/n): ").strip().lower()

    if choice == "y":
        human_first = True
    else:
        human_first = False

    if human_first:
        first = TextController(board)  # Human goes first (plays 'X')
        second = MinimaxController(board, is_first_player=False)  # AI goes second (plays 'O')
    else:
        first = MinimaxController(board, is_first_player=True)  # AI goes first (plays 'X')
        second = TextController(board)  # Human goes second (plays 'O')

    # first = TextController(board)
    # second = TextController(board)
    total_move = 0

    while total_move < 9:
        view.draw()
        first.move()
        view.draw()
        total_move += 1
        if board.check_win("X") is True:
            print("X won.")
            break
        if total_move == 9:
            print("Tie")
            break
        second.move()
        view.draw()
        total_move += 1
        if board.check_win("O") is True:
            print("O won.")
            break


if __name__ == "__main__":
    main()
