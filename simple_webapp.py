#!/usr/bin/python3
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return '''Simple webapp (Простейшее веб-приложение)<br>
           Page 1 (Страница 1) <a href=page1>page1</a><br>
           Page 2 (Страница 2) <a href=page2>page2</a>'''


@app.route('/page1')
def page1() -> str:
    return 'This is page 1. Первая страница.'


@app.route('/page2')
def page2() -> str:
    return 'This is page 2. Вторая страница.'


if __name__ == '__main__':
    app.run(debug=True)
