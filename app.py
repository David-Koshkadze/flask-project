from flask import Flask, render_template

app = Flask(__name__)

class Todo:
    def __init__(self, id, title, done):
        self.id = id
        self.title = title
        self.done = done

todos = [
    Todo(1, 'Learn frontend', False),
    Todo(2, 'Learn backend', False)
]

@app.route('/')
def index():
    title = "David"
    names = ["David", "My Love"]
    return render_template('index.html', title=title, names=names, todos=todos)

@app.route('/about')
def about():
    return render_template('about.html')

# handling error
@app.errorhandler(404)
def page_not_found(e):
    return '<h1>Page Not Found</h1>'

