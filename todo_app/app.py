from flask import Flask, render_template, request, redirect

from todo_app.data.session_items import add_item, get_item, remove_item, get_sorted_items
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route("/")
def index():
    return render_template("index.html", items=get_sorted_items())


@app.route("/add", methods=["POST"])
def add():
    new_item = request.form.get("new_item")
    add_item(new_item)
    return redirect("/")


@app.route("/complete", methods=["POST"])
def complete():
    item_to_complete = get_item(request.form.get("id_to_complete"))
    item_to_complete["status"] = "Completed"
    return redirect("/")


@app.route("/delete", methods=["POST"])
def remove():
    remove_item(int(request.form.get("id_to_delete")))
    return redirect("/")
