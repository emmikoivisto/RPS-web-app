import unittest
from app.models.game import Game
from app.models.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("John", "rock")
        self.player2 = Player("Jack", "scissors")


    def test_game_has_player(self):
        self.assertEqual("John", self.player1.name)