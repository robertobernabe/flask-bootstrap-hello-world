from hello_world import app
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    say = {"msg": "Hello World. Hello Bootrap"}
    return render_template("index.html", title="Home", say=say)


@app.route("/cover")
def cover():
    return render_template("cover.html")
