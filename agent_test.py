"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent

from importlib import reload

"""
1. Test output interface of MinimaxPlayer.minimax():
2. Test functionality of MinimaxPlayer.minimax():
3. Test that minimax() raises SearchTimeout when the timer expires:
4. Test that MinimaxPlayer successfully plays a full game:
5. Test interface of AlphaBetaPlayer.alphabeta():
6. Test the interface of AlphaBetaPlayer.get_move():
7. Test functionality of AlphaBetaPlayer.alphabeta():
8. Test that alphabeta() raises SearchTimeout when the timer expires:
9. Test iterative deepening in AlphaBetaPlayer.get_move():
10. Test that AlphaBetaPlayer successfully plays a full game:
11. Test output interface of custom_score():
12. Test output interface of custom_score_2():
13. Test output interface of custom_score_3():
14. Submission includes heuristic_analysis.pdf:
15. Submission includes research_review.pdf:
"""

class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)

class MinimaxTest(unittest.TestCase):

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)

    def test1(self):
        game_agent.MinimaxPlayer().minimax(self.game, 3)

if __name__ == '__main__':
    unittest.main()
