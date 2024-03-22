''' home work '''
import json
import re

class Student:
    def __init__(self, student_id=None, student_name=None, student_age=None, student_gender=None, student_score=None):
        self.student_dict = {}
        self.student_list = []
        self.student_id = student_id
        self.student_name = student_name
        self.student_age = student_age
        self.student_gender = student_gender
        self.student_score = student_score
        global sid
        sid = []
        global patterns
        patterns = r'\b\d+\b'
        
    def inputid(self):
        run = True
        while run:
            
            with open('data.json', 'r') as file:
                data = json.load(file)
            # print(data)

            matches = re.findall(patterns, str(data))
            for i in matches[::3]:
                sid.append(i)
                print('学生id:' ,i, end=' ')

            print(sid)
            if matches:
                print(matches, type(matches))
            try:
                self.student_id = int(input('id (0 to quit,-1 to show):'))
                
                if str(self.student_id) in sid:
                    print('id已存在')
                    self.student_id = None
                    continue

                if self.student_id == -1:
                    print('学生列表:' ,data )
                    continue
                if self.student_id == 0:
                    print('abort')
                    break
                print('你的id是:' , self.student_id)
                
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
                    except ValueError as e:
                        print(e)
                        continue
                
                print('你的名字是' , self.student_name)
                if self.student_name == None:
                    print('你还没有输入名字！')
                while True:
                    try:
                        self.student_gender = int(input('1 for man,2 for woman ,0 to quit: '))
                    except ValueError:
                        print('性别输入错误')
                        continue
                    if self.student_gender not in [1, 2, 0]:
                        print('性别输入错误')
                        continue
                    break
                
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
                # list
                self.student_list.append(self.student_id)
                # dict
                self.student_dict.update(data)
                self.student_dict[self.student_id] = {'name' : self.student_name, 'gender' : self.student_gender,'score' : self.student_score}
                
                
                # print(str(self.student_dict))
                select = float(input('1 to recreate 2 to add 0 to exit'))
                
                if select == 1:
                    with open('data.json', 'w', encoding='utf-8') as file:
                        json.dump(self.student_dict, file, ensure_ascii=False, indent=4)
                    print('successfully export studentlist')
                elif select == 2:
                    with open('data.json', 'a', encoding='utf-8') as file:
                        file.write('\n')
                        json.dump(self.student_dict, file, ensure_ascii=False, indent=4)
                else:
                    break
                
            except ValueError:
                print('请输入正确的id')
                continue
        
        
        # print(self.student_dict)
        
    def select_student(self):
        # if not self.student_list: # self.student_list 如果是null（空的）则bool值为False，即不会执行if条件判断语句
        #     print('目前没有学生')
        #     exit()
        print(self.student_list)
        for idx,id in enumerate(self.student_list, 1):
            print(f'{idx},{id}')
        
        while True:
            try:
                with open('data.json', 'r') as file:
                    data2 = json.load(file)
                print('data2:', data2)
                
                matches = re.findall(patterns, str(data2))
                
                for i in matches[::3]:
                    sid.append(i)
                    print('学生id:' ,i, end=' ')
                
                selected_idx = int(input("Enter the number of the student id you want to check (0 to exit, -1 to read data): "))
                # if-else statement
                if selected_idx > len(self.student_list) or selected_idx < -1:
                    print('超出范围，请重试')
                    continue
                if selected_idx == 0:
                    break
                if selected_idx == -1:
                    with open('data.json', 'r') as data:
                        sdata = data.read()
                        print(sdata)
                        
                # select student id
                selected_id = self.student_list[selected_idx - 1]
                print(self.student_dict[selected_id])
                
            except ValueError:
                print('无效输入')
                continue
if __name__ == '__main__':                  
    null = False
    student = Student(null, null, null, null, null)
    student.inputid()
    student.select_student()