def SequenceForFunction(function, startX, finishX, count):
	step = (finishX - startX) / float(count - 1)

	res = []
	for i in range(count):
		res.append(function(startX + step * i))

	return res

def SequenceForIteratedFunction(function, startX, count):
	res = []
	res.append(startX)
	for i in range(count-1):
		res.append(function(res[i]))

	return res

def SequenceForReccurentFunctionReducing(function, startX, count, lowerBound = 0.0, upperBound = 1.0):
	res = []
	res.append(Reduce(startX, lowerBound, upperBound))

	for i in range(count-1):
		res.append(Reduce(function(res[i]), lowerBound, upperBound))

	return res

def Reduce(value, lowerBound, upperBound):
	if(value < lowerBound):
		return lowerBound
	elif(value > upperBound):
		return upperBound
	else:
		return value
