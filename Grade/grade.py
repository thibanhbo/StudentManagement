class Grade:
    def __init__(self, student, course, score):
        self.student = student
        self.course = course
        self.score = score
        # xyz

    def show_grade(self):
        print(f"Grade: {self.student.name} - {self.course.course_name} = {self.score}")
