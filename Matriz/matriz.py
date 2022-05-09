#Eynes Test - Federico Wagner

#Matriz
import random
import numpy as np

matrix = [[random.randint(0, 2) for num in range(5)] for num in range(5)]
matrix = np.array(matrix)

def checkSequenceOnRows(matrix):
	"""Returns True/False depending on the presence of four  same consecutive numbers"""
	for row in matrix:
		counter = 0
		previousNum = row[0]
		for num in row:
			if num == previousNum:
				counter += 1
			else:
				counter = 1
			previousNum = num
			if counter == 4:
				return True
	return False

def checkSequenceOnColumns(matrix):
	""" Transpose the matrix and execute the presence function """
	matrix = matrix.transpose()
	return checkSequenceOnRows(matrix)


for row in matrix:	# TEST
    print(row)		# TEST

print("secuence precense: ",( checkSequenceOnRows(matrix) or checkSequenceOnColumns(matrix) )) # TEST
      