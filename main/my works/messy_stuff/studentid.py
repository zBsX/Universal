import json
import re
import os
# import tkinter

class Student:
    def __init__(self, student_id=None, student_name=None, student_age=None, student_gender=None, student_score=None):
        self.sid = []
        self.student_dict = {}
        self.student_id = student_id
        self.student_name = student_name
        self.student_age = student_age
        self.student_gender = student_gender
        self.student_score = student_score
        self.patterns = r'\b\d+\b'
        
    def check_data_file(self):
        if not os.path.exists('data.json'):
            with open('data.json', 'w', encoding='utf-8') as file:
                json.dump({}, file)

    def inputid(self):
        run = True
        self.check_data_file()
        
        while run:
            with open('data.json', 'r', encoding='utf-8') as file:
                data = file.read()
            if not data:
                data = {}
            else:
                data = json.loads(data)
                
            matches = re.findall(self.patterns, str(data))
            self.sid = [int(i) for i in matches[::3]]
            print('学生id:', self.sid)

            try:
                self.student_id = int(input('请输入你想创建的ID: \f 按 -1 列出，按 0 退出 \f '))
                if not self.student_id >= -1:
                    print('无效输入')
                    continue
                if self.student_id in self.sid:
                    print('id已存在')
                    self.student_id = None
                    continue

                if self.student_id == -1:
                    print('学生列表:', data)
                    continue
                if self.student_id == 0:
                    print('Abort')
                    break
                print('你的id是:', self.student_id)
                
                while True:
                    try:
                        self.student_name = input('name:')
                        if self.student_name == 'q':
                            self.student_name = None
                            break
                        if not self.student_name.isalpha():
                            print('请输入正确的名字')
                            continue
                        break
                    except ValueError as Error:
                        print(Error)
                        continue
                
                print('你的名字是' , self.student_name)
                if self.student_name is None:
                    print('你还没有输入名字！')
                while True:
                    try:
                        self.student_gender = input('请选择你的性别: \f男 女 退出\n')
                    except ValueError:
                        print('性别输入错误')
                        continue
                    if self.student_gender.lower() not in {'男', '女', '退出'}:
                        print('性别输入错误')
                        continue
                    break
                
                if self.student_gender == '退出':
                    break
                print('你的性别是' , self.student_gender)
                
                while True:
                    try:
                        
                        self.student_score = float(input('score (-1 to quit):'))
                        match self.student_score:
                            case self.student_score if self.student_score < -1:
                                print('不能小于0')
                                continue
                            case self.student_score if self.student_score > 750:
                                print('不能大于750')
                                continue
                            case _:
                                if self.student_score == -1:
                                    break
                                print('你的分数是' , self.student_score)
                                break
                        
                    except ValueError as e:
                        print(e)
                        continue    
                
                # list
                self.sid.append(self.student_id)
                
                # dict
                data[self.student_id] = {'name' : self.student_name, 'gender' : self.student_gender,'score' : self.student_score}
                
                # print(str(self.student_dict))
                select = input('1 to add q to exit:')
                
                if select == '1':
                    with open('data.json', 'w', encoding='utf-8') as file:
                        json.dump(data, file, ensure_ascii=False, indent=4)
                    print('successfully export studentlist')
                elif select == 'q':
                    break

            except ValueError:
                print('Error')
                continue
        # print(self.student_dict)
        
    def select_student(self):
        idset = set()
        while True:
            for idx,id in enumerate(self.sid, 1):
                print(f'{idx},{id}')
            
            with open('data.json', 'r', encoding='utf-8') as file:
                student_data_dict = json.load(file)
            # print('student_data_dict:', student_data_dict)
            
            matches = re.findall(self.patterns, str(student_data_dict))
            self.sid = [int(i) for i in matches[::3]]
            print('学生id:', self.sid)

            if not self.sid: # sid 如果是null（空的）则bool值为False，即不会执行if条件判断语句
                print('目前没有学生')
                exit()
            try:
                selected_id = int(input('请输入想要查询的ID(按0退出):'))
                
                for id in self.sid:
                    idset.add(id)
                # print(idset, student_data_dict)
                if selected_id in idset:
                    print(f'学生信息:{student_data_dict[str(selected_id)]}')
                elif selected_id == 0:
                    exit()
                else:
                    print('未找到该学生')
                
                
                
                
                
                # selected_idx = int(input("Enter the number of the student id you want to check (0 to exit, -1 to read data): "))
                # # if-else statement
                # if selected_idx > len(self.sid) or selected_idx < -1:
                #     print('超出范围，请重试')
                #     continue
                # if selected_idx == 0:
                #     break
                # elif selected_idx == -1:
                #     print(student_data_dict)
                # else:
                    # selected_id = self.sid[selected_idx - 1]
                    # print(student_data_dict[str(selected_id)])
                    # selected_id = 
                    
                self.sid.clear()
                
            except ValueError:
                print('无效输入')
                continue
            
if __name__ == '__main__':                  
    self = Student()
    selection = input('请选择创建还是查找:')
    if '创建' in selection:
        Student.inputid(self)
    elif '查找' in selection:
        Student.select_student(self)
    else:
        print('输入错误')
