from multinomialNB import MultinomialNB
from multivariateNB import MultivariateNB

classes = ['ham','spam']

def takeInput(filename):
	fin = open(filename, 'r')
	trainData = []
	print("Preparing Data...")
	for line in fin.readlines():
		y, X = line.split(maxsplit=1)
		trainData.append([X,y])

	return trainData

def kfoldDivision(k, data):
	print("Dividing data into k-folds...")
	dataSize = (k-1+len(data))//k
	data_pieces = []
	for start in range(0,len(data),dataSize):
		end = min(start+dataSize,len(data))
		data_pieces.append(data[start:end])

	return data_pieces

data = takeInput('SMSSpamCollection')
data_pieces = kfoldDivision(5, data)

def runMultinomialNB():
	print("\n\n\nRunning multinomialNB classifier")

	avg_accuracy = 0
	for idx, testData in enumerate(data_pieces):
		trainData = []
		for i, samples in enumerate(data_pieces):
			if i == idx:
				continue
			for sample in samples:
				trainData.append(sample)
		classifier = MultinomialNB(trainData,classes)
		print("---------------------------------------------------------")
		print(f"Calculating accuracy for {idx+1} datafold as testData...")
		accuracy = 0

		for doc in testData:
			classname = classifier.classify(doc[0])
			if classname == doc[1]:
				accuracy += 1

		accuracy /= len(testData)

		print("Accuracy:",accuracy)
		avg_accuracy += accuracy

	avg_accuracy /= len(data_pieces)
	print("---------------------------------------------------------")
	print("5-fold accuracy:",avg_accuracy)

def runMultivariateNB():
	print("\n\n\nRunning multivariateNB classifier")

	avg_accuracy = 0
	for idx, testData in enumerate(data_pieces):
		trainData = []
		for i, samples in enumerate(data_pieces):
			if i == idx:
				continue
			for sample in samples:
				trainData.append(sample)
		classifier = MultivariateNB(trainData,classes)
		print("---------------------------------------------------------")
		print(f"Calculating accuracy for {idx+1} datafold as testData...")
		accuracy = 0

		for doc in testData:
			classname = classifier.classify(doc[0])
			if classname == doc[1]:
				accuracy += 1

		accuracy /= len(testData)
		
		print("Accuracy:",accuracy)
		avg_accuracy += accuracy

	avg_accuracy /= len(data_pieces)
	print("---------------------------------------------------------")
	print("5-fold accuracy:",avg_accuracy)

if __name__ == '__main__':
	runMultinomialNB()
	runMultivariateNB()