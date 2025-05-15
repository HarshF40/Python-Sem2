students = {
    "Alice": {"math": 88, "science": 92, "english": 81},
    "Bob": {"math": 76, "science": 85, "english": 78},
    "Charlie": {"math": 90, "science": 87, "english": 85}
}

# 1. Accessing nested dictionary values
print("Alice's Math Score:", students["Alice"]["math"])

# 2. Updating nested values: Bob improved his English score
students["Bob"]["english"] = 82
print("Bob's updated English score:", students["Bob"]["english"])

# 3. Adding a new student
students["Diana"] = {"math": 91, "science": 89, "english": 88}
print("Added new student: Diana")

# 4. Calculating average score per student using dictionary comprehension
average_scores = {
    name: sum(scores.values()) / len(scores)
    for name, scores in students.items()
}
print("\nAverage scores per student:")
for name, avg in average_scores.items():
    print(f"{name}: {avg:.2f}")

# 5. Sorting students by average score (descending)
sorted_by_avg = sorted(average_scores.items(), key=lambda x: x[1], reverse=True)
print("\nStudents sorted by average score:")
for name, avg in sorted_by_avg:
    print(f"{name}: {avg:.2f}")

# 6. Merging additional info (e.g., student year) into existing student records
year_info = {
    "Alice": "Sophomore",
    "Bob": "Freshman",
    "Charlie": "Senior",
    "Diana": "Junior"
}

for name, year in year_info.items():
    students[name]["year"] = year

# 7. Printing full info
print("\nFull student records after merging year info:")
for name, info in students.items():
    print(f"{name} -> {info}")

# 8. Filtering students with math score above 85
high_math = {
    name: info for name, info in students.items() if info["math"] > 85
}
print("\nStudents with Math > 85:")
for name in high_math:
    print(name)
