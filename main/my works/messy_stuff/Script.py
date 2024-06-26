from tkinter import ttk
from tkinter import *
import json

Tasks_dict = dict()
counter = 0
sign_set = set()
d_conuter = 0
Label_list = []
Total_Tasks = ""
status = [False, False]
details = {}
TASKS_HEIGH = 111
TASKS_ITEMS = 3
Global_height = 1
LIST_HEIGHT = TASKS_HEIGH * TASKS_ITEMS
MAINFRAME_WIDGETS_HEIGHT = 54
Tempinfo = []


### Main UI
class UI:
    def __init__(self):
        # Main Root
        self.root = Tk()
        self.mainframe = Frame(self.root)
        self.root.title("ToDoList")
        self.root.geometry("400x500")
        self.mainframe.pack(fill="both", expand=True)
        self.root.iconbitmap("aw.ico")


        # Fields
        self.field = ttk.Entry(self.mainframe, width=40)
        self.field.pack(anchor="center")

        # Buttons
        self.button = ttk.Button(self.mainframe, text="Done", command=self.Scripts)
        self.button.pack(anchor="center")

        # Canvas
        self.canvas = Canvas(self.mainframe, scrollregion=(0,0,self.mainframe.winfo_width(), Global_height), bg="red")
        self.canvas.pack(side="left", fill="both", expand=True)
        
        # NewFrame
        self.ImportJSON()
        self.new_frame = Frame(self.canvas, bg="green")
        self.Add_Tasks()
        print("Load_counter:", counter)
        self.canvas.create_window(
                (0, 0), 
                window=self.new_frame, 
                anchor="nw", 
                width=381, 
                height=Global_height
            )
        

        # Slider 
        self.slider = ttk.Scrollbar(self.canvas, orient="vertical", command=self.canvas.yview)
        self.slider.pack(side="right", fill="y")

        # Configs 
        self.canvas.configure(yscrollcommand=self.slider.set)

        ## bar 
        self.canvas.bind_all("<MouseWheel>", lambda event: self.canvas.yview_scroll(-int(event.delta / 60), "units"))

        # resize the frame 
        self.mainframe.bind("<Configure>", lambda event: self.Resize(event))

        # Main Loop
        self.mainloop = mainloop()

