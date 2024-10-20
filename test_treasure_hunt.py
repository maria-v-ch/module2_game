import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from main import TreasureMap, Player, Game

class TestTreasureMap(unittest.TestCase):
    def setUp(self):
        self.treasure_map = TreasureMap()

    def test_generate_treasure(self):
        treasure = self.treasure_map._generate_treasure()
        self.assertIsInstance(treasure, tuple)
        self.assertIsInstance(treasure[0], int)
        self.assertIsInstance(treasure[1], str)
        self.assertTrue(1 <= treasure[0] <= 10)
        self.assertTrue('A' <= treasure[1] <= 'J')

    def test_check_guess(self):
        self.treasure_map.treasure = (5, 'C')
        self.assertTrue(self.treasure_map.check_guess((5, 'C')))
        self.assertFalse(self.treasure_map.check_guess((6, 'D')))

    def test_provide_clue(self):
        self.treasure_map.treasure = (5, 'C')
        self.assertEqual(self.treasure_map.provide_clue((5, 'C')), "Very hot!")
        self.assertEqual(self.treasure_map.provide_clue((6, 'D')), "Hot!")
        self.assertEqual(self.treasure_map.provide_clue((8, 'F')), "Warm.")
        self.assertEqual(self.treasure_map.provide_clue((10, 'J')), "Cold.")

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player(5)

    def test_init(self):
        self.assertEqual(self.player.attempts, 5)
        self.assertEqual(self.player.guesses, [])

    @patch('builtins.input', side_effect=['5,C'])
    def test_make_guess_valid(self, mock_input):
        guess = self.player.make_guess()
        self.assertEqual(guess, (5, 'C'))
        self.assertEqual(self.player.attempts, 5)
        self.assertEqual(self.player.guesses, [(5, 'C')])

    @patch('builtins.input', side_effect=['invalid', '11,K', '5,C'])
    def test_make_guess_invalid(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            guess = self.player.make_guess()
            self.assertEqual(guess, (5, 'C'))
            self.assertIn("Invalid input", fake_out.getvalue())

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game(5)

    @patch('main.logging.info')
    def test_start_win(self, mock_logging):
        self.game.treasure_map.treasure = (5, 'C')
        self.game.player.make_guess = MagicMock(return_value=(5, 'C'))
        result = self.game.start()
        self.assertTrue(result)
        self.assertEqual(self.game.player.attempts, 4)
        mock_logging.assert_any_call("Player won the game")

    @patch('main.logging.info')
    def test_start_lose(self, mock_logging):
        self.game.treasure_map.treasure = (5, 'C')
        self.game.player.make_guess = MagicMock(side_effect=[(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (6, 'E')])
        result = self.game.start()
        self.assertFalse(result)
        self.assertEqual(self.game.player.attempts, 0)
        mock_logging.assert_any_call("Game over - player ran out of attempts")

    def test_attempts_decrement(self):
        self.game.treasure_map.treasure = (5, 'C')
        self.game.player.make_guess = MagicMock(side_effect=[(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (6, 'E')])
        self.game.start()
        self.assertEqual(self.game.player.attempts, 0)

if __name__ == '__main__':
    unittest.main()
