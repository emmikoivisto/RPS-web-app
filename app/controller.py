from app import app
from flask import render_template
from app.models.player import *
from app.models.game import *



@app.route('/')
def index():
    return render_template('index.html', title='Game')

@app.route('/<choice>/<choice>')
def new_game():
    player1 = Player("Jack", "scissors")
    player2 = Player("John", "rock")
    game = Game(player1, player2)
    play_game(game)
    


