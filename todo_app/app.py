from flask import Flask, render_template, request, redirect

from todo_app.data.trello_items import (
    add_item,
    remove_item,
    get_sorted_items,
    complete_item,
)
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route("/")
def index():
    return render_template("index.html", items=get_sorted_items())


@app.route("/add", methods=["POST"])
def add():
    new_item_title = request.form.get("new_item")
    add_item(new_item_title)
    return redirect("/")


@app.route("/complete/<item_id>", methods=["POST"])
def complete(item_id):
    complete_item(item_id)
    return redirect("/")


@app.route("/remove/<item_id>", methods=["POST"])
def remove(item_id):
    remove_item(item_id)
    return redirect("/")
