from nltk.corpus import wordnet as wn
import textblob as tb
import pandas as pd
import string
from unidecode import unidecode

def clean_messages(messages:list)->list:
	"""
	Strips, encodes to ascii, and converts all text to lowercase.
	"""
	cleaned = []	
	for i in range(len(messages)):
		
		
		temp = str(messages[i]).translate(str.maketrans('', '', string.punctuation))
		temp = "".join(char for char in temp if char.isalpha() or char == ' ')
		temp2 = temp.lower().rstrip().lstrip()
		clean = " ".join(temp2.split())
		clean = unidecode(clean)
		if len(clean) != 0:
			cleaned.append(clean)
	
	return cleaned

def get_tags()->dict:
	"""
	Pulls all possible POS tags from a text file and vectorizes them
	in a dictionary. Key=POS tag, value=integer. 
	"""
	FILE = open("resources/textblob_tags.txt", "r")    
	lines = FILE.readlines()
	tags = {(line.split())[0]:num for (line, num) in zip(lines, range(1,len(lines)+1))}
	return tags

if __name__ == "__main__":
	discord_msgs = pd.read_excel("resources/discord_message_hist.xlsx")

	discord_msgs["Content"].str.lower()
	messages = discord_msgs["Content"].tolist()
	messages = clean_messages(messages)

	blobs = [tb.TextBlob(str(msg)) for msg in messages]
	all_tags = get_tags()
	vectors = [[int(0) for cols in range(len(all_tags))] for rows in range(len(blobs)) ]

	# Creating vectors to pass to NN
	for i in range(len(vectors)):
		for tag in blobs[i].tags:
			if tag[1] in all_tags:
				vectors[i][int(all_tags[tag[1]])-1] = vectors[i][int(all_tags[tag[1]])-1] + 1

