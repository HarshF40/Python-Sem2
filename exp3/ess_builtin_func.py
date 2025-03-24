#type conversion
age = int("25") #type conversion str -> int
price = float("19.99") #type conversion str -> float
text = str(55) #type conversion int -> str
is_active = bool(1) #type conversion int -> bool
print(age, price, text, is_active)

#conversion of iterables into data types like list, tuple, set.
number = range(5) #iterable
num_list = list(number)
num_tuple = tuple(number)
num_set = set(number)
print(num_list, num_tuple, num_set)

#Mathematical functions
distance = abs(-10) #absolute value
short_pi = round(3.14159, 2) #rounds the number to the specified digit
highest = max([3, 43, 4, 234, 54])
lowest = min([3, 43, 4, 234, 54])
total = sum([3, 43, 4, 234, 54])
print(distance, short_pi, highest, lowest, total)

#Sequence and Collection and functions
hello_len = len("hello")
sorted_letters = sorted(['b', 'a', 'c'])
rev_numbers = list(reversed([1, 2, 3, 4])) #reverse gives an iterable
combined = zip(['Alice', 'Bob', 'Charlie'], [25, 30, 35])
combined_list = list(combined)
print(hello_len, sorted_letters, rev_numbers, combined, combined_list)

#I/O
print("Hello World")
name = input("Enter You name: ")
print("Hello", name)

#Object and type inspection functions
a = 10
print(type(42), type('hello'), isinstance(42, int), isinstance('hello', str), id(10))

#Functional Programming Helpers
print(list(map(lambda x: x**2, [1, 2, 3, 4, 5])))
print(list(filter(lambda x: x%2==0, [1, 2, 3, 4, 5,])))

#All and Any
print(all([True, True, False])) #all -> returns true if all the elements are true
print(any([True, True, False])) #any -> returns true if any of the element is true

#Format function
print("Hello, {0}".format('World'))

#Function to convert between characters and unicode code points
print(chr(97), ord('a'), bin(10))
