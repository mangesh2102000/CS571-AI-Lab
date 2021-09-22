from nltk.tokenize import word_tokenize
import numpy as np

def countWords(paragraph):
	wordlist = word_tokenize(paragraph)
	wordCount = {}
	for word in wordlist:
		if word not in wordCount:
			wordCount[word] = 0
		wordCount[word] = wordCount[word]+1
	return wordCount

def extractVocabulary(data):
	vocabulary = set()
	for doc in data:
		wordlist = word_tokenize(doc[0])
		for word in wordlist:
			vocabulary.add(word)
	vocabulary = {word: idx for idx, word in enumerate(vocabulary)}

	return vocabulary


class MultinomialNB:
	def __init__(self, trainData, classes):
		self.classes = classes
		vocabulary, probOfClass, probWordInClass = self.trainMultinomial(trainData)
		self.vocabulary = vocabulary
		self.probOfClass = probOfClass
		self.probWordInClass = probWordInClass

	def trainMultinomial(self,docs):
		classes = self.classes

		#Extract Vocabulary
		vocabulary = extractVocabulary(docs)

		num_docs = len(docs)

		#Count of each word in each class:
		#totalWordCount[position][0,1] tells count of words for classes[0] and [1]
		#position is the position of word in vocabulary dictionary.
		totalWordCount = np.ones((len(vocabulary),len(classes)))
		docsPerClass = np.zeros(len(classes))

		for doc in docs:
			wordCount = countWords(doc[0])
			classtype = classes.index(doc[1])
			
			docsPerClass[classtype] += 1
			for word, count in wordCount.items():
				pos = vocabulary[word]
				totalWordCount[pos][classtype] += count	

		probOfClass = docsPerClass/num_docs
		probWordInClass = totalWordCount/np.sum(totalWordCount,axis=0)

		return vocabulary, probOfClass, probWordInClass

	def classify(self, doc):
		words = word_tokenize(doc)
		probability = np.log(self.probOfClass)
		for word in words:
			if word in self.vocabulary:
				pos = self.vocabulary[word]
				probability += np.log(self.probWordInClass[pos])
			# for words not in vocabulary, the unrecognizable words
			# are ignored

		max_pos = np.argmax(probability)
		return self.classes[max_pos]
	
