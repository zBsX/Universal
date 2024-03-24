import json
import re
import os


class Student:
    def __init__(self, student_id=None, student_name=None, student_age=None, student_gender=None, student_score=None):
        self.sid = []
        self.student_dict = {}
        self.student_id = student_id
        self.student_name = student_name
        self.student_age = student_age
        self.student_gender = student_gender
        self.student_score = student_score
        # self.patterns = r'"ID"\s*:\s*\d+'
    
    # File Check 检查文件
    def CheckDataFile(self):
        if not os.path.exists('data.json'):
            with open('data.json', 'w', encoding='utf-8') as file:
                json.dump({}, file)
        with open('data.json', 'r', encoding='utf-8') as file:
                check = file.read()
                if not check:
                    with open('data.json', 'w', encoding='utf-8') as file2:
                        file2.write('{}')
                else:
                    print('文件正常')
                
                
    # Init 文件初始化
    def InitSystem(self):
        self.CheckDataFile()
        global Tempinfo
        global data
        global Run
        Run = True
        data = dict()
        Tempinfo = dict()
        try:
            with open('data.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            self.sid = list(data.keys())
            # matches = re.findall(self.patterns, str(data))
            # self.sid = [int(i) for i in matches[::3]]
            print('学生ID:', self.sid)
        except json.decoder.JSONDecodeError:
            print('目前没有学生,正在创建学生库...')
            self.CheckDataFile()
            
    # ID 学生ID ### 修复重复ID
    def InputID(self) -> str:
           
            while Run:
                try:
                    self.student_id = str(input('请输入你想创建的ID: 按 -1 列出，按 0 退出 '))
                    
                    if int(self.student_id) < -1:
                        print('无效输入')
                        continue
                    if self.student_id in self.sid:
                        print('id已存在')
                        self.student_id = None
                        continue
                    if int(self.student_id) == -1:
                        print('学生列表:', data)
                        continue
                    if int(self.student_id) == 0:
                        print('Abort')
                        break
                    print('你的ID是:', self.student_id,'确定吗? y/n')
                    choice = str(input())
                    if choice.lower() == 'y':
                        return self.student_id
                    elif choice.lower() == 'n':
                        self.student_id == None
                        continue
                    else:
                        print('请输入y 或者n ')
                        continue
                except ValueError as Error:
                    print(Error)
                    continue
                
    # Name 名字
    def InputName(self) -> str:
                
                while Run:
                    try:
                        self.student_name = input('name:')
                        if self.student_name == 'q':
                            self.student_name = None
                            break
                        if not self.student_name.isalpha():
                            print('请输入正确的名字')
                            continue
                        if self.student_name is None:
                            print('你还没有输入名字！')
                            break
                        return self.student_name
                    except ValueError as Error:
                        print(Error)
                        continue
                print('你的名字是' , self.student_name)
                
    # Gender 性别             
    def InputGender(self) -> str:
                  
                while Run:
                    try:
                        self.student_gender = input('请选择你的性别: \f男man 女woman 退出q\n')
                    except ValueError:
                        print('性别输入错误')
                        continue
                    if self.student_gender.lower() not in {'man', 'woman', 'q'}:
                        print('性别输入错误')
                        continue
                    if self.student_gender == 'q':
                        print('退出')
                        break
                    print('你的性别是' , self.student_gender)
                    return self.student_gender
                
    # Score 分数            
    def InputScore(self) -> float:
                
                while Run:
                    try:
                        self.student_score = float(input('score (-1 to quit):'))
                        match self.student_score:
                            case score if score < -1:
                                print('不能小于0')
                                continue
                            case score if score > 750:
                                print('不能大于750')
                                continue
                            case _:
                                if score == -1:
                                    break
                                print('你的分数是', score)
                                return score
                    except ValueError as Error:
                        print(Error)
                        continue    
   
    def ExportJSON(self) -> json:
        
                # List 学生列表
                self.sid.append(self.student_id)
                
                # Dict 学生json字典
                print(Tempinfo)
                # data.update(Tempinfo)
                
                data[self.student_id] = Tempinfo
                
                # Save to local 本地json存储
                select = input('1 to add q to exit:')
                
                if select == '1':
                    with open('data.json', 'w', encoding='utf-8') as file:
                        json.dump(data, file, ensure_ascii=False, indent=4)
                    print('successfully export studentlist')
                    data.clear(); Tempinfo.clear()
                elif select == 'q':
                    exit()
                    
    # Student Selection Sys 学生选择系统
    def select_student(self) -> None:
        
        idset = set()
        while True:
            
            for idx,id in enumerate(self.sid, 1):
                print(f'{idx},{id}')
            try:
                with open('data.json', 'r', encoding='utf-8') as file:
                    student_data_dict = json.load(file)
                    print("dict:", student_data_dict)

                
                # matches = re.findall(self.patterns, str(student_data_dict))
                # print('matches:', matches)
                # self.sid = [int(i) for i in matches[::3]] ###
                print('学生id:', self.sid)

                if not self.sid:
                    print('目前没有学生')
                    break
                
            except json.decoder.JSONDecodeError: ### 如果使用continue 而不是break 则会反复报错反复印出'目前没有学生'
                print('目前没有学生')
                break
            try:
                selected_id = str(input('请输入想要查询的ID(按0退出):'))
                
                for id in self.sid:
                    idset.add(id)
                print(idset)
                
                if selected_id == '0':
                    # self.sid.clear()
                    break
                if selected_id in idset:
                    print(f'学生信息:{student_data_dict[str(selected_id)]}')
                    continue
                else:
                    print('未找到该学生')
                    continue

            except ValueError:
                print('无效输入')
                continue
            
    def DeleteID(self):
        while Run:
            self.InitSystem()
            print(data)
            idset = set()
            sidl = list(data.keys())
            for id in sidl:
                idset.add(id)
            selet = input('输入你想修改的学号:')
            
            if selet in idset:
                print('已选择ID:', selet)
                del data[selet]
                print(data)
                with open('data.json', 'w', encoding='utf-8') as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)
                idset.clear()
                print(idset)
                continue
            elif selet == 'q':
                break
            else:
                print('未找到ID')
                break
        
        
        
    
    
    
    
