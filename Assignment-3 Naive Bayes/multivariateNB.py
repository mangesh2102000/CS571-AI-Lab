from nltk.tokenize import word_tokenize
import numpy as np

def extractVocabulary(data):
	vocabulary = set()
	for doc in data:
		wordlist = word_tokenize(doc[0])
		for word in wordlist:
			vocabulary.add(word)
	vocabulary = {word: idx for idx, word in enumerate(vocabulary)}

	return vocabulary

class MultivariateNB:
	def __init__(self, trainData, classes):
		self.classes = classes
		vocabulary, probOfClass, probOccurOfWord = self.trainMultivariate(trainData)
		self.vocabulary = vocabulary
		self.probOfClass = probOfClass
		self.probOccurOfWord = probOccurOfWord



	def trainMultivariate(self, docs):
		classes = self.classes
		
		#Extract Vocabulary
		vocabulary = extractVocabulary(docs)

		num_docs = len(docs)

		totalOccurencesOfWord = np.ones((len(vocabulary),len(classes)))
		docsPerClass = np.zeros(len(classes))

		for doc in docs:
			classtype = classes.index(doc[1])

			docsPerClass[classtype] += 1
			wordlist = set(word_tokenize(doc[0]))
			for word in wordlist:
				pos = vocabulary[word]
				totalOccurencesOfWord[pos][classtype] += 1

		probOfClass = docsPerClass/num_docs

		#docsPerClass+1 may become equal to totalOccurencesOfWord
		#log(1) will return 0, to avoid that, +2 is used. 
		probOccurOfWord = totalOccurencesOfWord/(docsPerClass+2)

		return vocabulary, probOfClass, probOccurOfWord

	def classify(self, doc):
		wordlist = word_tokenize(doc)
		probability = np.log(self.probOfClass)

		for word, pos in self.vocabulary.items():
			if word in wordlist:
				probability += np.log(self.probOccurOfWord[pos])
			else:
				probability += np.log(1-self.probOccurOfWord[pos])

		max_pos = np.argmax(probability)
		return self.classes[max_pos]
