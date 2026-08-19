import numpy as np

arry = np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12],
                 [13,14,15,16]])  #2D array

""" Array[Start:end:step]
       Array[RowIndex[Start:end:step], ColumnIndex([Start:end:step])] """

# ROWS SELECTION/SLICING
print(arry[1])  # access single row
print(arry[0:3])    # start to end, last index don't count's
print(arry[0:4:2])  # give me 2nd row from 0 to 4 
print(arry[::-1])     # no starting and ending value shows to select all from start to end, and -1 indecates to return in reverse order

# COLUMNS SELECTION/SLICING
print(arry[2, 2])   # Single element
print(arry[: , 2])    # : (means select all rows), so from all rows select 2 index
print(arry[:, 0:3])     # 0:3 is the columns range, from 0 to 3, last index count's is 3-1
print(arry[:, 0: :2])   # select and returns every 2 column

# BOTH ROWS AND COLUMNS SELECTION
# Example we need 2,4 columns of row 3,4
print(arry[2:4, 1: :2])