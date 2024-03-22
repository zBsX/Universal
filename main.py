from studentid import Student
self = Student()
selection = input('请选择创建还是查找:')
if selection == '创建':
    Student.inputid(self)
elif selection == '查找':
    Student.select_student(self)