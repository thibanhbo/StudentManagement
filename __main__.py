from StudentManagement.Student.student import Student
from StudentManagement.Course.course import Course
from StudentManagement.Register.register import Register
from StudentManagement.Grade.grade import Grade
from StudentManagement.Admin.admin import Admin

def main():

    # Tạo sinh viên
    s1 = Student("SV001", "Nguyen Van A", "Computer Science")

    # Tạo môn học
    c1 = Course("CSE101", "Introduction to Programming", 3)

    # Hiển thị thông tin
    s1.show_info()
    c1.show_course()

    # Đăng ký môn
    reg = Register(s1, c1)
    reg.register_course()

    # Gán điểm
    g = Grade(s1, c1, 8.5)
    g.show_grade()

    # Admin test
    ad = Admin("admin01", "Manager")
    ad.show_info()


if __name__ == "__main__":
    main()
