from flask import Flask

watch this son of a biatch fail miserably because I don't know what I am doing

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, world!"


if __name__ == '__main__':
    app.run(debug=True)