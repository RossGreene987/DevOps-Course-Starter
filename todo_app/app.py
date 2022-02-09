from flask import Flask, render_template, request, redirect
from todo_app.data.models import Status, ViewModel

from todo_app.data.trello_items import (
    add_item,
    remove_item,
    get_sorted_items,
    move_item,
)
from todo_app.flask_config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route("/")
    def index():
        item_view_model = ViewModel(get_sorted_items())
        return render_template("index.html", view_model=item_view_model)

    @app.route("/add", methods=["POST"])
    def add():
        new_item_title = request.form.get("new_item")
        add_item(new_item_title)
        return redirect("/")

    @app.route("/begin/<item_id>", methods=["POST"])
    def begin(item_id):
        move_item(item_id, Status.STARTED)
        return redirect("/")

    @app.route("/complete/<item_id>", methods=["POST"])
    def complete(item_id):
        move_item(item_id, Status.COMPLETED)
        return redirect("/")

    @app.route("/remove/<item_id>", methods=["POST"])
    def remove(item_id):
        remove_item(item_id)
        return redirect("/")

    return app
