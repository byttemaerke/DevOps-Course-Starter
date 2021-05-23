from flask import Flask, render_template, request, redirect, url_for
from flask.json import jsonify
from todo_app.data.session_items import *
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods=['GET'])
def read_items():
    return render_template('index.html', items = get_items())

@app.route('/items', methods=['POST'])
def create_item():
    add_item(request.form.get('item-title'))
    return redirect_to_index()

@app.route('/items/<id>', methods=['POST'])
def update_or_delete_item(id):
    if request.form.get('operation') == 'UPDATE':
        item = get_item(id)
        save_item({ 'id': item.get('id'), 'status': derive_opposite_status(item.get('status')), 'title': item.get('title') })
    elif request.form.get('operation') == 'DELETE':
        delete_item_whose_id_is(id)
    else:
        print('Error', file=SystemError)

    return redirect_to_index()

def redirect_to_index():
    return redirect(url_for('read_items'))

if __name__ == '__main__':
    app.run()
