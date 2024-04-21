from tkinter import ttk
from tkinter import *
from printinfo import *


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


### Main Scripts 

## 'Done' button
def Scripts(text, new_frame, canvas, mainframe, slider):
    global counter
    global Total_Tasks
    
    Tasks_dict[f"Task_{counter}"] = text.get() # You can add + " \n" to increase padding between Title and Detail
    print(Tasks_dict)

    Details(new_frame, canvas, mainframe, slider)


    print(details)

    return

## Ok button
def Ok_button(window, field, new_frame, canvas, mainframe, slider):
    global status
    global details
    global d_conuter
    global counter
    global Global_height

    
    
    Global_height += list_height
    print("global height:", Global_height)

    Resize(canvas, new_frame, mainframe, slider=slider, event=None)
    # update_canvas_height(canvas, Global_height))
    # adjust_scrollbar(canvas, slider, Global_height)
    # canvas.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))


    details[f"Detail_{d_conuter}"] = field.get()

    ## Add Tasks

    # Main Title
    t = ttk.Label(new_frame, text=Tasks_dict[f"Task_{counter}"], font=("", 20))
    t.pack(anchor="w")

    # details Text
    t2 = ttk.Label(new_frame, text=details[f"Detail_{d_conuter}"])
    t2.pack(anchor="w")

    # Finished Button
    b = ttk.Button(new_frame, text="Finished", command=lambda: Finished(slider, b, text=t, text2=t2, canvas=canvas, new_frame=new_frame, mainframe=mainframe))
    b.pack(anchor="e")


    counter += 1
    print("Counter:", counter)

    print(details)

    window.destroy()
    status[0] = False 

    return


def Finished(slider, *button, text=None, text2=None, canvas=None, new_frame=None, mainframe=None):
    global status


    # Comfirm Window
    if status[1] == False:
        top = Toplevel()
        top.protocol("WM_DELETE_WINDOW", lambda: Close(top, 1))
        top.iconbitmap("awd.ico")
        t = ttk.Label(top, text="Confirm?", font=20, padding=30, width=20, anchor="center")
        t.pack()
        b1 = ttk.Button(top, text="Yes", command=lambda: Destroy_Script(slider, mainframe, canvas, new_frame, top, 1, text, text2, button))
        b2 = ttk.Button(top, text="No", command=lambda: Close(top, 1))
        b1.pack()
        b2.pack()
        status[1] = True
    else:
        print("Opening")
        print("status:", status)
        
        return
    
## details button
def Details(new_frame, canvas, mainframe, slider):
    global status
    global d_conuter

    if status[0] == False:
        top = Toplevel()
        top.protocol("WM_DELETE_WINDOW", lambda: Close(top, 0))
        top.iconbitmap("awa.ico")
        top.title("Editing details")
        f = ttk.Entry(top, width=40)
        f.pack()
        b = ttk.Button(top, text="Ok", command=lambda: Ok_button(top, f, new_frame, canvas, mainframe, slider))
        b.pack()
        d_conuter += 1
        status[0] = True
    else:
        print("Opening")
        
        return


def Destroy_Script(slider, mainframe, canvas, new_frame, window, member, text=None, text2=None, *button):
    global Global_height
    
    Global_height -= list_height
    print("global height:", Global_height)

    Resize(canvas, new_frame, mainframe, slider=slider, event=None)
    update_canvas_height(canvas, Global_height)

    


    # destroy things
    Close(window, member)
    
    

    for i in range(len(button)):
        button[0][i - 1].destroy()
        
    if text == None or text2 == None:
        return
    else:
        text.destroy()
        text2.destroy()

    return


def Refresh_Details(mainframe, field):
    field.destroy()
    new_details_field = ttk.Label(mainframe, text=details)
    new_details_field.pack(anchor="w")

    return new_details_field


def Resize(canvas, new_frame, mainframe, event, slider):
    global Global_height

    canvas.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all"))) 
    adjust_scrollbar(canvas, slider, Global_height)
    print("mainframe width:", mainframe.winfo_width())
    

    if event == None:

        if Global_height <= canvas.winfo_height(): # 窗口大于任务栏长度
            
            Fill_Canvas(canvas, new_frame, event=None)
            update_canvas_height(canvas, Global_height)
            adjust_scrollbar(canvas, slider, Global_height)

            canvas.unbind_all("<MouseWheel>")

            # printinfo_lesser(Global_height, canvas, new_frame)

            return
        
        elif Global_height > canvas.winfo_height(): # 窗口小于任务栏长度，任务栏可以滑动

            Fill_Canvas(canvas, new_frame, event=None)
            update_canvas_height(canvas, Global_height)
            adjust_scrollbar(canvas, slider, Global_height)

            canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(-int(event.delta / 60), "units"))

            # printinfo_bigger(Global_height, canvas)

            return
    
    else:

        if Global_height <= canvas.winfo_height(): # 窗口大于任务栏长度

            Fill_Canvas(canvas, new_frame, event)
            update_canvas_height(canvas, Global_height)

            canvas.unbind_all("<MouseWheel>")
            
            # printinfo_lesser(Global_height, canvas, new_frame)


        elif Global_height > canvas.winfo_height(): # 窗口小于任务栏长度，任务栏可以滑动

            Fill_Canvas(canvas, new_frame, event)
            update_canvas_height(canvas, Global_height)

            canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(-int(event.delta / 60), "units"))

            # printinfo_bigger(Global_height, canvas)

    return


def Fill_Canvas(canvas, new_frame, event):
    if event == None: # 非活动时
        canvas.create_window(
            (0, 0), 
            window=new_frame, 
            anchor="nw", 
            width=canvas.winfo_width() - 3, 
            height=Global_height)
        return
    
    else: # 活动时
        canvas.create_window(
                (0, 0), 
                window=new_frame, 
                anchor="nw", 
                width=event.width - 20, 
                height=Global_height)

    return


def update_canvas_height(canvas, new_height):   # 修改 Canvas 的高度
    canvas.config(height=new_height)
    
    
    # 重新配置 Canvas 的大小
    canvas.update_idletasks()
    # canvas.update()

    
    # 更新 Canvas 的滚动区域
    canvas.config(scrollregion=(0, 0, canvas.winfo_width(), Global_height))


    # 更新滚动条
    canvas.yview_moveto(0)


def adjust_scrollbar(canvas, scrollbar, new_height):
    if new_height <= canvas.winfo_height():
        scrollbar.set(0, 1)  # 如果内容适合画布，则设置为完整
    else:
        scrollbar.set(0, float(canvas.winfo_height()) / new_height)


def Close(window=None, member=None):
    global status

    if window == None:
        status[member] = False

    else:

        window.destroy()
        status[member] = False

    return


def Clear(field):
    field.delete(0, END)

    return