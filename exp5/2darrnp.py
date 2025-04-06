import numpy as np

arr = np.array([[10, 20, 30], [40, 50, 60]])
print("Original 2D array from list: ", arr)

arr_from_tuple = np.array(((10, 20, 30), (40, 50, 60)))
print("2D array from tuple: ", arr_from_tuple)

arr_complex = np.array([[1+2j, 3+4j, 5+6j], [7+8j, 9+10j, 11+12j]])
print("2D array with complex number: ", arr_complex)

#arange -> creates an array between the specified range
#reshape -> reshapes the array to a 2D array of 2rows and 5columns
arr_arange = np.arange(0, 10).reshape(2, 5)
print("2D array using arange and reshape", arr_arange)

#linspace -> returns an array of a specified range of specified interval
arr_linspace = np.linspace(0, 1, 6).reshape(2, 3)
print("2D array using linspace: ", arr_linspace)

#random.rand(r, c) -> return an array of randomly generated numbers in the order rXc
arr_rand = np.random.rand(2, 3)
print("2D array using rand: ", arr_rand)
