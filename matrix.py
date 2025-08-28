import numpy as np


#addition of a matrix in python
A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
B = np.array([[4, 7], [2, 6]])

# print(A+B)


#multiplication of a scalar matrix
# print(2*A)

#to transpose a matrix(hcnaging rows to columns)
# print(A.T)


#determinant
# print(np.linalg.det(B))

#inverse a matrix
print(np.linalg.inv(B))