if __name__ == '__main__': ### 完成状态         
    self = Student()
    self.InitSystem()
    status = [False, False, False, False]
    Run = True
    
    while Run:
        selection = input('请选择create find gender name score q:')
        match selection:
            case 'create':          
                if not status[0]:
                    Tempinfo.setdefault('ID', self.InputID())
                    status[0] = True
                
                elif Tempinfo['ID'] == None:
                    print(self.InputID())
                    Tempinfo['ID'] = self.student_id
                
                else:
                    print('你已经输入过ID了,要修改吗？')
                    sele = input('y/n')
                    if sele == 'y':
                        Tempinfo['ID'] = self.InputID()
                    elif sele == 'n':
                        break
                    else:
                        print('无效输入')
                    continue
                    
                print(Tempinfo)
                continue
            case 'find':
                
                self.select_student()
                print(Tempinfo)
                continue
            
            case 'gender':
                
                if not status[1]:
                    Tempinfo.setdefault('Gender', self.InputGender())
                    status[1] = True
                else:
                    print('你已经输入过性别了')
                    continue
                    
                
                print(Tempinfo)
                continue
            
            case 'name':
                
                if not status[2]:
                    Tempinfo.setdefault('Name', self.InputName())
                    status[2] = True
                else:
                    print('你已经输入过名字了')
                    continue
                    
                print(Tempinfo)
                continue
            
            case 'score':
                
                if not status[3]:
                    Tempinfo.setdefault('Score', self.InputScore())
                    status[3] = True
                else:
                    print('你已经输入过分数了')
                    continue
                    
                print(Tempinfo)
                continue
            
            case 'del':
                self.DeleteID()
            
            case 'done':
                self.ExportJSON()
                status = [False, False, False, False]
            case 'q':
                break
                
            case _:
                print('输入错误')
                continue