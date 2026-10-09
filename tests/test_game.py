import unittest

from board import Board
from game import DotsAndBoxes
from rules import valid_move


class BoardRulesTests(unittest.TestCase):
    def test_valid_horizontal_move(self):
        board = Board(2, 2)

        self.assertTrue(valid_move(board, "H", 0, 1))
        board.add_line("H", 0, 1)
        self.assertFalse(valid_move(board, "H", 0, 1))

    def test_valid_vertical_move(self):
        board = Board(2, 2)

        self.assertTrue(valid_move(board, "V", 1, 2))
        board.add_line("V", 1, 2)
        self.assertFalse(valid_move(board, "V", 1, 2))

    def test_invalid_and_repeated_move(self):
        board = Board(2, 2)

        self.assertFalse(valid_move(board, "H", -1, 0))
        self.assertFalse(valid_move(board, "V", 2, 3))
        board.add_line("H", 0, 0)
        self.assertFalse(valid_move(board, "H", 0, 0))

    def test_completion_of_box(self):
        board = Board(1, 1)
        board.add_line("H", 0, 0)
        board.add_line("H", 1, 0)
        board.add_line("V", 0, 0)

        self.assertEqual(board.add_line("V", 0, 1), 1)
        self.assertEqual(board.completed, {(0, 0)})

    def test_end_of_game_condition(self):
        board = Board(1, 1)
        for move in (("H", 0, 0), ("H", 1, 0), ("V", 0, 0), ("V", 0, 1)):
            board.add_line(*move)

        self.assertTrue(board.is_complete())
        self.assertFalse(valid_move(board, "H", 0, 0))

    def test_custom_board_size(self):
        game = DotsAndBoxes(rows=3, cols=4)

        self.assertEqual((game.board.rows, game.board.cols), (3, 4))


if __name__ == "__main__":
    unittest.main()
