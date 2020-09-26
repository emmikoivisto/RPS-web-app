from app import app
from flask import render_template
# from app.models.player import *
# from app.models.game import *



@app.route('/')
def index():
    return render_template('index.html', title='Game')

# @app.route('/<choice>/<choice>')
# def play_game(choice_1, choice_2):
#     new_game(choice_1, choice_2)
    


