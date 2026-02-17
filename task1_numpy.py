import numpy as np

# Task 1 - NumPy practice (from cheat sheet)

# 1) Create an array of 10 zeros
print("1)", np.zeros(10))

# 2) Create an array of 10 ones
print("2)", np.ones(10))

# 3) Create an array of 10 fives
print("3)", np.full(10, 5))

# 4) Create an array of the integers from 10 to 50
print("4)", np.arange(10, 51))

# 5) Create an array of all the even integers from 10 to 50
print("5)", np.arange(10, 51, 2))

# 6) Create a 3x3 matrix with values ranging from 0 to 8
print("6)\n", np.arange(0, 9).reshape(3, 3))

# 7) Create a 3x3 identity matrix
print("7)\n", np.eye(3))

# 8) Use NumPy to generate a random number between 0 and 1
print("8)", np.random.rand(1))

# 9) Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
print("9)", np.random.randn(25))

# 10) Create an array of 20 linearly spaced points between 0 and 1
print("10)", np.linspace(0, 1, 20))

# ---- Indexing and Selection part from your screenshot ----
arr_2d = np.array([
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45]
])

# Retrieve the value 25 from the array using indexing.
print("11)", arr_2d[1, 1])

# Extract the second row of the array.
print("12)", arr_2d[1, :])

# Extract the third column of the array.
print("13)", arr_2d[:, 2])

# Extract the bottom-right 2x2 sub-array from arr_2d.
print("14)\n", arr_2d[1:, 1:])
