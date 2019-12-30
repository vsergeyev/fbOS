import os
from flask import Flask
from flask import render_template, request, url_for, redirect

import settings


app = Flask(__name__, static_folder='appmedia', static_url_path='/appmedia')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/desktop/')
def desktop():
    return render_template("desktop.html")


if __name__ == '__main__':
    app.run(debug=settings.DEBUG)
