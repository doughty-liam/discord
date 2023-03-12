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

	index = 0
	for message in messages[:30]:
		for i in range(10): # Create ten new augmented messages per original
			words = message.split()
			print(words)
			currWord = str(random.choice(words))
			# print(nltk.pos_tag([currWord]))
		index = index + 1