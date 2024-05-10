from tkinter import ttk
from tkinter import *
import json


# !variables
# <_CONST> : Local constant
# <CONST> : Class global constant
# <GlobalVariable> : Class global variable
# <local_variable> : Local variable

# !functions
# <GlobalFunction> : Global functions
# <StaticMethod> : Static class methods
# <Method> : Class methods


### Main UI
class UI:
    ## Main Global Variables

    # Main Global
    TASKS_HEIGH = 30
    TASKS_ITEMS = 3
    LIST_HEIGHT = TASKS_HEIGH * TASKS_ITEMS
    MAINFRAME_WIDGETS_HEIGHT = 54
    UPCONERHEIGHT = 19
    DRAWCOORDINATE = (0, 0)

    # Main TEXT Dictionary for Labels
    TasksDict = {}
    DetailsDict = {}

    # Main Counter
    Counter = 0
    
    # TEST
    SignSet = set()

    # TEST
    LabelDict_Tasks = {}
    LabelDict_Details = {}
    ButtonDict = {}

    # Window Status
    Status = [False, False]

    # Temperory Data for Saving Purpuse
    TempInfo = []

    # Tasks' Global Height for Determining ScrollRegion
    GlobalHeight = 1

    ## Main Scripts
    def __init__(self):
        # Main Root
        self.root = Tk()
        self.mainframe = Frame(self.root)
        self.mainframe.pack(expand=True, fill="both")
        self.root.title("ToDoList")
        self.root.geometry("400x500")
        self.root.iconbitmap(r"data\aw.ico")


        # Fields
        self.field = ttk.Entry(self.mainframe, width=40)
        self.field.pack(anchor="center")

        # Buttons
        self.button = ttk.Button(self.mainframe, text="Done", command=self.Scripts)
        self.button.pack(anchor="center")

        # Canvas
        self.canvas = Canvas(self.mainframe, scrollregion=(0,0,self.mainframe.winfo_width(), self.GlobalHeight))
        self.canvas.pack(side="left", fill="both", expand=True)
        
        # NewFrame
        self.ImportJSON()
        self.new_frame = Frame(self.canvas)
        self.AddTasks()
        print("Load_Counter:", self.Counter)
        self.canvas.create_window(
                self.DRAWCOORDINATE, 
                window=self.new_frame, 
                anchor="nw", 
                width=self.root.winfo_width() - self.UPCONERHEIGHT, 
                height=self.GlobalHeight
            )
        

        # Slider 
        self.slider = ttk.Scrollbar(self.canvas, orient="vertical", command=self.canvas.yview)
        self.slider.pack(side="right", fill="y")

        # Configs 
        self.canvas.configure(yscrollcommand=self.slider.set)

        # bar 
        self.canvas.bind_all("<MouseWheel>", lambda event: self.canvas.yview_scroll(-int(event.delta / 60), "units"))

        # resize the frame 
        self.mainframe.bind("<Configure>", lambda event: self.Resize(event))

        # Main Loop
        self.mainloop = mainloop()

        return
    
    ## 'Done' button's script (High degree of code coupling, bad code!)
    def Scripts(self):

        # Add tasks from the user input
        self.TasksDict[f"Task_{self.Counter}"] = self.field.get() 
        
        # Scripts
        self.Resize(event=None)
        self.Details()

        print(self.DetailsDict, self.TasksDict)

        return

    ## Ok button
    def OkButton(self, window, detail_field):

        # add task height
        self.GlobalHeight += self.LIST_HEIGHT
        print("global height:", self.GlobalHeight)

        # resizing
        self.Resize(event=None)

        # load Details
        self.DetailsDict[f"Detail_{self.Counter}"] = detail_field.get()

        # save as json
        self.ExportJson()

        print(self.DetailsDict, self.TasksDict)


        ## Add Tasks

        # Main Title
        
        self.SignSet.add(self.Counter)
        print(" ok button SignSet:", self.SignSet) # ///////////////////////////// Working on ///////////////////////////////
        

        self.LabelDict_Tasks[self.Counter] = ttk.Label(self.new_frame, text=self.TasksDict[f"Task_{self.Counter}"], font=("", 20))
        self.LabelDict_Tasks[self.Counter].pack(anchor="w")

        # Details Text
        
        self.LabelDict_Details[self.Counter] = ttk.Label(self.new_frame, text=self.DetailsDict[f"Detail_{self.Counter}"])
        self.LabelDict_Details[self.Counter].pack(anchor="w")


        # Finished Button
        self.ButtonDict[self.Counter] = ttk.Button(self.new_frame, text=f"Finished{self.Counter}", command=lambda: self.Finished(self.Counter - 1))
        self.ButtonDict[self.Counter].pack(anchor="e")

        # global Counter
        self.Counter += 1

        # add to sign set
        # self.SignSet.add(self.Counter)

        print("SignSet:", self.SignSet)
        print("Counter:", self.Counter)

        # destroy edit window
        window.destroy()
        self.Status[0] = False 

        return

    # Finish button's script
    def Finished(self, serial_number):

        # Comfirm Window
        if self.Status[1] == False:

            top = Toplevel()
            top.protocol("WM_DELETE_WINDOW", lambda: self.Close(top, 1))
            top.iconbitmap(r"data\awd.ico")
            t = ttk.Label(top, text="Confirm?", font=20, padding=30, width=20, anchor="center")
            t.pack()
            b1 = ttk.Button(top, text="Yes", command=lambda: self.DestroyScript(top, 1, serial_number))
            b2 = ttk.Button(top, text="No", command=lambda: self.Close(top, 1))
            b1.pack()
            b2.pack()
            self.Status[1] = True

        else:
            print("Opening")
            
        return
        
    # destroy things
    def DestroyScript(self, window, member, serial_number):
    
        # subtract by task height
        self.GlobalHeight -= self.LIST_HEIGHT
        print("global height:", self.GlobalHeight)

        # Scripts
        self.Resize(event=None)
        self.UpdateCanvasHeight()
        self.ImportJSON()
        self.DeleteJSON(serial_number)



        # close the window
        self.Close(window, member)
        
        # destroy lot of things
        self.LabelDict_Tasks[serial_number].destroy()
        self.LabelDict_Details[serial_number].destroy()
        self.ButtonDict[serial_number].destroy()

        return

    # Details window
    def Details(self):

        if (self.Status[0] == False):

            top = Toplevel()
            top.protocol("WM_DELETE_WINDOW", lambda: self.Close(top, 0))
            top.iconbitmap(r"data\awa.ico")
            top.title("Editing Details")
            f = ttk.Entry(top, width=40)
            b = ttk.Button(top, text="Ok", command=lambda: self.OkButton(top, f))
            f.pack()
            b.pack()
            
            self.Status[0] = True

        else:
            print("Opening")
            
            return

    # refreshing the Details for editing ( 0 reference )
    def RefreshDetails(self):
        self.field.destroy()
        new_Details_field = ttk.Label(self.mainframe, text=self.DetailsDict)
        new_Details_field.pack(anchor="w")

        return new_Details_field

    # main resize
    def Resize(self, event):
        _STATIC = 1

        if (event == None): # 静态时

            if (self.GlobalHeight <= self.canvas.winfo_height()): # 窗口大于任务栏长度, 任务栏不可以滑动
                
                self.CreateNewFrame(None)
                self.UpdateCanvasHeight(_STATIC)
                self.canvas.unbind_all("<MouseWheel>")
            
            elif (self.GlobalHeight > self.canvas.winfo_height()): # 窗口小于任务栏长度，任务栏可以滑动
                
                self.CreateNewFrame(None)
                self.UpdateCanvasHeight()
                self.canvas.bind_all("<MouseWheel>", lambda event: self.canvas.yview_scroll(-int(event.delta / 60), "units"))
        
        else: # 活动时

            if (self.GlobalHeight <= self.mainframe.winfo_height() - self.MAINFRAME_WIDGETS_HEIGHT): # 窗口大于任务栏长度，任务栏不可以滑动

                self.CreateNewFrame(event)
                self.UpdateCanvasHeight(_STATIC)
                self.canvas.unbind_all("<MouseWheel>")
                
            elif (self.GlobalHeight > self.mainframe.winfo_height() - self.MAINFRAME_WIDGETS_HEIGHT): # 窗口小于任务栏长度，任务栏可以滑动

                self.CreateNewFrame(event)
                self.UpdateCanvasHeight()
                self.canvas.bind_all("<MouseWheel>", lambda event: self.canvas.yview_scroll(-int(event.delta / 60), "units"))
                
        return

    # basically just drawing a new frame on top of the previous frame on the canvas (!brutal)
    def CreateNewFrame(self, event):

        if (event == None): # 静态时
            print("static")

            index_inactive = self.canvas.create_window(
                self.DRAWCOORDINATE, 
                window=self.new_frame, 
                anchor="nw", 
                width=self.mainframe.winfo_width() - self.UPCONERHEIGHT, 
                height=self.GlobalHeight
            )

            print("INDEX_INACTIVE:", index_inactive)
            del index_inactive

            return
        
        else: # 活动时
            print("dynamic")

            index_active = self.canvas.create_window(
                self.DRAWCOORDINATE, 
                window=self.new_frame, 
                anchor="nw", 
                width=event.width - self.UPCONERHEIGHT, 
                height=self.GlobalHeight
            )

            print("INDEX_ACTIVE:", index_active)
            del index_active

        return

    # update the scrollbar depending on the tasks
    def UpdateCanvasHeight(self, static=0): 

        print("updated canvas height")

        # 重新配置 Canvas 的大小
        self.canvas.update_idletasks()

        # 更新 Canvas 的滚动区域
        if (static):
            
            print("Static State !!!") # Have to disable the scrollbar !!!

        else:

            self.canvas.config(scrollregion=(0, 0, self.canvas.winfo_width(), self.GlobalHeight))

        return

    # closing windows and update Status 
    def Close(self, window=None, member=None):

        if (window == None):

            self.Status[member] = False

        else:

            window.destroy()
            self.Status[member] = False

        return
    
    # Save the file in json format
    def ExportJson(self):

        with (open(r"data\data.json", "w", encoding="UTF-8")) as file:

            json.dump((self.DetailsDict, self.TasksDict), file, ensure_ascii=False, indent=4)

        return

    # Import data.json file
    def ImportJSON(self):

        with (open(r"data\data.json", "rt", encoding="UTF-8")) as file:
            
            try:

                self.data = json.load(file)
                self.DetailsDict = self.data[0]
                self.TasksDict = self.data[1]

            except json.decoder.JSONDecodeError:

                print("NO DATA CURRENTLY!!!")

            return

    # Export data.json file
    def DeleteJSON(self, serial_number): # //////////////////// working on /////////////////////////////

        self.TempInfo = self.data[:]
        Details_dict_local = self.TempInfo[0]
        tasksDict_local = self.TempInfo[1]
        Details_dict_local.pop(f"Detail_{serial_number}")              # //////////////////// working on /////////////////////////////
        tasksDict_local.pop(f"Task_{serial_number}")


        with open(r"data\data.json", "w", encoding="UTF-8") as file:

            json.dump(self.TempInfo, file, ensure_ascii=False, indent=4)
        
        return

    # Add tasks by looping through the data
    def AddTasks(self) -> dict:

        tasks_sign_list = [] # define local tasks SignSet list 定义 局部任务导入标签
        details_sign_list = [] # define local Details list 定义 局部注解(Details)导入标签

        # print Counter
        print("Counter:", self.Counter)
        
        # for looping through keys
        for key in self.TasksDict.keys(): # for 循环 遍历tasks 序号

            tasks_sign_list.append(key)

        for key in self.DetailsDict.keys(): # for 循环 遍历Details 序号

            details_sign_list.append(key)

        # check if tasks_sign_list empty
        if (not tasks_sign_list):
            return
        
        # Set a local Counter to iterate
        local_counter = 0
        
        # Get the Max Count of the Tasks, and we use only <tasks_sign_list>
        max_task = max(tasks_sign_list)
        print("max value:", max_task)

        # Get the actual <n> integer value in the max_task string
        max_tasks_number = int(max_task[5:]) + 1
        print("Max tasks count:", max_tasks_number)

        while (local_counter < len(tasks_sign_list)):
            
            found = False # TEST
            for i in range(max_tasks_number):  # 检查连续的 <max_tasks_number> 个索引

                # <+ 0~max_tasks_number> or <+i> offset
                if (local_counter + i == int(tasks_sign_list[local_counter][5:])):
                    self.IterateTasks(local_counter + i)
                    found = True
                    break

                # <- 0~max_tasks_number> or <-i> offset
                elif (local_counter - i == int(tasks_sign_list[local_counter][5:])):
                    self.IterateTasks(local_counter - i)
                    found = True
                    break

            if (not found):
                print("does not exist!!! // local_counter:", local_counter)

            local_counter += 1

        return
    
    ## Add buttons 添加组件 ；每次调用IterateTasks方法时，其中的局部变量t、t2和b都会在不同的内存空间中创建。
    def IterateTasks(self, index): # 因为不同的组件被创建在不同的内存空间，所以说需要使用函数为介质来阻挡 for 循环在同一个 局部变量 内生成同一个内存空间的组件

        # Add to sign set
        self.SignSet.add(index)
        print("iter SignSet:", self.SignSet)
        

        # Update GlobalHeight
        self.GlobalHeight += self.LIST_HEIGHT
        print("global height:", self.GlobalHeight)


        # Titles
        self.LabelDict_Tasks[index] = ttk.Label(self.new_frame, text=self.TasksDict[f"Task_{index}"], font=("", 20))
        self.LabelDict_Tasks[index].pack(anchor="w")

        
        # Details
        self.LabelDict_Details[index] = ttk.Label(self.new_frame, text=self.DetailsDict[f"Detail_{index}"])
        self.LabelDict_Details[index].pack(anchor="w"); 


        serial_number = index
        print("/// Serial Number:", serial_number)


        # 'Finished' button  # !tricky: the ttk.Button's 'command=' keyword argument will save the passing variable <serial_number> into memory, so it can basically remember the <serial_number>
        self.ButtonDict[index] = ttk.Button(self.new_frame, text=f"Finished{serial_number}", command=lambda: self.Finished(serial_number)) 
        self.ButtonDict[index].pack(anchor="e")

        # Add iteration by 1
        self.Counter += 1   
        
        return
        



    



if __name__ == "__main__":
    UI()