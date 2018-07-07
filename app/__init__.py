# !/usr/bin/env python3
from flask import Flask, render_template, url_for
import os

app = Flask(__name__)


@app.context_processor
def _url_for_rewrite():
    """
    Override url_for() to prevent CSS caching
    """
    return dict(url_for=_dated_url_for)


def _dated_url_for(endpoint, **values):
    """
    Helper function to handle Flask CSS caching.
    Source: http://flask.pocoo.org/snippets/40/

    """
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path, endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


@app.route("/")
def index():
    placeholder_variable1 = "Placeholder 1"
    placeholder_variable2 = "Placeholder 2"
    return render_template("index.html", **locals())


if __name__ == '__main__':
    app.run(port=8080)






