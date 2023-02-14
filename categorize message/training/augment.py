import numpy as np
import pandas as pd
import os, psutil
import random
import math
from nltk.corpus import wordnet
import textblob as tb

'''
HOW TO MAKE THE GENERATED MESSAGES BETTER?

- Determine order of word-types from discord data
- Determine the sentiment of the messages if possible?

Using this information, generate messages that have some sort of order,
ex. noun verb noun noun or something and also have a common sentiment?

- Could arrange all words from messages and english dataset into
  smaller arrays for just nouns, verbs, adjectives, and unknowns

 --> Then, select a random word for each based on a random sentence format
'''

def read_wordbanks():

    DISCORD_WORDS = open("resources/discord_wordbank.txt", 'r')
    ENGLISH_WORDS = open("resources/3000_english_words.txt", 'r')

    discord_wordbank = list()

    discord_wordbank = DISCORD_WORDS.readlines()
    english_wordbank = ENGLISH_WORDS.readlines()

    for i in range(len(discord_wordbank)):
        discord_wordbank[i] = discord_wordbank[i].strip().split(' ')[0] 

    for i in range(len(english_wordbank)):
        english_wordbank[i] = english_wordbank[i].strip()

    DISCORD_WORDS.close()
    ENGLISH_WORDS.close()

    return [discord_wordbank, english_wordbank]


# Generates random messages using words from wordbanks. Returns list of messages with specified length.
def gen_messages(num_msg, ranked_words, english_words, min_len, max_len):
    
    min_msg_len = min_len
    max_msg_len = max_len
    num_messages = num_msg
    num_ranked = len(ranked_words)
    num_english = len(english_words)

    generated = []

    # Generating num_messages amount of random sentences
    for i in range(num_messages):
        num_words = random.randint(min_msg_len, max_msg_len) # Determine number of words in message
        curr_msg = ""
        
        for j in range(num_words):
            wordbank = random.choice([ranked_words, english_words]) # Randomly select word from english or discord wordbank
        
            if j == 0:
                curr_msg = curr_msg + wordbank[random.randint(0, num_ranked)]
            else:
                curr_msg = curr_msg + " " + wordbank[random.randint(0, num_ranked)]      
                
        generated.append(curr_msg)
        
    return generated
