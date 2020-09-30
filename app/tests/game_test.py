import unittest
from app.models.game import Game
from app.models.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("John", "rock")
        self.player2 = Player("Jack", "scissors")
        self.game1 = Game()

    # def test_game_has_player(self):
    #     self.assertEqual("John", self.player1.name)

    # def test_player_has_choice(self):
    #     self.assertEqual("scissors", self.player2.choice)

    def test_game_with_player(self):
        player3 = Player("John", "rock")
        self.assertEqual("John wins", self.game1.play_game(player3, self.player2))

        # self.game.play_game(self.player2, self.player2)