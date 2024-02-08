from flask import Flask

app = Flask(__name__)


@app.route('/')
def app_():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def promotion():
    return '<p>Человечество вырастает из детства.</p><p>Человечеству мала одна планета.</p>' \
           '<p>Мы сделаем обитаемыми безжизненные пока планеты.</p><p>И начнем с Марса!</p><p>Присоединяйся!</p>'


@app.route("/image_mars")
def image_mars():
    return '<head><title>Привет, Марс!</title></head><body><p>Жди нас, Марс!</p><img src="static/MARS.png" ' \
           'alt="здесь должна была быть картинка, но не нашлась">' \
           '<p>Вот она какая, красная планета</p></body>'




if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
