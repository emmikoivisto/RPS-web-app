from app import app
from flask import render_template
from app.models.player import *
from app.models.game import *



@app.route('/')
def index():
    return render_template('index.html', title='Game')


@app.route('/play_game')
def new_game():
    player1 = Player("Jack", "scissors")
    player2 = Player("John", "rock")
    game = Game()
    return game.play_game(player1, player2)


