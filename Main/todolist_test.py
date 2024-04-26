from tkinter import ttk
from tkinter import *



Tasks_dict = dict()
counter = 0
d_conuter = 0
Label_list = []
Total_Tasks = ""
status = [False, False]
details = {}
TASKS_HEIGH = 30
TASKS_ITEMS = 3
Global_height = 1
list_height = TASKS_HEIGH * TASKS_ITEMS


### Main UI
class UI:
    def __init__(self):
        # Main Root
        self.root = Tk()
        self.mainframe = Frame(self.root)
        self.root.title("ToDoList")
        self.root.geometry("400x500")
        self.root.protocol("zoomed", self.Get_Status)
        self.mainframe.pack(fill="both", expand=True)
        self.root.iconbitmap("aw.ico")

        # Fields
        self.field = ttk.Entry(self.mainframe, width=40)
        self.field.pack(anchor="center")

        # Buttons
        self.button = ttk.Button(self.mainframe, text="Done", command=self.Scripts)
        self.button.pack(anchor="center")

        # Canvas
        self.canvas = Canvas(self.mainframe, bg="red", width=self.mainframe.winfo_width()+100, height=self.mainframe.winfo_height()+100, scrollregion=(0,0,self.mainframe.winfo_width(), Global_height))
        self.canvas.pack(side="left", fill="both", expand=True)
        
        # NewFrame
        self.new_frame = Frame(self.canvas)

        # Slider 
        self.slider = ttk.Scrollbar(self.mainframe, orient="vertical", command=self.canvas.yview)
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

        self.Details()

        print(details)

        return

    ## Ok button
    def Ok_button(self, window, detail_field):
        global status
        global details
        global d_conuter
        global counter
        global Global_height

        Global_height += list_height
        print("global height:", Global_height)

        self.Resize(event=None)

        details[f"Detail_{d_conuter}"] = detail_field.get()

        ## Add Tasks

        # Main Title
        t = ttk.Label(self.new_frame, text=Tasks_dict[f"Task_{counter}"], font=("", 20))
        t.pack(anchor="w")

        # details Text
        t2 = ttk.Label(self.new_frame, text=details[f"Detail_{d_conuter}"])
        t2.pack(anchor="w")

        # Finished Button
        b = ttk.Button(self.new_frame, text="Finished", command=lambda: self.Finished(t, t2, b))
        b.pack(anchor="e")


        counter += 1
        print("Counter:", counter)
        print(details)


        window.destroy()
        status[0] = False 

        return


    def Finished(self, text, text2, button):
        global status

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
        
        Global_height -= list_height
        print("global height:", Global_height)

        self.Resize(event=None)
        self.update_canvas_height()


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
            d_conuter += 1
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

            if Global_height <= self.canvas.winfo_height(): # 窗口大于任务栏长度
                
                self.Fill_Canvas(event=None)
                self.update_canvas_height()
                # self.adjust_scrollbar()

                self.canvas.unbind_all("<MouseWheel>")

                

                return
            
            elif Global_height > self.canvas.winfo_height(): # 窗口小于任务栏长度，任务栏可以滑动
                

                self.Fill_Canvas(event=None)
                self.update_canvas_height()
                # self.adjust_scrollbar()

                self.canvas.bind_all("<MouseWheel>", lambda event: self.canvas.yview_scroll(-int(event.delta / 60), "units"))

                

                return
        
        else:                                           # 活动时

            if Global_height <= self.mainframe.winfo_height(): # 窗口大于任务栏长度

                # self.Fill_Canvas(event)

                self.update_canvas_height()
                
                self.canvas.unbind_all("<MouseWheel>")
                


            elif Global_height > self.mainframe.winfo_height(): # 窗口小于任务栏长度，任务栏可以滑动

                
                
                print(f"globalheight:{Global_height} is bigger then self.canvas:{self.canvas.winfo_height()} height is ", Global_height > self.canvas.winfo_height())
                print(self.canvas.bindtags())

                # self.Fill_Canvas(event)

                self.update_canvas_height()

                self.canvas.bind_all("<MouseWheel>", lambda event: self.canvas.yview_scroll(-int(event.delta / 60), "units"))

                # print(self.get_fullscreen_status(self.root))
                # if self.get_fullscreen_status(self.root) is not None:
                #     pass
                
        return

    # draw tasks on the canvas
    def Fill_Canvas(self, event):
        if event == None: # 静态时
            self.canvas.create_window(
                (0, 0), 
                window=self.new_frame, 
                anchor="nw", 
                width=self.canvas.winfo_width() - 3, 
                height=Global_height)
            return
        
        else: # 活动时
            self.canvas.create_window(
                    (0, 0), 
                    window=self.new_frame, 
                    anchor="nw", 
                    width=event.width -20, 
                    height=Global_height)

        return

    # update the scrollbar depending on the tasks
    def update_canvas_height(self):   # 修改 Canvas 的高度
        global Global_height

        self.canvas.config(height=Global_height)
        
        # 重新配置 Canvas 的大小
        self.canvas.update_idletasks()

        # 更新 Canvas 的滚动区域
        self.canvas.config(scrollregion=(0, 0, self.canvas.winfo_width(), Global_height))

        return

    # 2rd update (useless)
    def adjust_scrollbar(self):
        global Global_height

        if Global_height <= self.canvas.winfo_height(): # 任务栏长度小于canvas画布长度
            self.slider.set(0, 1)  # 如果内容适合画布，则设置为完整
        else:
            self.slider.set(0, float(self.canvas.winfo_height()) / Global_height)

            return

    #(test)
    def Get_Status(self):
        print("fullscreen")
        
        return


    #(test)
    # def is_fullscreen(self, window):
    #     # 获取窗口的尺寸
    #     window_width = window.winfo_width()
    #     window_height = window.winfo_height()

    #     # 获取屏幕的尺寸
    #     screen_width = window.winfo_screenwidth()
    #     screen_height = window.winfo_screenheight()

    #     # 判断窗口的尺寸是否与屏幕大小相同
    #     return window_width == screen_width and window_height == screen_height

    #(test)
    def get_fullscreen_status(self, window):
        # 获取窗口的属性信息
        attributes = window.attributes()
        attributes_list = list(attributes)

        # 检查 fullscreen 属性是否存在
        if '-fullscreen' in attributes_list:
            print(attributes_list)
            index_number = attributes_list.index('-fullscreen') + 1
            fullscreen_status = attributes_list[index_number]
            return fullscreen_status
        else:
            return None

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
    



if __name__ == "__main__":
    self = UI()