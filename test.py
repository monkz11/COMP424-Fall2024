import unittest

import numpy as np

from agents import random_agent
from agents.random_agent import RandomAgent
from world import World


##Test world class
class TestWorld(unittest.TestCase):

    def setUp(self):
        print("=== TestWorld ===\n")
        """
        Setup
        """
        self.world = World()

    def test_initalize_world(self):
        """
        Test the initialization of the world class
        """
        self.assertEqual(self.world.player_1_name, "random_agent")
        self.assertEqual(self.world.board_size % 2, 0)
        if self.world.board_size == 6:
            self.assertTrue(
                np.array_equal(
                    self.world.chess_board,
                    np.array(
                        [
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 2, 1, 0, 0],
                            [0, 0, 1, 2, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                        ]
                    ),
                )
            )
        if self.world.board_size == 8:
            self.assertTrue(
                np.array_equal(
                    self.world.chess_board,
                    np.array(
                        [
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 2, 1, 0, 0, 0],
                            [0, 0, 0, 1, 2, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                        ]
                    ),
                )
            )
        if self.world.board_size == 10:
            self.assertTrue(
                np.array_equal(
                    self.world.chess_board,
                    np.array(
                        [
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 2, 1, 0, 0, 0, 0],
                            [0, 0, 0, 0, 1, 2, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        ]
                    ),
                )
            )
        if self.world.board_size == 12:
            self.assertTrue(
                np.array_equal(
                    self.world.chess_board,
                    np.array(
                        [
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        ]
                    ),
                )
            )

    def test_step_function(self):
        """
        Test the step function of the world class (random moves)
        """
        print("test_step_function")
        result = self.world.step()
        print(result)


    def test_is_valid_move(self):
        """
        Test the is_valid_move function
        Here we will reassign the chessboard for the test
        """
        ###Basic 8x8 intial board
        self.world.chess_board = np.array(
            [
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 2, 1, 0, 0],
                [0, 0, 1, 2, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
            ]
        )

        ##Test != 0
        self.assertFalse(self.world.is_valid_move((2, 2), 1))
        ##Test valid capture
        self.assertTrue(self.world.is_valid_move((2, 1), 1))
        ##Test invalid capture
        self.assertFalse(self.world.is_valid_move((4, 3), 2))
        self.assertFalse(self.world.is_valid_move((1, 4), 1))

    def test_execute_move(self):
        """
        Test the execute move, and flips
        """
        self.world.chess_board = np.array(
            [
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 2, 1, 0, 0],
                [0, 0, 1, 2, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
            ]
        )
        self.world.execute_move((1, 2), 1)

        self.assertTrue(
            np.array_equal(
                self.world.chess_board,
                np.array(
                    [
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0],
                        [0, 0, 1, 1, 0, 0],
                        [0, 0, 1, 2, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                    ]
                ),
            )
        )
        self.world.execute_move((3, 1), 2)

        self.assertTrue(
            np.array_equal(
                self.world.chess_board,
                np.array(
                    [
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0],
                        [0, 0, 1, 1, 0, 0],
                        [0, 2, 2, 2, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                    ]
                ),
            )
        )

    def test_check_endgame(self):
        """
        Try out a variety of known endgames, see if our algorithm
        retuns the correct tuple (bool, int, int)
        """
        # Vlasáková 1 – 63 Schotte (European Grand Prix Prague 2011)
        self.world.chess_board = np.array(
            [
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 0, 0],
                [1, 1, 1, 1, 1, 1, 0, 2],
                [1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 1, 1],
            ]
        )
        self.world.board_size = 8
        self.assertEqual(self.world.check_endgame(), (False, 58, 1))
        ##No legal moves will be found
        self.assertEqual(self.world.step(), (True, 58, 1))

        # Vecchi 13 – 51 Nicolas (World Othello Championship 2017, Ghent)
        self.world.chess_board = np.array(
            [
                [0, 2, 2, 2, 2, 2, 2, 2],
                [0, 1, 1, 1, 1, 1, 0, 2],
                [1, 1, 1, 1, 1, 1, 1, 2],
                [1, 1, 1, 1, 1, 1, 1, 2],
                [1, 1, 1, 1, 1, 1, 1, 2],
                [1, 1, 1, 1, 1, 1, 1, 2],
                [1, 1, 1, 1, 1, 1, 1, 2],
                [0, 1, 1, 1, 1, 1, 0, 0],
            ]
        )

        self.assertEqual(self.world.check_endgame(), (False, 45, 13))
        ##No legal moves will be found
        self.assertEqual(self.world.step(), (True, 45, 13))

        # Hassan 3 – 17 Verstuyft J. (European Grand Prix Ghent 2017)
        self.world.chess_board = np.array(
            [
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 1, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 2],
                [0, 0, 1, 1, 1, 1, 0, 2],
                [0, 0, 1, 1, 1, 0, 0, 2],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ]
        )

        self.assertEqual(self.world.check_endgame(), (False, 17, 3))
        ##No legal moves will be found
        self.assertEqual(self.world.step(), (True, 17, 3))





##Test random agent
class TestRandomAgent(unittest.TestCase):
    def setUp(self):
        print("=== TestRandomAgent ===\n")
        self.random_agent = RandomAgent()

    def test_step(self):
        print("test_step\n")
        chess_board = np.array([[1, 2, 1, 0], [1, 2, 1, 0], [0, 1, 2, 1], [0, 1, 2, 1]])

        move = self.random_agent.step(chess_board, 0, 1)
        self.assertEqual(chess_board[move[0]][move[1]], 0)


if __name__ == "__main__":
    unittest.main()
