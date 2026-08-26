import numpy as np

# Aggregates: 
#           optimized built-in methods used to summarize, reduce, or combine elements of an array into a single value or a reduced array

array = np.array([[2, 4, 3, 5], [5, 7, 8, 9]])

print(np.sum(array))        # sum of the array
print(np.mean(array))       # mean(average) of the array
print(np.median(array))     # middle value of the array
print(np.std(array))        # Compute standared deviation
print(np.var(array))        # compute variance
print(np.min(array))        # minimum of the array
print(np.max(array))        # maximum of the array
print(np.prod(array))       # Product of all elements
print(np.argmax(array))     # the index of the max value
print(np.argmin(array))     # the index of the min value

#   WE can apply these functions on roes and columns sepratly too
print(np.sum(array, axis= 0))       # 0 for Columns
print(np.sum(array, axis= 1))       # 1 for rows