from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Super secret key'

class Todo:
    def __init__(self, id, title, done):
        self.id = id
        self.title = title
        self.done = done

todos = [
    Todo(1, 'Learn frontend', False),
    Todo(2, 'Learn backend', False)
]

# Create a Form Class
class NamerClass(FlaskForm):
    name = StringField("What is your name", validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def index():
    title = "David"
    names = ["David", "My Love"]
    return render_template('index.html', title=title, names=names, todos=todos)

# About Route
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/name', methods=['GET', 'POST'])
def name():
    return render_template('name.html')

# handling error
@app.errorhandler(404)
def page_not_found(e):
    return '<h1>Page Not Found</h1>'

