from flask import Flask

app = Flask(__name__)


@app.route('/')
def index1():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index2():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion_image')
def promotion_image():
    with open('templates/index.html', 'r', encoding='utf-8') as stream:
        return stream.read()


@app.route('/astronaut_selection')
def astronaut_selection():
    with open('templates/astronaut_selection.html', 'r', encoding='utf-8') as stream:
        return stream.read()




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
