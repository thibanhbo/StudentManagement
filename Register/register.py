class Register:
    def __init__(self, student, course):
        self.student = student
        self.course = course

    def register_course(self):
        print(f"{self.student.name} has registered course {self.course.course_name}")
