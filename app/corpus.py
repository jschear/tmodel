# snagged from http://radimrehurek.com/2014/03/tutorial-on-mallet-in-python/

import logging
import os
from gensim import corpora, utils
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def iter_documents(directory):
    """Iterate over documents, yielding one document at a time."""
    for fname in os.listdir(directory):
        if fname != 'README':
            document = open(os.path.join(directory, fname)).read() # read each document as one big string
            yield utils.simple_preprocess(document) # parse document into a list of utf8 tokens

def iter_plain_text_documents(directory):
    """Iterate over documents, yielding one document at a time."""
    for fname in os.listdir(directory):
        if fname != 'README':
            yield open(os.path.join(directory, fname)).read() # read each document as one big string

class Corpus(object):
    def __init__(self, directory):
        self.directory = directory
        self.dictionary = corpora.Dictionary(iter_documents(directory))

    def __iter__(self):
        for tokens in iter_documents(self.directory):
            yield self.dictionary.doc2bow(tokens)
