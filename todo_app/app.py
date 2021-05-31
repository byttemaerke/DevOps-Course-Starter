from todo_app.data.session_items import delete_item_whose_id_is
from flask import Flask, render_template, request, redirect, url_for
from flask.json import jsonify
from todo_app.flask_config import Config
import todo_app.data.trello_client as trello_client

app = Flask(__name__)
app.config.from_object(Config)
INDEX_FILENAME = 'index.html'
ITEM_TITLE_KEY = 'item-title'
ITEM_STATUS_KEY = 'item-status'


@app.route('/', methods=['GET'])
def read_items():
    return render_template(INDEX_FILENAME, items=trello_client.get_items())


@app.route('/items', methods=['POST'])
def create_item():
    trello_client.add_item(request.form.get(ITEM_TITLE_KEY))
    return redirect_to_index()


@app.route('/items/<id>/update', methods=['POST'])
def update_item(id):
    trello_client.update_item_whose_id_is(id, request.form.get(ITEM_STATUS_KEY))
    return redirect_to_index()


@app.route('/items/<id>/delete', methods=['POST'])
def delete_item(id):
    trello_client.delete_item_whose_id_is(id)
    return redirect_to_index()


def redirect_to_index():
    return redirect(url_for('read_items'))


if __name__ == '__main__':
    app.run()
