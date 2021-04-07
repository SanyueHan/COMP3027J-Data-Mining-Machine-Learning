import numpy as np

# Matrix
A = np.arange(1, 9).reshape(2, 4)
print(A)

print(A.shape)

B = np.array([[1, 1, 1, 1], [2, 2, 2, 2]])
print(B)

print(B.shape)

# Matrix Elements
print(A[1, 1])
print(A[0, 1])
print(A[1, 2])

# Vector
y = np.array([6, 5])
print(y)
print(y[0])
print(y[1])
y2 = np.array([[6], [5]])
print(y2)
print(y.reshape([2, 1]))

# Matrix Addition
print(A+B)
print(A-B)
print(A*B)

C = np.array([[1, 1], [2, 2], [1, 1], [2, 2]])
print(C)
try:
    print(A+C)
except ValueError as e:
    print(e)

print(C.T)
print(A + C.T)

# Scalar Multiplication
print(2*A)
print(A/10)
print(5+A)

# Matrix Vector Multiplication
X = np.array([[1, 3], [2, 6], [1, 2], [2, 2]])
theta = np.array([[1], [2]])
y_hat = np.matmul(X, theta)
print(y_hat)

# Matrix-Matrix Multiplication
A = np.array([[1, 3], [2, 6], [1, 2], [2, 2]])
B = np.array([[1, 3], [2, 0]])
print(np.matmul(A, B))