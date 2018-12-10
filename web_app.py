from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import Form, StringField, IntegerField, FieldList, FormField, validators
from analyzer import layered_iteration
from anytree import Node 
from anytree.exporter import DotExporter

app = Flask(__name__)
app.config['SECRET_KEY'] = 'CDB14257595C9E3B85884E0E366A63267C4980CD5A0AC2395C05CD1591692037'

DEFAULT_INITIAL_WORD = "hack"
DEFAULT_TOPICS = "technology"
DEFAULT_BREADTH = 1

class MainForm(FlaskForm):
    initial_word = StringField('Initial Word')
    iterations = IntegerField('Iterations/Depth')
    breadth = IntegerField('Breadth/Width')
    topic1 = StringField('Topic 1')
    topic2 = StringField('Topic 2')
    topic3 = StringField('Topic 3')
    topic4 = StringField('Topic 4')
    topic5 = StringField('Topic 5')

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/get_picture", methods=['POST'])
def get_picture():
    form = MainForm(request.form)
    iterations = form.iterations.data
    if form.initial_word.data != "":
        root = Node(form.initial_word.data)
        initial_word = form.initial_word.data
    else:
        root = Node(DEFAULT_INITIAL_WORD)
        initial_word = DEFAULT_INITIAL_WORD
    if form.breadth.data != "":
        breadth = int(form.breadth.data)
    else:
        breadth = DEFAULT_BREADTH
    topics_list = [form.topic1.data, form.topic2.data, form.topic3.data, 
              form.topic4.data, form.topic5.data]
    topics = ""
    if not all(topics_list):
        topics = DEFAULT_TOPICS
    else:
        if form.topic1.data:
            topics += form.topic1.data 
        if form.topic2.data:
            topics += ",{}".format(form.topic2.data)
        if form.topic3.data:
            topics += ",{}".format(form.topic3.data)
        if form.topic4.data:
            topics += ",{}".format(form.topic4.data)
        if form.topic5.data:
            topics += ",{}".format(form.topic5.data)

    seen_words = [initial_word]

    if initial_word.endswith('y'):
        seen_words.append(initial_word[:-1] + "ies")
    if initial_word.endswith('ies'):
        seen_words.append(initial_word[:-3] + "y")
    if initial_word.endswith('s'):
        seen_words.append(initial_word[:-1])
    if initial_word.endswith('es'):
        seen_words.append(initial_word[:-2])
    seen_words.append(initial_word + "s")
    seen_words.append(initial_word + "es")
    
    layered_iteration(initial_word, topics, root, 0, iterations, seen_words,
                      breadth, {})
    DotExporter(root).to_picture("./root.png")
    return render_template("index.html")