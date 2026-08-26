import numpy as np

""" Broadcasting: The mechanism for performing arithmetic operation on arrays of different 
                shapes by virtually expending the smaller arrays to match the larger one
                without creating unnecessory copies of data in memory """

# RULES: Broadcasting is compatiable by comparing array shape
#       1. Dimensions are compatiable if they are equal.
#       2. Dimensions are compatiable if one of them is 1.
#       1. Dimensions are compatiable if one array lacks that dimension (treated as 1).

array1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
array2 = np.array([9])

print(array1.shape)
print(array2.shape)
# Arithematic opreation btw different Dimention array
print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)

marks = np.array([30, 40, 50, 32, 70, 60])
P_f = np.array(["Pass", "Fail"])
result = np.where(marks < 50, P_f[1], P_f[0])
print(result)