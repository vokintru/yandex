from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index1():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion_image')
def index2():
    with open('templates/index.html', 'r', encoding='utf-8') as stream:
        return stream.read()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
