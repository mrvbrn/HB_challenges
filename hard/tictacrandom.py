def tic_tac_random():
    """Play game of tic-tac-toe.

    The human will be X and the computer will be O.

    Loop:
    - Show the board
    - If it's the human's turn, prompt for a position (1-9) and make their move
    - If it's the computer's turn, make any legal move
    - If there's a winner or the board is full, quit the game

    At the end of the game, announce the winner (if any).
    """

    board = setup_board()
    current_player = 'X'
    winner = None
    full = False

    while not winner and not is_board_full(board):
        print()
        print_board(board)
        print()
        if current_player == 'X':
            move = input("Enter move (1-9)> ")
            position = int(move)
            make_move(board, position, 'X')
            current_player = 'O'
        else:
            position = make_random_move(board, 'O')
            print("O played in position %s" % position)
            current_player = 'X'

        winner = find_winner(board)

    if winner:
        print("Congratulations to " + winner)
    else:
        print("How boring, a tie")


def setup_board():
    """Create an empty tic-tac-toe board.

    Create a board as a list-of-rows, each row being a list-of-cells.

    Put '.' in each cell to mark it as empty.

    Return the board.

    >>> setup_board()
    [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    """

    return [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]


def is_board_full(board):
    """Return True is board is full, False otherwise.

    >>> is_board_full([['.', '.', '.'], ['X', '.', 'O'], ['.', '.', '.']])
    False

    >>> is_board_full([['X', 'O', '.'], ['X', 'O', 'X'], ['X', 'O', 'X']])
    False

    >>> is_board_full([['X', 'O', 'X'], ['X', 'X', 'O'], ['O', 'O', 'O']])
    True
    """
    for row in board:
        if "." in row:
            return False
    return True
    
  
    


def make_random_move(board, player):
    """Find an empty cell and play into it.

    player = 'X' or 'O', depending on who should move.

    This should change the board in-place. It should return the
    position (1-9) it played into.

    You don't need to do this randomly -- it can simply use the first empty
    cell it finds.

    >>> board = [['X', 'O', 'X'], ['X', 'X', 'O'], ['O', 'O', '.']]
    >>> make_random_move(board, 'X')
    9

    >>> board
    [['X', 'O', 'X'], ['X', 'X', 'O'], ['O', 'O', 'X']]
    """
    if not is_board_full:
        count = 1
        for row in board:
            for column in row:
                if column != ".":
                    count += 1
        return count





def find_winner(bd):
    """"Given board, determine if winner. Return 'X', 'O', or None if no winner.

    >>> print(find_winner([['.', '.', '.'], ['X', '.', 'O'], ['.', '.', '.']]))
    None

    >>> find_winner([['X', '.', '.'], ['X', '.', 'O'], ['X', '.', '.']])
    'X'

    >>> find_winner([['X', 'O', 'X'], ['O', 'O', 'X'], ['O', 'X', 'X']])
    'X'

    >>> find_winner([['X', '.', 'O'], ['X', 'O', 'O'], ['O', '.', '.']])
    'O'
    """


def print_board(board):
    """Given a board[col][row], print it out.

    >>> print_board([['.', '.', '.'], ['X', '.', 'O'], ['.', '.', '.']])
    . . . 
    X . O 
    . . . 
    """

    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()


def make_move(board, position, player):
    """Play into position 1-9.

    position = 1-9 (top-left, top-middle, top-right ... bottom-right)
    player = 'X' or 'O'

    This should update the board to play there. It does not return anything.

    >>> board = [['X', '.', 'O'], ['X', 'O', 'O'], ['O', '.', '.']]

    >>> make_move(board, 2, 'O')
    >>> board
    [['X', 'O', 'O'], ['X', 'O', 'O'], ['O', '.', '.']]

    >>> make_move(board, 9, 'X')
    >>> board
    [['X', 'O', 'O'], ['X', 'O', 'O'], ['O', '.', 'X']]
    """


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        import doctest

        if doctest.testmod().failed == 0:
            print("\n*** ALL TESTS PASS. FANTASTIC WORK!\n")
    else:
        tic_tac_random()

