_str = ["H", "e", "l", "l", "o", " ", "W", "o", "l", "d"]
print(_str[0]) #first char
print(_str[-2]) #second last character

_str[5] = "_"
print(_str)

for i in range(len(_str)):
    print(_str[i], end="")

print()

nested_list = [[1,2,3], [4,5,6], [7,8,9]]
print(nested_list[2][2])
