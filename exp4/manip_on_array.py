import numpy as np

array_gen = np.array([1, 2, 3, 4, 5, 6, 7])
print("Original Array:", array_gen)

print("Array append:", np.append(array_gen, [8, 9]))

print("Array insertion:", np.insert(array_gen, 2, [0, -1]))

print("Array Deletion:", np.delete(array_gen, [1, 3]))

array_gen[2] = -1024
print("Array Update:", array_gen)

print("Array element access:", array_gen[3])

print("Slice array:", array_gen[1:4])

print("Array each element*2:", array_gen*2)
print("Array each element+5:", array_gen+5)

#searching for elements
print("Elements greater than 3:", array_gen[np.where(array_gen > 3)])

print("Filtered Array:", array_gen[array_gen < 4])

print("Concatinated Array:", np.concatenate((array_gen, np.array([0, 9, 8, 7]))))

print("Sorted Array:", np.sort(array_gen))

array_copy = np.copy(array_gen)
array_copy[0] = 77777
print("Original:", array_gen, "Copy:", array_copy)

print("Array Reshape:", array_gen.reshape((7,1)))

mask = array_gen > 2
print("Masking:",array_gen[mask])

print("Sum of array:",np.sum(array_gen))
print("Mean of array:", np.mean(array_gen))
print("Standard deviation of elements:", np.std(array_gen))

print("Cumulative Sum:", np.cumsum(array_gen))
print("Cumulative Prodict:", np.cumprod(array_gen))


array = np.array([1, 1, 2, 3, 2, 5, 6, 6, 7, 1])
print("Unique Elements:", np.unique(array))

print("Split Array:", np.split(array, 2))
bool_array = np.array([True, False, True])
print("Inverted array:", np.invert(bool_array))

#changing data type
print("Array with integer data type:", array.astype(int))
