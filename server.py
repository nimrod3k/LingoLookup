from flask import Flask, render_template
from blocks import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test_word_color/<color>/<height>/<word>", )
def test_Word_Color(color, height, word):
    
    if color == 'white' :
        block = White(word)
    if color == 'black' :
        block = Black(word)

    if height == 'mid' :
        return block.solve_mid()

    if height == 'bot' :
        return block.solve_bot()

if __name__ == "__main__":
    app.run()