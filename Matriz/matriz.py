#Eynes Test - Federico Wagner

#Matriz
import random
import numpy as np


sequenceArray = []

def checkSequenceOnRows(matrix, rowCheck = True):
	"""Returns True/False depending on the presence of four same consecutive numbers"""
	for indexMatrix, row in enumerate(matrix):
		counter = 0
		previousNum = row[0]
		for indexRow, num in enumerate(row):
			if num == previousNum:
				counter += 1
			else:
				counter = 1
			previousNum = num
			if counter == 4:
				if(rowCheck):
					sequenceArray.append(("HORIZONTAL", 4, (indexRow-3, indexMatrix), (indexRow, indexMatrix)))
				else:
					sequenceArray.append(("VERTICAL", 4, (indexMatrix, indexRow-3), (indexMatrix, indexRow)))

			if counter == 5:
				sequenceArray.pop()
				if(rowCheck):
					sequenceArray.append(("HORIZONTAL", 5, (indexRow-4, indexMatrix), (indexRow, indexMatrix)))
				else:
					sequenceArray.append(("VERTICAL", 5, (indexMatrix, indexRow-4), (indexMatrix, indexRow)))	

def checkSequenceOnColumns(matrix):
	""" Transpose the matrix and execute the presence function """
	matrix = matrix.transpose()
	return checkSequenceOnRows(matrix, False)


def run():
	matrix = [[random.randint(0, 1) for num in range(5)] for num in range(5)]
	matrix = np.array(matrix)
	
	for row in matrix:	
		print(row)		

	checkSequenceOnRows(matrix)
	checkSequenceOnColumns(matrix)
	if(len(sequenceArray)==0):
		print("No sequence present in matrix")
	else:
		for sequence in sequenceArray:
			print("Direction: ", sequence[0],"Longitude: ",sequence[1],"|", sequence[2], "----", sequence[3])


run() # TEST
