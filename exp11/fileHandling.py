import os 

def create_file(filename):
    with open(filename, "w") as file:
        file.write("File Handling!\n")
    print(f"'{filename}' created and initial content written.")

def append_to_file(filename):
    with open(filename, "a") as file:
        file.write("This line is added using append mode!\n")
    print(f"Append new line to '{filename}'.")

def read_file(filename):
    with open(filename, "r") as file:
        print(f"Reading full content of '{filename}'")
        content = file.read()
        print(content)

def read_lines(filename):
    with open(filename, "r") as file:
        print(f"Reading '{filename}' line by line: ")
        lines = file.readlines()
        for i, line in enumerate(lines, 0):
            print(f"{i}. {line.strip()}")

def read_with_readline(filename):
    with open(filename, "r") as file:
        print("Reading lines using readline(): ")
        line1 = file.readline()
        line2 = file.readline()
        print(f"First line: {line1.strip()}")
        print(f"Second line: {line2.strip()}")

def check_existence(filename):
    print(f"Checking if '{filename}' exists...")
    if os.path.exists(filename):
        print("File found")
    else :
        print("File not found!")

def rename_file(old_name, new_name):
    os.rename(old_name, new_name)
    print(f"Renamed '{old_name}' to '{new_name}'.")

def delete_file(filename):
    os.remove(filename)
    print(f"Deleted '{filename}' successfully.")

file_name = "demo.txt"
new_file_name = "demo_renamed.txt"

create_file(file_name)
append_to_file(file_name)
read_file(file_name)
read_lines(file_name)
read_with_readline(file_name)
check_existence(file_name)
rename_file(file_name, new_file_name)
check_existence(new_file_name)
delete_file(new_file_name)
check_existence(new_file_name)
