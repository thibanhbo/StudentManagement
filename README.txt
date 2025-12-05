1. MỤC ĐÍCH PHẦN MỀM
- Phần mềm Student Management System được xây dựng nhằm mô phỏng một hệ thống quản lý sinh viên cơ bản 
- Trong project này, các modules được thiết lập bao gồm: Register Module, Course Module, Grade Module, Student Module, Admin Module
- Hệ thống cho phép quản lý thông tin sinh viên, môn học, đăng ký môn, chấm điểm và vai trò quản trị. 

2. DANH SÁCH MODULE ĐÃ CÀI ĐẶT
- Student Module: Quản lý thông tin sinh viên (ID, tên, chuyên ngành)
- Course Module: Lưu trữ thông tin môn học (mã môn, tên môn, số tín chỉ)
- Register Module: Thực hiện đăng ký môn học cho sinh viên
- Grade Module: Lưu điểm và hiển thị kết quả học tập
- Admin Module: Quản lý người dùng và phân quyền đơn giản

3. CHỨC NĂNG CHÍNH (đã implement)
- Tạo sinh viên, hiển thị thông tin
- Tạo môn học, hiển thị thông tin
- Cho sinh viên học môn học đã tạo và thực hiện đăng ký
- Gán điểm cho sinh viên theo từng môn, hiển thị điểm 
- Tạo tài khoản admin và hiển thị thông tin quản trị 


4. THÀNH VIÊN THỰC HIỆN
- Phạm Minh Thi

5. HƯỚNG DẪN CHẠY THỬ
Folder project tên: StudentManagement 
Trong folder có chứa tất cả module và hàm main 
1. Mở project bằng Visual Studio 
2. Mở terminal và đứng ở thư mục StudentManagement 
3. Nhập câu lệnh ( python -m StudentManagement ) để chạy
4. Màn hình sẽ hiển thị thông tin sinh viên, cousre, điểm của sinh viên kèm theo admin quản lý/nhập thông tin của sinh viên