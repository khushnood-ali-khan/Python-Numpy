import numpy as np

# Zero Dimensional Array
arry = np.array('A')
print(arry.ndim)      # Type of the array

#   One Dimensional Array
arry = np.array([1,2,3,4])
print(arry.ndim)

#  2D/METRICX Array
twoD_Array = np.array([[1,2,3,4],[5,6,7,8],[8,9,10,0]])     # The number of elements must be same in each sublist
print(twoD_Array.ndim)

# 3D ARRAY
D3_Array = np.array([
    [[1,2,3,4],[5,6,7,8],[2,34,52,12]],
    [[9,10,11,12],[13,14,15,16],[34,543,21,34]]            # The number of elements must be same in each sublist
])
print(D3_Array.ndim)
print(D3_Array.shape)    #tells you the dimensions and size of array, how many rows, columns, or depth layers it has.

# ACCESS THROUGHT CHAIN INDEXING (Old inefficent method)
print(D3_Array[0][2][2])

# ACCESS THROUGHT MULTIDIMENTIONAL INDEXING (Numpy method faster then chain indexing)
print(D3_Array[1, 2, 1])