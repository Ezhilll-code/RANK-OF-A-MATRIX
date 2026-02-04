#Program to find the rank of a matrix.
#Developed by: Ezhilan H
#RegisterNumber: 212225240040

import numpy as np

A = np.array([[1, 2, 3],[3, 6, 9]])

rank = np.linalg.matrix_rank(A)

print(rank)
