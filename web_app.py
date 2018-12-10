from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import Form, StringField, IntegerField, FieldList, FormField, validators
from flask_bootstrap import Bootstrap 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'CDB14257595C9E3B85884E0E366A63267C4980CD5A0AC2395C05CD1591692037'
Bootstrap(app)

class MainForm(FlaskForm):
    initial_word = StringField('Initial Word')
    iterations = IntegerField('Iterations/Depth')
    breadth = IntegerField('Width/Breadth')
    topic1 = StringField('Topic 1')
    topic2 = StringField('Topic 2')
    topic3 = StringField('Topic 3')
    topic4 = StringField('Topic 4')
    topic5 = StringField('Topic 5')

@app.route("/")
def index():
    form = MainForm()
    return render_template("index.html", form=form)