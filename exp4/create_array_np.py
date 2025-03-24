import numpy as np

print("Array using List:", np.array([1, 2, 3, 4, 5]))
print("Array using tuple:", np.array((1, 2, 3, 4, 5)))
print("Complex Array:", np.array([1+2j, 3+4j, 5+6j]))
print("Array using arange:", np.arange(0, 10, 1)) #numbers between 0 (incl) to 10 (excl) with step of 1
print("Array using linspace:", np.linspace(0, 1, 5)) #5 numbers between 0 to 1
print("Array using random number:", np.random.rand(5)) #Random number between 0 and 1, array of size 5
