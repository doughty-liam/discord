import numpy as np
import pandas as pd
from nltk.corpus import wordnet as wn
import nltk
import os, psutil
import random
import math
import textblob as tb
from vectorize import clean_messages

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

	messages = get_messages()
	new = []

	all_nouns = [word for synset in wn.all_eng_synsets(wn.NOUN) for word in synset.lemma_names()]
	all_verbs = [word for synset in wn.all_eng_synsets(wn.VERB) for word in synset.lemma_names()]
	all_adverbs = [word for synset in wn.all_eng_synsets(wn.ADV) for word in synset.lemma_names()]
	all_adjectives = [word for synset in wn.all_eng_synsets(wn.ADJ) for word in synset.lemma_names()]

	FILE = open("resources/augmented_messages.txt", "w")

	for message in messages:
		for i in range(10): # Create ten new augmented messages per original
			replaceInd = 0
			words = message.split()
			for j in range((len(words)//4) + 1):

				currWord = str(random.choice(words))
				replaceInd = words.index(currWord)
				tag = nltk.pos_tag([currWord])[0][1]

				newWord = "_-"
				if tag == "JJ":
					while ("_" in newWord) or ("-" in newWord):
						newWord = str(random.choice(all_adjectives)).lower()
					words[replaceInd] = newWord
					newMsg = " ".join(words)
					new.append(newMsg)

				elif tag == "RB":
					while ("_" in newWord) or ("-" in newWord):
						newWord = str(random.choice(all_adverbs)).lower()
					words[replaceInd] = newWord
					newMsg = " ".join(words)
					new.append(newMsg)

				elif tag == "VB":
					while ("_" in newWord) or ("-" in newWord):
						newWord = str(random.choice(all_verbs)).lower()
					words[replaceInd] = newWord
					newMsg = " ".join(words)
					new.append(newMsg)
				
				else:
					while ("_" in newWord) or ("-" in newWord):
						newWord = str(random.choice(all_nouns)).lower()
					words[replaceInd] = newWord
					newMsg = " ".join(words)
					new.append(newMsg)
			FILE.write(newMsg+"\n")
