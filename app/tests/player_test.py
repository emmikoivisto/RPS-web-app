import unittest
from app.models.player import Player

class TestPlayer(unittest.TestCase):
    
    def setUp(self):
        self.player1 = Player("John", "rock")

    
    def test_player1_has_name(self):
        self.assertEqual("John", self.player1.name)

    def test_player2_has_choice(self):
        self.assertEqual("rock", self.player1.choice)

