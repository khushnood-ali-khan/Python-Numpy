import numpy as np

arry = np.array([1,2,3,4])  # 1D array

#   Scalar arithmetic / Single number opreation(like, +, -, *, /)
print(arry + 20)
print(arry - 20)
print(arry * 2)
print(arry / 2)
print(arry ** 2)

#   Vectorized math fuction
print(np.sqrt(arry))    # Square route of the array
print(np.pi)        #build ing constant
print(np.round(arry))   # Round-up a floating value

"""EXERCISE"""
# Find area of a circle
redius = np.array([3, 4, 5])
circle = np.pi * redius ** 2        # combine vector function and scalar opreation
print(circle)

#   ELEMENT_WISE ARITHMETIC
arry1 = np.array([1, 2, 3])
arry2 = np.array([4, 5, 6])
print(arry1 + arry2)
print(arry1 - arry2)
print(arry1 * arry2)
print(arry1 / arry2)
print(arry1 ** arry2)

#   Comparision operators (>, <, ==, >=, <=, !=)
result = np.array([60, 34, 70, 85, 90, 69, 79])

print(result == 90)
print(result >= 60)