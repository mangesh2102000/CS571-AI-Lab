from nltk.tokenize import word_tokenize
import numpy as np

classes = ['ham','spam']

def countWords(paragraph):
	wordlist = word_tokenize(paragraph)
	wordCount = {}
	for word in wordlist:
		if word not in wordCount:
			wordCount[word] = 0
		wordCount[word] = wordCount[word]+1
	return wordCount

def trainClassifier(data):
	num_classes = len(classes)
	# word: [1]*num_classes (add-one smoothing)

	int allocated = 0;
	wordList = {}
	totalCount = []
	for sample in data:
		wordCount = countWords(sample[0])
		classtype = 0
		if sample[1] == classes[1]:
			classtype = 1

		for word, count in wordCount.items():
			if word not in wordList:
				wordList[word] = allocated
				allocated += 1
				totalCount.append([1]*num_classes)

			position = wordList[word]
			totalCount[position][classtype] += count

	return wordList, np.array(totalCount)

def multinomialNB(para):
	pass

def multivariateNB(para):
	pass

def takeInput(filename):
	fin = open(filename, 'r')
	trainData = []
	for line in fin.readlines():
		y, X = line.split(maxsplit=1)
		trainData.append([X,y])

	return trainData

trainData = takeInput('SMSSpamCollection')
wordList, countArray = trainClassifier(trainData)





