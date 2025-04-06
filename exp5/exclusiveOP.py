import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
    ])

print("Original Array \n", arr)
print("Transpose Array: \n", arr.T)

arr2 = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
    ])

print("Array 2: \n", arr2)
print("arr X arr2: \n", arr @ arr2)

#linear algebra operation to compute determinant
print("Determinant: ", np.linalg.det(np.array([
    [1, 0],
    [0, 1]
    ])))
