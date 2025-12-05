class Student:
    def __init__(self, student_id, name, major):
        self.id = student_id
        self.name = name
        self.major = major

    def show_info(self):
        print(f"Student: {self.id} - {self.name} - {self.major}")