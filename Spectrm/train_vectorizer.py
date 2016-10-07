from collections import defaultdict
import pandas as pd
import numpy as np
import re

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer

import cPickle

en_stopwords = set(stopwords.words('english')) | {"n't", 's', 're', 've', 'm', 'would', 'could'}

def remove_html(text):
    return re.sub('<.+?>', ' ', text)

def tokenize(phrase):
    phrase = remove_html(phrase)
    tokens = word_tokenize(phrase)
    tokens = [t.strip("'.\"?:;") for t in tokens]
    tokens = [t for t in tokens if t and t[0].isalpha() and t not in en_stopwords]
    return ' '.join(tokens)

dialogs_all = defaultdict(list)
missing_phrases = {}

with open('./challenge_data/train_dialogs.txt', 'r') as f:
    for line in f:
        did, phrase = line.lower().strip().split(' +++$+++ ')
        phrase = tokenize(phrase)
        dialogs_all[did].append(phrase)

with open('./challenge_data/test_dialogs.txt', 'r') as f:
    for line in f:
        did, phrase = line.lower().strip().split(' +++$+++ ')
        phrase = tokenize(phrase)
        dialogs_all[did].append(phrase)

with open('./challenge_data/train_missing.txt', 'r') as f:
    for line in f:
        did, phrase = line.lower().strip().split(' +++$+++ ')
        phrase = tokenize(phrase)
        missing_phrases[did] = phrase

with open('./challenge_data/test_missing.txt', 'r') as f:
    for i, line in enumerate(f):
        _, phrase = line.lower().strip().split(' +++$+++ ')
        phrase = tokenize(phrase)
        missing_phrases['t%05d' % i] = phrase

all_texts = []
for sentences in dialogs_all.values():
    all_texts.append(' '.join(sentences))
all_texts.extend(missing_phrases.values())

vect = TfidfVectorizer(ngram_range=(1, 3), min_df=4)
vect.fit(all_texts)

with open('tfidf.bin', 'wb') as f:
    cPickle.dump(vect, f)

print 'done'