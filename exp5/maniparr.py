import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
    ])

print("Original Array: \n", arr)

#axis = 0 -> specifies that to append along the rows
print("Array after appending an array: \n", np.append(arr, [[100, 110, 120]], axis=0))

#inserting at row 1
print("Array after insertion: \n", np.insert(arr, 1, [[1, 2, 3]], axis=0))

#deleting the row at index 1
print("Array after deletion: ", np.delete(arr, 1, axis=0))

#accessing array at a specific position
print("Element at 2,3: ", arr[1, 2])

#slicing a matrix to get a submatrix
print("Sliced matrix: \n", arr[0:2, 1:3])

#mathematical operation on each element (same for all)
print("Muliplying each element by 33.33", arr*33.33)

#searching for elements
print("Elements where number are multiple of 3", arr[np.where(arr % 3 == 0)])

#filetering array: boolean mask to keep elements which are less than 30
#the resulting array will be flattened
print("Array where numbers are less than 30: ", arr[arr < 30])

arr_new = np.array([
    [23],
    [33],
    [98]
    ])

#hstack -> concatinates along the column or at each element at the end of the each row
print("hstack: ", np.hstack((arr, arr_new)))

#vstack
print("vstack: ", np.vstack((arr, [10, 29, 33])))

#sorting the array
print("Sorted array: ", np.sort([
    [23, 12, 34, 2, 43],
    [3, 23, 4, 432, 3],
    [34, 5, 54, 122, 4]
    ], axis=1))

#copying the array
copied_array = np.copy(arr)
copied_array[1, 2] = 33
print("Copied Array: \n", copied_array)
print("Original Array: \n", arr)

#reshaping array:
print("Reshaped Array: \n", np.array([10, 20, 30, 40]).reshape(2, 2))

#total sum
print("Sum: ", np.sum(arr))

#mean
print("Mean: ", np.mean(arr))

#standard deviation
print("Standard Deviation: ", np.std(arr))

#cumulative sum and cumulative product
print("Cumsum and Cumproduct resp.: ", np.cumsum(arr), np.cumprod(arr))

#splitting arrays:
print("Splitiing array into 3 sub arrays along rows: \n")
for subarr in np.array_split(arr, 3, axis=1):
    print(subarr)

#removing duplicates from an array:
print("Unique Elements: ", np.unique(np.array([
    [1, 2, 3, 2, 1],
    [3, 4, 2, 1, 3]
    ])))

#inversion of array:
print("Inversion of boolean values in an array", np.invert(np.array([True, False, False, True])))

#conversion of float to int
print("Array float to int: ", np.array([[
    [1.3, 4.4],
    [3.44, 5.44]
    ]]).astype(int))
