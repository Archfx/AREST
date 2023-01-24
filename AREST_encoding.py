import string
import math
import time
import os
import sys

def hamming2(s1, s2):
    #Calculate the Hamming distance between two bit strings
    assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


start_time = time.time()
numGroups = 1 #int(sys.argv[1])
HD = int(sys.argv[1])
largestGroup = int(sys.argv[2])
# -1 to shift into correct length at start of while loop.
if numGroups > 1:
	stringLength = HD + math.ceil(HD/2) - 1
else:
	stringLength = 0
values = []
finalValues = []
while len(values) < numGroups:
	stringLength = stringLength + 1
	values = ["".zfill(stringLength)] 
	incrementValue = 1
	for i in range(0,pow(2,stringLength),incrementValue):
		added = True
		for j in values:
			if hamming2("{0:b}".format(i).zfill(stringLength), j) < HD:
				added = False
		if added:
			values.append("{0:b}".format(i).zfill(stringLength))
			if len(values) == numGroups:
				break
finalValues = values
if (largestGroup > 1):
	finalValues = []
	for i in values:
		for j in range(largestGroup):
			print("Appended to final Group")
			print("{0:b}".format(j).zfill(math.ceil(math.log(largestGroup))))
			finalValues.append(str(i) + str("{0:b}".format(j).zfill(math.ceil(math.log(largestGroup)))))
			print(str(i), finalValues[-1])
full_time = (time.time() - start_time)
print(finalValues)
print("Length of vectors: " + str(len(finalValues[-1])))
print("Time: " + str(full_time) + " seconds")
