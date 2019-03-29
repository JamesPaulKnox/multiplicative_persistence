# Import a library that let's me explicitly instruct
# the program to create a copy of a value, and not just
# a reference to a value.
import copy as cp



# Here, we can tell it the first number we want to check
# and the last number (minus one) we want to check. The
# code will check every number in this range. For example,
# 277777788888899 could be a useful first number. It has a
# known answer of 11. In python, there is no hard upper limit
# for integers. The only limiting factor is your RAM.
firstNum = 277777788888899
lastNum = 277777788888911



# Declaring and initializing a variable
# I will use to keep track of the record
# number within our test range.
recordSeq = [0]


# Turns an integer into a list of digits
# Returns a list
def makeIntList(x):
	
	print("Making a list of integers.")

	# M.P.'s solution is much more elegant than mine,
	# and most likely faster. I've implemented the
	# method shown in the video below:
	
	xNumList = [int(i) for i in str(x)]
	
	return xNumList



# Multiplies a list of digits together
# Returns an integer
def multiplyDigits(xList):
	print("Multiplying them together.")
	result = 1
	
	for xInt in xList:
		result = result * xInt
	
	return int(result)



# Iterate through your specified range,
# checking every number within it.
for x in range(firstNum, lastNum):

	print("Checking {}".format(x))

	# The sequence variable is used only for the current
	# integer we are checking. I first make it equal to the
	# first step's results. "x" is our current integer.
	# makeIntList will turn that int into a list of single
	# digit ints. multiplyDigits takes a list of single digits,
	# and will return an integer equal to the product of the digits
	sequence = [multiplyDigits(makeIntList(x))]

	# This says "As long as the most recent result is more than 9...
	while sequence[-1] > 9:
		print("Iterating with {}".format(sequence[-1]))
		# ... copy the most recent result to a variable multThis...
		multThis = cp.copy(sequence[-1])
		print(multThis)
		
		# ... and do the math again for that number! Append the result
		# as the last item in the sequence list.
		sequence.append(multiplyDigits(makeIntList(multThis)))
	
	# This is mostly unnessecary, but it makes the first item in the list
	# the original number. Having the first number in the list be the int
	# we checked will make reporting our record easier to understand.
	sequence.insert(0, x)
	
	# If the length of our current sequence is larger than the length
	# of any previous sequence, it is the smallest number of the record
	# length. If you change ">" to ">=" below, it will instead record the
	# largest number of record length. Personally, I think the smallest
	# number with a long length is much more interesting.
	if len(sequence) > len(recordSeq):
		recordSeq = sequence
	
	# Give some output for the user to read in the logs.
	print("The integer {} persists for {} iterations.".format(x, (len(sequence) - 1)))
	print("The sequence for it is:")
	print(sequence)
	print("")





### ==========================================================
### Finally, report the record we found within our test range!
### ==========================================================

# Important note though: the sequence length is not the same as
# the number of steps it persisted for! The following statement
# explicitly corrects it.

recordLen = len(recordSeq) - 1

print("=============================")
print("Here is the lowest number with the highest")
print("multiplication persistance: {}".format(recordSeq[0]))
print("and it persists for {} steps!".format(recordLen))
print("=============================")
print(recordSeq)
