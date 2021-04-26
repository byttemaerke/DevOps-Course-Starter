from flask import Flask, render_template, request
from todo_app.data.session_items import *
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('item-title') != None:
            add_item(request.form.get('item-title'))
        else:
            item = get_item(request.form.get('item-status'))
            if item['status'] == 'Not Started':
                item['status'] = 'Completed'
            else:
                item['status'] = 'Not Started'
            save_item(item)
        
    return render_template('index.html', items = sorted(get_items(), key=lambda k: k['status'], reverse=True))


if __name__ == '__main__':
    app.run()
