def AND(a, b):
	return a and b

def OR(a, b):
	return a or b

def IMPLIES(a, b):
	return OR(not a, b)

OPERATION = { '^' : AND, 'v' : OR, '=>' : IMPLIES}

def solve(exp, values):
	idx = 0
	left = ""
	right = ""
	operation = ""
	l = len(exp)

	if(l == 1):
		return(values[exp[0]])
	elif(l == 2):
		return(str((int(values[exp[1]]) + 1) % 2))

	while idx < l:
		if exp[idx] == '^' or exp[idx] == 'v' or exp[idx] == '=':
			operation = exp[idx]
			break
		left += exp[idx]
		idx += 1
	idx += 1

	if exp[idx] == '>':
		operation += exp[idx]
		idx += 1
	while idx < l:
		right += exp[idx]
		idx += 1

	if left[0] == '~':
		left_value = (str((int(values[left[1]]) + 1) % 2))
	else :
		left_value = (str((int(values[left[0]])) % 2))

	if right[0] == '~':
		right_value = (str((int(values[right[1]]) + 1) % 2))
	else :
		right_value = (str((int(values[right[0]])) % 2))

	res = OPERATION[operation](int(left_value),int(right_value))
	return str(int(res));


def simplify(query, values):
	stack = []
	for i, c in enumerate(query):
		if(c==")"):
			exp = []
			while(stack[-1] != "("):
				exp.append(stack.pop())
			stack.append(solve(exp[::-1], values))
		else:
			stack.append(c)
	if(stack[-1] == "1"):
		return(True)
	return(False)

def split_clauses(query, values):
	stack=[]
	index=0

	for i, c in enumerate(query):
		if(c==")"):
			stack.pop()
			if(len(stack)==0):
				index = i
				break
		elif(c=="("):
			stack.append(c)

	if("=>" in query):
		left = query[:index+1]
		right = query[index+3:]
		if(simplify(left, values)):
			if(not simplify(right, values)):
				return("Not Theorem")

if __name__ == "__main__":
	flag = 0
	query = str(input("Enter a Query: "))
	variable = set([x for x in query if x not in ['=', '>', '~', ')', '(', '^', 'v']])
	for i in range(2**len(variable)):
		values = {}
		values['0'] = '0'
		values['1'] = '1'
		temp = format(i, '0'+str(len(variable))+'b')
		for idx, c in enumerate(variable):
			values[c] = temp[idx]
		if(split_clauses(query, values) == "Not Theorem"):
			flag = 1
	if(flag):
		print("Not Theorem")
	else:
		print("Theorem")
		