from nltk.corpus import wordnet as wn
import textblob as tb
import multiprocessing as mp
import time
from vectorize import clean_messages
from augment import get_messages


if __name__ == '__main__':
    
    msgs = get_messages()

    for msg in msgs:
        print(msg)