from flask import render_template, request, flash

from app import app

from forms import CorpusForm
from corpus import Corpus

from gensim import models, utils

CORPORA = app.config['CORPORA']
MALLET_PATH = app.config['MALLET_PATH']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/select_corpus', methods=['GET', 'POST'])
def select_corpus():
    form = CorpusForm()
    form.corpus.choices = [(key, key) for key in CORPORA.keys()]
    if form.validate_on_submit():
        flash('Form worked')

        corpus = form.corpus.data
        iterations = form.iterations.data
        topics = form.topics.data

        return process_corpus(corpus, iterations, topics)

    return render_template('select_corpus.html', form = form)

def process_corpus(corpus_name, iterations, num_topics):

    corpus = Corpus(CORPORA[corpus_name]) # init the corpus

    # train LDA topics using MALLET
    model = models.LdaMallet(MALLET_PATH, corpus, num_topics=num_topics, id2word=corpus.dictionary, iterations=iterations)

    # model = models.ldamodel.LdaModel(corpus=corpus, num_topics=num_topics, id2word=corpus.dictionary, iterations=iterations)

    # each topic is a list of words
    topics = model.show_topics(topics=-1, topn=20, log=False, formatted=False)

    topic_strings = []
    for topic in topics:
        string = ' '.join(word[1] for word in topic)
        topic_strings.append(string)

    # print list of words for each topic
    word_in_topics = build_word_in_topics(topics)

    # print topic proportion for each document
    # topics_in_docs = build_topics_in_docs(model, corpus)

    return render_template('view_corpus.html', corpus=corpus_name, \
        words_in_topics=word_in_topics, topic_strings=topic_strings) #, topics_in_docs=topics_in_docs)

def build_word_in_topics(topics):
    word_in_topics = []
    for topic in topics:
        topic_words = []
        for pair in topic:
            word_map = {}
            word_map['text'] = pair[1]
            word_map['value'] = str(pair[0])
            topic_words.append(word_map)
        word_in_topics.append(topic_words)
    return word_in_topics


def build_topics_in_docs(model, corpus):
    topics_in_docs = []
    docs = model[corpus]
    for doc in docs:
        doc_topics = []
        for pair in doc:
            topic_map = {}
            topic_map['topic_num'] = str(pair[0])
            topic_map['proportion'] = str(pair[1])
            doc_topics.append(topic_map)
        topics_in_docs.append(doc_topics)
    return topics_in_docs

