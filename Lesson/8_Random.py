import numpy as np

# # Genrate Random value with numpy built-in funtions

# rng = np.random.default_rng()

# print(rng.integers(1, 11))      # random number btw 1 to 10
# print(rng.integers(1, 11, 3))      # random number btw 1 to 10 the size of 3

# # For readibility you can assign key words like:
# print(rng.integers(low=10, high= 101, size= 5))

# # if you want 2 dimentional random numbers, then you can set dimentions in size
# print(rng.integers(low=1, high=51, size=(3,2)))


# # IF YOU WANT TO GENRATE THE SAME RANDOM LIST EVERY TIME YOU CAN USE seed IN RANDOM FUNCTION
# rng2 = np.random.default_rng(seed=1)
# print(rng2.integers(low=1, high=21, size=(2,3)))    # it will always genrate the same random array


# GENERATE RANDOM floating NUMBERS
print(np.random.uniform())      #it will genrate a random floating value btw 0 and 1

# WE can set a seed to always get the same values, and can set size too
np.random.seed(1)
print(np.random.uniform(low=-1, high=1, size=(3,2)))

# Shuffle our array

rg = np.random.default_rng()

arr = np.array([1,2,4,5,6,7])

rg.shuffle(arr)
print(arr)