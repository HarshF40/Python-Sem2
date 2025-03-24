a, b = 1, 11

# Arithmetic Operators
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

# Assignment operator
c = a + b + 88
print(c)
c += 1
print(c)
c -= 1
print(c)
c *= 1
print(c)
# same for other remaining Arithmetic operators

# Comparison operators
print(a == b)# == equal
print(a != b)# != Not equal
print(a > b)# > Greater than
print(a < b)# < Less than
print(a >= b)# >= Greater than or equal to
print(a <= b)# <= Less than or equal to

# Logical Operators
x = True
y = False
print(x and y)
print(x or y)
print(not x)

# Bitwise Operators
z = 5
y = 1
print(z & y)
print(z | y)
print(z ^ y)
print(~z)
print(z<<2)
print(z>>2)

# Identity Operators
list1 = [1, 11, 111]
list2 = [1, 11, 111]
list3 = list1

print(list1 is list2, list1 is list3)
print(list2 is not list3)

# Membership Operators
print(1 in list1, 1111 in list2)
print('One' in list3)

# Ternary Operators
print("yes" if z>y else "no")
