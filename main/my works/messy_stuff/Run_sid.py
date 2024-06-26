import studentid2

### Selet Choice模块
def Selet(FUNC, Model: str) -> None:
    while Run:
        print('你已经输入过了,要修改吗？')
        sele = input('y/n')
        if sele == 'y':
            studentid2.Tempinfo[Model] = FUNC()
            print(studentid2.Tempinfo)
            return
        elif sele == 'n':
            break
        else:
            print('无效输入')
        continue
        

if __name__ == '__main__': ### main   
    self = studentid2.Student()
    self.InitSystem()
    status = [False, False, False, False]
    Run = True
    
    while Run:
        selection = input('请选择create find gender name score del done q:')
        match selection:
            case 'create':          
                if not status[0]:
                    studentid2.Tempinfo.setdefault('ID', self.InputID())
                    status[0] = True
                
                elif studentid2.Tempinfo['ID'] == None:
                    print(self.InputID())
                    studentid2.Tempinfo['ID'] = self.student_id
                else:
                    Selet(self.InputID, 'ID')
                continue

            case 'find':
                
                self.select_student()
                print(studentid2.Tempinfo)
                continue
            
            case 'gender':
                
                if not status[1]:
                    studentid2.Tempinfo.setdefault('Gender', self.InputGender())
                    status[1] = True

                elif studentid2.Tempinfo['Gender'] == None:
                    studentid2.Tempinfo['Gender'] = self.InputGender()
                else:
                    Selet(self.InputGender, 'Gender')
                continue
            
            case 'name':
                
                if not status[2]:
                    studentid2.Tempinfo.setdefault('Name', self.InputName())
                    status[2] = True

                elif studentid2.Tempinfo['Name'] == None:
                    studentid2.Tempinfo['Name'] = self.InputName()
                else:
                    Selet(self.InputName, 'Name')
                continue

            case 'score':
                
                if not status[3]:
                    studentid2.Tempinfo.setdefault('Score', self.InputScore())
                    status[3] = True
                else:
                    Selet(self.InputScore, 'Score')
                continue
            
            case 'del':

                self.DeleteID()
            
            case 'done':
                if status[0] and studentid2.Tempinfo['ID'] != None:
                    self.ExportJSON()
                    status = [False, False, False, False]
                elif studentid2.Tempinfo['ID'] == None or not status[0]:
                    print('你还没有输入ID')
                    continue
                else:
                    print('奇怪')

            case 'q':
                break
                
            case _:
                print('输入错误')
                continue