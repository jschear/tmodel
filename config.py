CSRF_ENABLED = True
SECRET_KEY = 'SECRET_KEY!'

# path to mallet binary
MALLET_PATH = 'mallet-2.0.7/bin/mallet'

# local corpora used for LDA
CORPORA = {
    'Reuters (NLTK)': 'corpora/reuters/training/',
    'State of the Union (NLTK)': 'corpora/state_union/',
    'Gutenberg (NLTK)': 'corpora/gutenberg/',
    'Shakespeare's Sonnets': corpora/sonnets/'
}

