from nltk.tokenize import word_tokenize
import random
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

	allocated = 0;
	wordList = {}
	totalCount = []
	print("Training NB Classifier...")
	print("Preparing Count Vector...")
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

def kfoldDivision(k, data):
	print("Dividing data into k-folds...")
	dataSize = (k-1+len(data))//k
	data_pieces = []
	for start in range(0,len(data),dataSize):
		end = min(start+dataSize,len(data))
		data_pieces.append(data[start:end])

	return data_pieces

def multinomialNB(trainData, testData):
	wordList, countArray = trainClassifier(trainData)
	totalSum = np.sum(countArray)
	class_counts = np.sum(countArray, axis=0).astype('float64')
	class_counts /= totalSum
	true_pred = 0
	# P(ham/sentence) = P(ham)*P(sentence/ham)/P(sentence)
	
	for sample in testData:
		words = word_tokenize(sample[0])
		probabilities = class_counts
		for word in words:
			# The words not in wordList, we can take their probability
			# as 1/classes (for add-one smoothing), and since it is the same
			# for all the classes, we can ignore this also. 
			if word in wordList:
				position = wordList[word]
				probabilities = probabilities*countArray[position]
				word_counts = np.sum(countArray[position])
				probabilities /= word_counts

		max_pos = np.argmax(probabilities)
		if sample[1] == classes[max_pos]:
			true_pred += 1


	accuracy = true_pred/len(testData)
	return accuracy



def multivariateNB(para):
	pass

def takeInput(filename):
	fin = open(filename, 'r')
	trainData = []
	print("Preparing Data...")
	for line in fin.readlines():
		y, X = line.split(maxsplit=1)
		trainData.append([X,y])

	return trainData

data = takeInput('SMSSpamCollection')
data_pieces = kfoldDivision(5, data)

avg_accuracy = 0
for idx, testData in enumerate(data_pieces):
	trainData = []
	for i, samples in enumerate(data_pieces):
		if i == idx:
			continue
		for sample in samples:
			trainData.append(sample)
	print("---------------------------------------------------------")
	print(f"Calculating accuracy for {idx+1} datafold as testData...")
	accuracy = multinomialNB(trainData,testData)
	print("Accuracy:",accuracy)
	avg_accuracy += accuracy

avg_accuracy /= len(data_pieces)
print("---------------------------------------------------------")
print("5-fold accuracy:",avg_accuracy)







