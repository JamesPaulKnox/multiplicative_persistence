import copy as cp

firstNum = 100
lastNum = 1000000


# Turns an integer into a list of digits
# Returns a list
def makeIntList(x):
	print("Making a list of integers.")
	xStr = cp.copy(str(x))
	xCharList = cp.copy(list(xStr))
	
	xNumList = []
	for xChar in xCharList:
		xNumList.append(int(xChar))
	
	return xNumList



# Multiplies a list of digits together
# Returns an integer
def multiplyDigits(xList):
	print("Multiplying them together.")
	result = 1
	
	for xInt in xList:
		result = result * xInt
	
	return int(result)
	
recordSeq = [0]

# Iterate through your specified range, checking
for x in range(firstNum, lastNum):

	print("Checking {}".format(x))

	sequence = [multiplyDigits(makeIntList(x))]

	while sequence[-1] > 9:
		print("Iterating with {}".format(sequence[-1]))
		multThis = cp.copy(sequence[-1])
		print(multThis)
		
		sequence.append(multiplyDigits(makeIntList(multThis)))
		
	sequence.insert(0, x)
	
	while sequence.count(0) > 0:
		sequence.remove(0)
	
	if len(sequence) > len(recordSeq):
		recordSeq = sequence
	
	print("The integer {} persists for {} iterations.".format(x, len(sequence)))
	print("The sequence for it is:")
	print(sequence)
	print("")





print("=============================")
print("Here is the lowest number with the highest")
print("multiplication persistance: {}".format(recordSeq[0]))
print("and it persists for {} steps!".format(len(recordSeq)))
print("=============================")
print(recordSeq)
