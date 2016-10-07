import sys
import re
from collections import defaultdict
import cPickle

import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

en_stopwords = set(stopwords.words('english')) | {"n't", 's', 're', 've', 'm', 'would', 'could'}

def remove_html(text):
    return re.sub('<.+?>', ' ', text)

def tokenize(phrase):
    phrase = remove_html(phrase)
    tokens = word_tokenize(phrase)
    tokens = [t.strip("'.\"?:;") for t in tokens]
    tokens = [t for t in tokens if t and t[0].isalpha() and t not in en_stopwords]
    return ' '.join(tokens)

def read_phrases_file(file_name):
    dialogs = defaultdict(list)

    with open(file_name, 'r') as f:
        for line in f:
            did, phrase = line.lower().strip().split(' +++$+++ ')
            phrase = tokenize(phrase)
            dialogs[did].append(phrase)
    
    ids = []
    texts = []
    for id, sentences in dialogs.items():
        ids.append(id)
        texts.append(' '.join(sentences))

    return pd.DataFrame({'id': ids, 'dialogue': texts})

def read_missing_file(file_name):
    results = []
    original = []
    with open(file_name, 'r') as f:
        for line in f:
            _, phrase = line.lower().strip().split(' +++$+++ ')
            original.append(phrase)
            phrase = tokenize(phrase)
            results.append(phrase)
    return original, results

def write_predictions(predictions, file_name):
    with open(file_name, 'w') as f:
        for id, phrase in predictions:
            f.write(id + ' +++$+++ ' + phrase)
            f.write('\n')
        f.flush()

def main(dialog_file, missing_file):
    with open('tfidf.bin', 'rb') as f:
        vect = cPickle.load(f)
    
    df_dialogues = read_phrases_file(dialog_file)
    missing_original, missing = read_missing_file(missing_file)

    X_mis = vect.transform(missing).astype('float32')
    X_doc = vect.transform(df_dialogues.dialogue).astype('float32')

    dot = (X_mis * X_doc.T).toarray()
    most_similar = (-dot).argsort(axis=1)[:, 0]
    
    predictions = list(df_dialogues.id.iloc[most_similar])
    results = zip(predictions, missing_original)
    write_predictions(results, 'test_missing_with_predictions.txt')

    print 'done'

if __name__ == '__main__':
    """
    This script should be called as 
        python match_dialogs.py path/to/test_dialogs.txt path/to/test_missing.txt
    and write the predicted conversation numbers for all missing lines to a file 
    named test_missing_with_predictions.txt
    """

    if len(sys.argv) > 2:
        test_dialogs_file, test_missing_file = sys.argv[1], sys.argv[2]
        main(test_dialogs_file, test_missing_file)
    else:
        print "please call this script with `python match_dialogs.py path/to/test_dialogs.txt path/to/test_missing.txt`"
