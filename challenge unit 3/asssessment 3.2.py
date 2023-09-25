def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Create some student objects
students = [
    Student("John Doe", "A1234", 3.8),
    Student("Jane Doe", "A5678", 3.6),
    Student("Bob Smith", "A2345", 3.9),
    Student("Alice Johnson", "A6789", 3.7),
]

# Test the sort_students function
sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
