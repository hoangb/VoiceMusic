# !/usr/bin/env python3
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello world" #return render_template(‘hello.html’)


if __name__ == '__main__':
    app.run(port=8080)






