from app.models.player import Player

class Game:


    def play_game(self, player1, player2):
        if player1.choice == 'rock' and player2.choice == 'scissors':
            return player1.name + 'wins'
        elif player1.choice == 'paper' and player2.choice == 'scissors':
            return player2.name + 'wins'
        elif player1.choice == 'scissors' and player2.choice == 'rock':
            return player2.name + 'wins'
        elif player1.choice == 'scissors' and player2.choice == 'paper':
            return player1.name + 'wins'
        elif player1.choice == 'paper' and player2.choice == 'rock':
            return player1.name + 'wins
        elif player1.choice == 'rock' and player2.choice == 'paper':
            return player2.name + 'wins'