### Main Scripts 

    ## 'Done' button
    def Scripts(self):
        global counter
        global Total_Tasks
        
        Tasks_dict[f"Task_{counter}"] = self.field.get() # You can add + " \n" to increase padding between Title and Detail
        print(Tasks_dict)

        self.Resize(event=None)

        self.Details()

        print(details)

        return

    ## Ok button
    def Ok_button(self, window, detail_field):
        global status
        global details
        global d_conuter
        global counter
        global sign_set
        global Global_height

        # add task height
        Global_height += LIST_HEIGHT
        print("global height:", Global_height)

        # resizing
        self.Resize(event=None)

        # load details
        details[f"Detail_{d_conuter}"] = detail_field.get()

        # save as json
        self.ExportJOSN()

        print(details, Tasks_dict)


        ## Add Tasks

        # Main Title
        
        sign_set.add(counter)
        print(" ok button sign_set:", sign_set)
        sign = list(sign_set)

        t = ttk.Label(self.new_frame, text=Tasks_dict[f"Task_{counter}"], font=("", 20))
        t.pack(anchor="w")

        # details Text
        
        t2 = ttk.Label(self.new_frame, text=details[f"Detail_{d_conuter}"])
        t2.pack(anchor="w")


        # Finished Button
        b = ttk.Button(self.new_frame, text=f"Finished{sign}", command=lambda: self.Finished(t, t2, b, sign_set))
        b.pack(anchor="e")

        # global counter
        counter += 1
        d_conuter += 1
        # add to sign set
        sign_set.add(counter)
        print("sign_set:", sign_set)
        print("Counter:", counter)
        print("d_counter", d_conuter)
        # print(details)

        # destroy edit window
        window.destroy()
        status[0] = False 

        return


    def Finished(self, text, text2, button, sign_set):
        global status

        print(sign_set)

        # Comfirm Window
        if status[1] == False:
            top = Toplevel()
            top.protocol("WM_DELETE_WINDOW", lambda: self.Close(top, 1))
            top.iconbitmap("awd.ico")
            t = ttk.Label(top, text="Confirm?", font=20, padding=30, width=20, anchor="center")
            t.pack()
            b1 = ttk.Button(top, text="Yes", command=lambda: self.Destroy_Script(top, 1, text, text2, button))
            b2 = ttk.Button(top, text="No", command=lambda: self.Close(top, 1))
            b1.pack()
            b2.pack()
            status[1] = True
        else:
            print("Opening")
            
            return
        

    def Destroy_Script(self, window, member, text, text2, button):
        global Global_height
        
        
        # subtract by task height
        Global_height -= LIST_HEIGHT
        print("global height:", Global_height)

        # Scripts
        # self.Resize(event=None)
        # self.update_canvas_height()
        self.ImportJSON()
        self.DeleteJSON()



        # destroy things
        self.Close(window, member)
        button.destroy()
        text.destroy()
        text2.destroy()

        return


    ## details window
    def Details(self):
        global status
        global d_conuter

        if status[0] == False:
            top = Toplevel()
            top.protocol("WM_DELETE_WINDOW", lambda: self.Close(top, 0))
            top.iconbitmap("awa.ico")
            top.title("Editing details")
            f = ttk.Entry(top, width=40)
            b = ttk.Button(top, text="Ok", command=lambda: self.Ok_button(top, f))
            f.pack()
            b.pack()
            
            status[0] = True
        else:
            print("Opening")
            
            return

    # refreshing the details for editing
    def Refresh_Details(self):
        self.field.destroy()
        new_details_field = ttk.Label(self.mainframe, text=details)
        new_details_field.pack(anchor="w")

        return new_details_field

    # main resize
    def Resize(self, event):
        global Global_height

        print("mainframe width:", self.mainframe.winfo_width())
        

        if event == None:                                # 静态时

            if (Global_height <= self.canvas.winfo_height()): # 窗口大于任务栏长度
                
                self.Create_New_Frame(None)
                print("_1")
                self.update_canvas_height()

                self.canvas.unbind_all("<MouseWheel>")

                return
            
            elif (Global_height > self.canvas.winfo_height()): # 窗口小于任务栏长度，任务栏可以滑动
                
                self.Create_New_Frame(None)
                print("_2")
                self.update_canvas_height()

                self.canvas.bind_all("<MouseWheel>", lambda event: self.canvas.yview_scroll(-int(event.delta / 60), "units"))

                return
        
        else:                                           # 活动时

            if (Global_height <= self.mainframe.winfo_height() - MAINFRAME_WIDGETS_HEIGHT): # 窗口大于任务栏长度

                self.Adjust_New_Frame(event)
                print("_3")
                self.update_canvas_height()

                self.canvas.unbind_all("<MouseWheel>")
                


            elif (Global_height > self.mainframe.winfo_height() - MAINFRAME_WIDGETS_HEIGHT): # 窗口小于任务栏长度，任务栏可以滑动

                print(self.mainframe.winfo_height(), "<", Global_height)

                self.Adjust_New_Frame(event)
                print("_4")
                self.update_canvas_height()

                self.canvas.bind_all("<MouseWheel>", lambda event: self.canvas.yview_scroll(-int(event.delta / 60), "units"))
                
        return


    # draw tasks on the canvas
    def Adjust_New_Frame(self, event):
        print("ok")
        if event == None:
            index_inactive = self.Create_New_Frame(None)
            self.canvas.itemconfigure(index_inactive)

        else:
            index_active = self.Create_New_Frame(event)
            self.canvas.itemconfigure(index_active)
        return
    

    def Create_New_Frame(self, event):

        if event == None: # 静态时
            print("static")

            index_inactive = self.canvas.create_window(
                (0, 0), 
                window=self.new_frame, 
                anchor="nw", 
                width=self.mainframe.winfo_width() - 19, 
                height=Global_height
            )

            print("INDEX_INACTIVE:", index_inactive)

            return index_inactive
        
        else: # 活动时
            print("dynamic")

            index_active = self.canvas.create_window(
                (0, 0), 
                window=self.new_frame, 
                anchor="nw", 
                width=event.width -19, 
                height=Global_height
            )


            print("INDEX_ACTIVE:", index_active)

        return index_active


    # update the scrollbar depending on the tasks
    def update_canvas_height(self):   # 修改 Canvas 的高度
        global Global_height
        print("updated canvas height")
        # self.canvas.config(height=Global_height)
        
        # 重新配置 Canvas 的大小
        self.canvas.update_idletasks()

        # 更新 Canvas 的滚动区域
        self.canvas.config(scrollregion=(0, 0, self.canvas.winfo_width(), Global_height))

        return


    # closing windows and update status 
    def Close(self, window=None, member=None):
        global status

        if window == None:
            status[member] = False

        else:

            window.destroy()
            status[member] = False

        return

    # clear button for clearing the words
    def Clear(self, field):
        field.delete(0, END)

        return
    


    def ExportJOSN(self):
        global details
        global Tasks_dict

        with open("data.json", "w", encoding="UTF-8") as file:
            json.dump((details, Tasks_dict), file, ensure_ascii=False, indent=4)


        return



    def ImportJSON(self):
        global details
        global Tasks_dict
        global counter
        global d_conuter
        global data

        with open("data.json", "rt", encoding="UTF-8") as file:
            
            try:
                data = json.load(file)
                details = data[0]
                Tasks_dict = data[1]
                d_conuter = len(data[0])
                counter = len(data[1])
                # print(details, Tasks_dict)
            except json.decoder.JSONDecodeError:
                print("NO DATA CURRENTLY!!!")



    def DeleteJSON(self): # //////////////////// working on /////////////////////////////
        global data
        global Tempinfo
        global sign_set

        Tempinfo = data[:]
        details_dict_local = Tempinfo[0]
        tasks_dict_local = Tempinfo[1]
        details_dict_local.pop(f"Detail_{1}")
        tasks_dict_local.pop(f"Task_{1}")


        with open("data.json", "w", encoding="UTF-8") as file:
            json.dump(Tempinfo, file, ensure_ascii=False, indent=4)
        
        return

        


    def Add_Tasks(self) -> dict: # //////////////////// working on /////////////////////////////
        global counter
        global d_conuter
        global Global_height
        global sign_set
        
        # local_sign = {} # define local sign_set 定义 局部标签
        tasks_sign_list = [] # define local tasks sign_set list 定义 局部任务导入标签
        details_sign_list = [] # define local details list 定义 局部注解(details)导入标签

        print("addtasks d_counter:", d_conuter)
        print("counter:", counter)
        
        for key in Tasks_dict.keys(): # for 循环 遍历tasks 序号
            # print("taskskey:", keys)

            tasks_sign_list.append(key)

            # print("tasks_sign_list:", tasks_sign_list)
            # print("tasks_sign_list_str:", tasks_sign_list[0])
        for key in details.keys(): # for 循环 遍历details 序号
            # print("detailskey:", keys)

            details_sign_list.append(key)

            # print("details_sign_list", details_sign_list)

        # relieve memory
        del key


        # set a local counter to iterate
        LocalCounter = 0 
        # Get the Max Count of the Tasks
        MaxTaskCount = max(tasks_sign_list)
        print("max value:", MaxTaskCount)
        # Get the actual <n> integer value
        n = int(MaxTaskCount[5])
        print("Max tasks count:", n)

        while LocalCounter < len(tasks_sign_list):
            
            found = False
            for i in range(n):  # 检查连续的 <n> 个索引  //////////////////// working on /////////////////////////////
                if (f"{LocalCounter + i}" in tasks_sign_list[LocalCounter]):
                    self.Iterate_Tasks(LocalCounter + i)
                    found = True
                    break

            if (not found):
                print("does not exist!!!", "// LocalCounter:", LocalCounter)

            LocalCounter += 1













            # if (f"{LocalCounter}" in tasks_sign_list[LocalCounter] and f"{LocalCounter}" in details_sign_list[LocalCounter]): # index for tasks and details, "<number>" 用来判断是否存在与 tasks details dictionary
            #     print("// LocalCounter:", LocalCounter)
            #     self.Iterate_Tasks(LocalCounter)


            # elif (f"{LocalCounter + 1}" in tasks_sign_list[LocalCounter]):
            #     self.Iterate_Tasks(LocalCounter + 1)


            # elif (f"{LocalCounter + 2}" in tasks_sign_list[LocalCounter]):
            #     self.Iterate_Tasks(LocalCounter + 2)


            # elif (f"{LocalCounter + 3}" in tasks_sign_list[LocalCounter]):
            #     self.Iterate_Tasks(LocalCounter + 3)


            # elif (f"{LocalCounter + 4}" in tasks_sign_list[LocalCounter]):
            #     self.Iterate_Tasks(LocalCounter + 4)


            # elif (f"{LocalCounter + n}" in tasks_sign_list[LocalCounter]):
            #     self.Iterate_Tasks(LocalCounter + n)

                
            # else:
            #     print("dosnt exist!!!", "// LocalCounter:", LocalCounter)

            # LocalCounter += 1



        ## 使用 for 循环 遍历counter 并且 if 判断是否存在于 读取的json文件中 (test)
        # for iter, index in enumerate(range(counter)):
        #     if (str(iter) in tasks_sign_list[iter] and str(index) in details_sign_list[index]):
        #         self.Iterate_Tasks(iter, index)
        #         # local_sign[sign_set] = f"Task_{iter}"
        #         # print("loaclsign:", local_sign)
        #     else:
        #         print("dosnt exist!!!")
        
        # print("localsign:", local_sign)


        return
    

    ## Add buttons 添加组件 ；每次调用Iterate_Tasks方法时，其中的局部变量t、t2和b都会在不同的内存空间中创建。
    def Iterate_Tasks(self, iter): # 因为不同的组件被创建在不同的内存空间，所以说需要使用函数为介质来阻挡 for 循环在同一个 局部变量 内生成同一个内存空间的组件
        global Global_height

        # Add to sign set
        sign_set.add(iter)
        print("iter sign_set:", sign_set)
        sign = list(sign_set)
    
        # Update Global_height
        Global_height += LIST_HEIGHT
        print("global height:", Global_height)

        # Titles
        t = ttk.Label(self.new_frame, text=Tasks_dict[f"Task_{iter}"], font=("", 20))
        t.pack(anchor="w")
        
        # Details
        t2 = ttk.Label(self.new_frame, text=details[f"Detail_{iter}"])
        t2.pack(anchor="w"); 


        # Finished Button
        b = ttk.Button(self.new_frame, text=f"Finished{sign}", command=lambda: self.Finished(t, t2, b, sign_set))
        b.pack(anchor="e")

        print("// iter tasks local counter:", iter)
        

        return 
        



    



if __name__ == "__main__":
    UI()