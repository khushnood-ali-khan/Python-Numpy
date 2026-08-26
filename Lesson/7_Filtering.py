import numpy as np

# Filtering mean checking the data on a certain conditions and using them or discarding them

marks = np.array([30, 50, 58, 87, 45, 20, 74, 39])

result = marks[marks < 50]
result = marks[(marks > 50) & (marks < 80)]
print(result)

marks[marks < 50] = 0       # change the value base on condition
print(marks)

# if we want to keep the original Dimention shap of the arry then we can use where() function
arr = np.array([[98, 90, 70, 60], [85, 50, 55, 72]])

result = np.where(arr > 60, arr, 0)
print(result)