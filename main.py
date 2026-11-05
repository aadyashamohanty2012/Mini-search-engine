import math
from collection import Counter, defaultdict
from articles import Article

def tokenize(text):
  chars = [ch if ch.isalnum() else ' ' for ch in text.lower()]
  return ''.join(chars).split()
def build_index(articles):
    index = defaultdict(dict)
    lengths = {}
    for doc_id, (title, text) in enumerate(articles):
        words = tokenize(title + ' ' + text)
        lengths[doc_id] = len(words)
        for word in words:
            index[word][doc_id] = index[word].get(doc_id, 0) + 1
    return index, lengths

INDEX
  