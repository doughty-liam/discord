from nltk.corpus import wordnet as wn
import textblob as tb
import multiprocessing as mp
import time


# Could multi-process this for speed?
def get_nouns():
    all_nouns = [word for synset in wn.all_eng_synsets(wn.NOUN) for word in synset.lemma_names()]
    return all_nouns

def get_verbs():
    all_verbs = [word for synset in wn.all_eng_synsets(wn.VERB) for word in synset.lemma_names()]
    return all_verbs

def get_adverbs():
    all_adverbs = [word for synset in wn.all_eng_synsets(wn.ADV) for word in synset.lemma_names()]
    return all_adverbs

def get_adjectives():
    all_adjectives = [word for synset in wn.all_eng_synsets(wn.ADJ) for word in synset.lemma_names()]
    return all_adjectives

if __name__ == '__main__':

    nouns = get_nouns()
    verbs = get_verbs()
    adjectives = get_adjectives()
    adverbs = get_adverbs()

    print(nouns[:20],verbs[:20])
