import numpy as np
arr = np.array([1, 2, 3, 4, 5])
# print(arr)

#printing the type
# 
#now for 2d array
# arr = np.array(45)
# print(arr)

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr)

#now 3d array
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr.ndim)     #to get the dimesnions an array is in

# arr = np.array([10, 20, 30, 40, 50])
# # print(arr[0])           #getting an index in the array
# print(arr.sum())        #summing an array

# arr = np.array([[1, 2, 3], [4, 5, 6], [30, 40, 50]])
# print(arr[2, 1])        #accessing values from a 3d array, just multidimensional in general

# print(arr.dtype)            #to get the datatype pf the array

#generate randm array i guess
# print(np.random.rand(100, 50))

sales = np.array([
    [50, 30, 20],       #day 1
    [60, 35, 22],
    [55, 40, 25],
    [70, 45, 30],
    [65, 42, 28]
])

# print(f"Total per product: {sales.sum(axis = 0)}")
print(f"Average eggs: {sales[::,2].mean()}")