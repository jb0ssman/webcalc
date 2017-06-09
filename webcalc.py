from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Nope, I refuse to play your game!"


if __name__ == '__main__':
    app.run(debug=True)