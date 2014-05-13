from flask_wtf import Form
from wtforms import TextField, IntegerField, SelectField
from wtforms.validators import DataRequired

class CorpusForm(Form):
    corpus = SelectField('Corpus')
    iterations = IntegerField('Iterations', default = 500)
    topics = IntegerField('Numer of Topics', default = 20)
