# Lists

# 0. Creating a variable type list
def create_varied_lists():
    ls1 = [1,2,3]
    print(ls1)
    ls2 = ["Harsh", "BrrBrrPatapim"]
    print(ls2)
    ls3 = [1,2.4,"Harsh",[4,"hello"]]
    print(ls3)

# Indexing and Slicing
def index(lst, i):
    print(f"Element at {i} position: {lst[i-1]}")
    print(f"Elements before {i} position: {lst[0:i-1]}")
    print(f"Elements after {i} position : {lst[i-1:len(lst)]}")

# 1. Creating Lists using range() Function
def create_list(n):
    return list(range(n))

# 2. Updating the Elements of a List
def update_element(lst, index, value):
    lst[index] = value
    return lst

# 3. Concatenation of Two Lists
def concat_lists(a, b):
    return a + b

# 4. Repetition of Lists
def repeat_list(lst, times):
    return lst * times

# 5. Membership in Lists
def is_member(lst, item):
    return item in lst

# 6. Aliasing and Cloning Lists
def alias_list(lst):
    return lst

def clone_list(lst):
    return lst[:]

# 7. Methods to Process Lists
def sum_list(lst):
    return sum(lst)

# 8. Finding Biggest and Smallest Elements in a List
def min_max(lst):
    return min(lst), max(lst)

# 9. Sorting the List Elements
def sorted_list(lst):
    return sorted(lst)

def sort_in_place(lst):
    lst.sort()
    return lst

# 10. Number of Occurrences of an Element in the List
def count_occurrences(lst, item):
    return lst.count(item)

# 11. Finding Common Elements in Two Lists
def common_elements(a, b):
    return list(set(a) & set(b))

# 13. Nested Lists
def get_nested(lst, i, j):
    return lst[i][j]

# 14. Nested Lists as Matrices
def matrix_dimensions(matrix):
    return len(matrix), len(matrix[0])

# 15. List Comprehensions
def squares_list(n):
    return [i*i for i in range(n)]

# Placeholder for missing mixed_list function
def mixed_list():
    return [1, "text", 3.14, [1, 2]]

if __name__ == '__main__':
    create_varied_lists()
    print("create_list(5):", create_list(5))
    index([9,8,7,6,5], 3)
    print("update_element:", update_element([1,2,3], 1, 9))
    print("concat_lists:", concat_lists([1,2], [3,4]))
    print("repeat_list:", repeat_list(['a','b'], 3))
    print("is_member:", is_member([1,2,3], 2))
    print("alias_list and clone_list difference:")
    orig = [1,2]
    a = alias_list(orig)
    c = clone_list(orig)
    a.append(3)
    c.append(4)
    print(orig, a, c)
    print("sum_list:", sum_list([1,2,3]))
    print("min_max:", min_max([5,3,9]))
    print("sorted_list:", sorted_list([3,1,2]))
    print("count_occurrences:", count_occurrences([1,2,2,3], 2))
    print("common_elements:", common_elements([1,2,3], [2,3,4]))
    print("mixed_list:", mixed_list())
    matrix = [[1,2,3],[4,5,6]]
    print("matrix_dimensions:", matrix_dimensions(matrix))
    print("squares_list:", squares_list(5))
