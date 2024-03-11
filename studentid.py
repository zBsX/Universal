''' home work '''
class Student:
    def __init__(self, student_id, student_name, student_age, student_gender, student_score):
        self.student_dict = {}
        self.student_list = []
        """""
        self.student_id = student_id
        self.student_name = student_name
        self.student_age = student_age
        self.student_gender = student_gender
        self.student_score = student_score
        """""
        
    def inputid(self):
        run = True
        while run:
            try:
                self.student_id = int(input('id (0 to quit,-1 to show):'))
                if self.student_id in self.student_dict:
                    print('id已存在')
                    continue
                if self.student_id == -1:
                    print('学生列表:' , self.student_dict)
                    continue
                if self.student_id == 0:
                    break
                print('你的id是:' , self.student_id)
                
                while True:
                    try:
                        self.student_name = input('name(0 to quit):')
                        if not self.student_name.isalpha():
                            print('请输入正确的名字')
                            continue
                        break
                    except ValueError as e:
                        print(e)
                        continue
                if self.student_name == '0':
                    break
                print('你的名字是' , self.student_name)
                self.student_gender = int(input('1 for man,2 for woman ,0 to quit: '))
                
                
                if self.student_gender == 0:
                    break
                if self.student_gender == 1:
                    self.student_gender = 'man'
                elif self.student_gender == 2:
                    self.student_gender = 'woman'
                print('你的性别是' , self.student_gender)
                while True:
                    try:
                        self.student_score = float(input('score (-1 to quit):'))
                        if self.student_gender == -1:
                            break
                        print('你的分数是' , self.student_score)
                        break
                    except ValueError as e:
                        print(e)
                        continue    
                
                self.student_list.append(self.student_id)
                self.student_dict[self.student_id] = {'name' : self.student_name, 'gender' : self.student_gender,'score' : self.student_score}
                print(str(self.student_dict))
                
                with open('data.txt', 'w') as file:
                    file.write(str(self.student_id))
                    file.write(str(self.student_dict))
                
            except ValueError:
                print('请输入正确的id')
                continue
        
        
        print(self.student_dict)
        
    def select_student(self):
        if not self.student_list: # self.student_list 如果是null（空的）则bool值为False，即不会执行if条件判断语句
            print('目前没有学生')
            exit()
        print(self.student_list)
        for idx,id in enumerate(self.student_list, 1):
            print(f'{idx},{id}')
        
        while True:
            try:
                
                selected_idx = int(input("Enter the number of the student id you want to check (0 to exit, -1 to read data): "))
                
                if selected_idx > len(self.student_list) or selected_idx < -1:
                    print('超出范围，请重试')
                    continue
                if selected_idx == 0:
                    break
                if selected_idx == -1:
                    with open('data.txt', 'r', encoding='utf-8') as data:
                        sdata = data.read()
                        print(sdata)
                    
                
                # selected_id = self.student_list[selected_idx - 1]
                # print(self.student_dict[selected_id])
            except ValueError:
                print('无效输入')
                continue
                
            
            
        
null = False
student = Student(null, null, null, null, null)
student.inputid()
student.select_student()