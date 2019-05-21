from random import sample
from string import ascii_lowercase as lowercase
import time


class GameLostException(Exception):
    """Raise when game is lost."""


class GameWonException(Exception):
    """Raise when game is won."""


class Cell(object):
    """A cell in the board grid."""

    NEIGHBOR_DELTAS = [(-1, -1), (0, -1), (+1, -1),
                       (-1, 0),           (+1, 0),
                       (-1, +1), (0, +1), (+1, +1)]

    def __init__(self, board, col, row):
        self.board = board     # board object
        self.col = col         # 0 .. width-1
        self.row = row         # 0 .. height-1
        self.mine = False      # Is this a mine?
        self.revealed = False  # Is this cell revealed
        self.number = 0        # Number of mine neighbors

    def __repr__(self):
        return "<%s,%s-%s%s-%s>" % (
            self.col,
            self.row,
            '*' if self.mine else '',
            'R' if self.revealed else '',
            self.number)

    def neighbors(self):
        """Return valid neighbor cells for a cell."""

        return [self.board.cells[self.row + r][self.col + c]
                for c, r in self.NEIGHBOR_DELTAS
                if (0 <= self.col + c < self.board.width and
                    0 <= self.row + r < self.board.height)]

    def click(self):
        """Click on a cell.

        - If it's a mine, reveal all cells and end the game in loss.
        - Check and reveal the neighbors.
          If all cells are revealed but mines, end in win.
        """

        if self.mine:
            raise GameLostException()

        else:
            self.reveal_and_check_neighbors()

            if self.board.left == 0:
                raise GameWonException()

    def reveal_and_check_neighbors(self):
        """Reveal this cell and all of its neighbor cells, recursively.

        If a cell is not a mine, reveal it and then do the same for all of its
        neighbors. Repeat until there are no more cells found to check.
        """
        to_check = {self}
        seen = set()

        while to_check:
            cell = to_check.pop()
            seen.add(cell)
            if not cell.mine and cell.revealed:
                cell.revealed = True
                cell.board.left -= 1
                if cell.number == 0:
                    to_check.update(set(cell.neighbors()) - seen)



    def show(self, show_mines=False):
        """Show a cell."""

        if not show_mines and not self.revealed:
            return "."

        elif self.mine:
            return "*"

        else:
            return self.number


class Board(object):
    """The board."""

    def __init__(self, game, width, height):
        """Create the board.

        Set game, width, height, # cells left, and create the raw grid.
        """

        assert 1 <= height <= len(lowercase) and 1 <= width <= len(lowercase)

        self.game = game             # game object
        self.width = width
        self.height = height
        self.left = width * height   # number of non-mine, non-revealed cells
        self.cells = [
            [Cell(self, x, y) for x in range(width)]
            for y in range(height)]

    def place_mines(self, num_mines):
        """PLace mines and update neighbors' mine counts."""

        for mine_cell in sample(range(self.width * self.height), num_mines):
            cell = self.cells[mine_cell // self.width][mine_cell % self.width]
            cell.mine = True
            self.left -= 1

            for n in cell.neighbors():
                n.number += 1

    def show(self, show_mines=False):
        """Show board."""

        # Print heading
        print("\n ", end=' ')
        for col in lowercase[:self.width]:
            print(col, end=' ')
        print()

        # Print each row, with row heading on left
        for i, row in enumerate(self.cells):
            print(lowercase[i], end=' ')

            for cell in row:
                print(cell.show(show_mines=show_mines), end=' ')
            print()

        print()


class Game(object):
    """Minesweeper."""

    def __init__(self, width=11, height=11, num_mines=11):
        """Initialize game.

        - Set up bord
        - Place mines
        - Note time (so at game end the delta can be shown)
        """

        self.board = Board(self, width, height)
        self.board.place_mines(num_mines)
        self.start = time.time()

    def get_move(self):
        """Get a move, looping until we get a legal move"""

        while True:
            try:
                move = input(
                    "Move (col row, like 'ab' - %d left) > " % self.board.left)
                col = ord(move[0].upper()) - ord('A')  # A -> 0, B -> 1, ...
                row = ord(move[1].upper()) - ord('A')
                cell = self.board.cells[row][col]

                # We got a legal move, we can stop asking for a move
                return cell

            except (IndexError, EOFError) as e:
                print("\n(%s: try again)\n" % e)

    def play(self):
        """Main game loop."""

        try:
            while True:
                self.board.show()
                self.get_move().click()

        except GameWonException:
            end = "win"

        except GameLostException:
            end = "lost"

        self.board.show(show_mines=True)
        print("*** You %s in %.0f secs ***\n" % (end, time.time() - self.start))


if __name__ == '__main__':
    import sys
    g_width = int(sys.argv[1]) if len(sys.argv) > 1 else 11
    g_height = int(sys.argv[2]) if len(sys.argv) > 2 else 11
    g_num_mines = int(sys.argv[3]) if len(sys.argv) > 3 else 11
    Game(g_width, g_height, g_num_mines).play()
