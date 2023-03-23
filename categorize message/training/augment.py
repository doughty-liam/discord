import numpy as np
import pandas as pd
from nltk.corpus import wordnet as wn
import nltk
import os, psutil
import random
import math
import textblob as tb
from vectorize import clean_messages

'''
How to augment?

1. Scan all messages in list
2. Select 1-2 (max message length) words to replace from the message list
3. Store current message in a list of words
4. Randomy select numReplaced words from msgList.
5. Get each words POS tag.
6. Replace words in original message with new RANDOM words that have the same POS tag.
'''

#	blobs = [tb.TextBlob(str(msg)) for msg in messages]
def get_blobs():

	discord_msgs = pd.read_excel("resources/discord_message_hist.xlsx")
	discord_msgs["Content"].str.lower()
	messages = discord_msgs["Content"].tolist()
	messages = clean_messages(messages)
	blobs = [tb.TextBlob(str(msg)) for msg in messages]

	return blobs

def get_messages():

	discord_msgs = pd.read_excel("resources/discord_message_hist.xlsx")
	discord_msgs["Content"].str.lower()
	messages = discord_msgs["Content"].tolist()
	messages = clean_messages(messages)

	return messages



if __name__ == "__main__":

	blobs =	get_blobs()
	messages = get_messages()
	new = []

	all_nouns = [word for synset in wn.all_eng_synsets(wn.NOUN) for word in synset.lemma_names()]
	all_verbs = [word for synset in wn.all_eng_synsets(wn.VERB) for word in synset.lemma_names()]
	all_adverbs = [word for synset in wn.all_eng_synsets(wn.ADV) for word in synset.lemma_names()]
	all_adjectives = [word for synset in wn.all_eng_synsets(wn.ADJ) for word in synset.lemma_names()]

	index = 0
	for message in messages[:10]:
		for i in range(10): # Create ten new augmented messages per original
			words = message.split()
			currWord = str(random.choice(words))
			tag = nltk.pos_tag([currWord])[0][1]

			if tag == "JJ":
				newWord = str(random.choice(all_adjectives))
				newMsg = message.replace(currWord, newWord)
				print(message, newMsg)
				new.append(newMsg)

			elif tag == "RB":
				newWord = str(random.choice(all_adverbs))
				newMsg = message.replace(currWord, newWord)
				print(message, newMsg)
				new.append(newMsg)

			elif tag == "VB":
				newWord = str(random.choice(all_verbs))
				newMsg = message.replace(currWord, newWord)
				print(message, newMsg)
				new.append(newMsg)
			
			else:
				newWord = str(random.choice(all_nouns))
				newMsg = message.replace(currWord, newWord)
				print(message, newMsg)
				new.append(newMsg)
