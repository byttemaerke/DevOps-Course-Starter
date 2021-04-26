from flask import Flask, render_template, request
from todo_app.data.session_items import get_items, add_item
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        add_item(request.form.get('title'))
    return render_template('index.html', items = get_items())


if __name__ == '__main__':
    app.run()
