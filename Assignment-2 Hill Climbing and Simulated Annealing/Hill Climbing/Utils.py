# This File contains functions to help with input and output 

def inputFromFile(filename):
	file = open(filename, 'r')
	data = []
	for row in file:
		row = row.replace('T','')
		row = row.replace('\n','')
		row = row.replace('B','0')
		data.append([int(x) for x in row.split()])

	return data

def convertToInputFormat(data):
	res = ""
	for i in range(3):
		for j in range(3):
			if data[i][j] != 0:
				res += ('T' + str(data[i][j]) + ' ')
			else :
				res += ('B ')
		res += "\n";
	return res