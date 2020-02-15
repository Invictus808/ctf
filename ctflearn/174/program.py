#####
# File: program.py
# Copyright: 2020, Blaise Aranador
# Description: File contains the code to solve CTF Learn challenge 174.
#####

# Open data.dat file
inputfile = open('./data.dat', 'r')

# Read input file line by line
lines = inputfile.readlines()

counter = 0

# Iterate one line at a time
for line in lines:
	zeros = 0
	ones = 0

	# Count the # of 1's and 0's in each line
	for bit in line.rstrip():
		if int(bit) == 0:
			zeros += 1
		else:
			ones += 1

	# Increment counter if # of 0's is a multiple of 3
	# OR
	# Increment counter if # of 1's is a multiple of 2
	if zeros % 3 == 0:
		counter += 1
	elif ones % 2 == 0:
		counter += 1

print("Flag: " + str(counter))
