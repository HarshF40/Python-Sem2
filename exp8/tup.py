# tuple manipulations in python

# Creating tuples 
empty_tuple = ()
single_element_tuple = (3)
normal_tuple = (1, 2, 3, 4, 5)
mixed_tuple = (1, "Hello World", (1, 2, 3))

print("Empty tuple: ", empty_tuple)
print("Single element tuple: ", single_element_tuple)
print("Normal tuple: ", normal_tuple)
print("Mixed tuple: ", mixed_tuple)

# accessing elements in tuple
print("First Element in Normal tuple: ", normal_tuple[0])
print("Last Element in Normal tuple: ", normal_tuple[-1])

# slicing a normal tuple
print("Sliced normal_tuple (Index 1 to 4)", normal_tuple[1:4])

# updating a tuple (indirect way)
# tuples are immutable so first we convert it into list
temp_list = list(normal_tuple)
temp_list[2] = 99
normal_tuple = tuple(temp_list)
print("Updated Normal tuple: ", normal_tuple)

# concatinating tuples
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (6, 7, 8, 9, 0)
concatinated_tuple = tuple1 + tuple2
print("Concatinated Tuple: ", concatinated_tuple)

#deleting tuple
del tuple2
print("Tuple2 deleted cant access it now")

# membership testing
print("Is 3 in tuple 1: ", 3 in tuple1)
print("Is 10 in tuple 1: ", 10 in tuple1)

print("Iterating through tuple: ")
for element in concatinated_tuple :
    print(element, end=" ")

print("")

# tuple unpacking
person = ("Alice", 25, "Engineer")
name, age, profession = person
print("Tuple unpacking: ")
print(name, age, profession)

# Built in functions
numbers = (1, 2, 3, 4, 5, 6)
print("Lenght of the tuple: ", len(numbers))
print("Max element: ", max(numbers))
print("Min element: ", min(numbers))
print("Sum of elements: ", sum(numbers))

# nesting tuples
nested = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("Nested tuple: ", nested)
print("Accessing from the first tuple in the tuple: ", nested[0][0])

# counting and indexing
fruits = ("apple", "banana", "cherry", "apple", "banana", "apple")
print("Number of times apple appeared in fruits: ", fruits.count("apple"))
print("First Index of banana: ", fruits.index("banana"))
