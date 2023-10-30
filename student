class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average_score(self):
        return sum(self.scores) / len(self.scores)

class GradeBook:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def class_average(self):
        return sum([student.average_score() for student in self.students]) / len(self.students)

# 创建学生和成绩
student1 = Student("Alice", [85, 90, 75, 88])
student2 = Student("Bob", [75, 80, 82, 79])
student3 = Student("Charlie", [90, 92, 88, 94])

# 创建成绩册并添加学生
grade_book = GradeBook()
grade_book.add_student(student1)
grade_book.add_student(student2)
grade_book.add_student(student3)

# 打印每个学生的平均分和班级平均分
for i, student in enumerate(grade_book.students, 1):
    print(f"Student {i}: {student.name}, Average Score: {student.average_score()}")

print(f"Class Average Score: {grade_book.class_average()}")
