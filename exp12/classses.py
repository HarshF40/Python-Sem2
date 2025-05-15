class Student:
    def __init__(self, name, roll_number, course):
        self.name = name
        self.roll_number = roll_number
        self.course = course
        self.marks = {}

    def add_mark(self, subject, score):
        self.marks[subject] = score

    def calculate_average(self):
        if self.marks:
            return sum(self.marks.values()) / len(self.marks)
        return 0

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Course: {self.course}")
        print("Marks:")
        for subject, score in self.marks.items():
            print(f"  {subject}: {score}")
        print(f"Average: {self.calculate_average():.2f}")
        print("-" * 40)

student1 = Student("Ayesha", 101, "Computer Science")
student1.add_mark("Math", 90)
student1.add_mark("Physics", 85)
student1.add_mark("Programming", 95)

student2 = Student("Rahul", 102, "Mechanical Engineering")
student2.add_mark("Thermodynamics", 88)
student2.add_mark("Mechanics", 78)

student3 = Student("Mira", 103, "Electrical Engineering")
student3.add_mark("Circuits", 92)
student3.add_mark("Signals", 81)
student3.add_mark("Systems", 87)

print("Student Records:\n")
student1.display_info()
student2.display_info()
student3.display_info()
