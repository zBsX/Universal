from tkinter import ttk
from tkinter import *

Tasks_dict = dict()
counter = 0
d_counter = 0
Label_list = []
Tasks = []
Total_Tasks = ""
status = [False, False]
details = {}

### Main Scripts 

## 'Done' button
def Scripts(text, mainframe):
    global counter
    global Total_Tasks
    if text.get() == "":
        print("you didnt type any thing!")
        return
    
    s = text.get() # You can add + " \n" to increase padding between Title and Detail
    Tasks_dict[f"Task_{counter}"] = s
    print(s, Tasks_dict)

    Tasks.append(Tasks_dict[f"Task_{counter}"])


    print(details)
    print(len(Tasks))

    ## Add Tasks
    t = ttk.Label(mainframe, text=Tasks[counter], font=10)
    t.pack(anchor="w")

    t2 = ttk.Label(mainframe, text="details")
    t2.pack(anchor="w")

    b = ttk.Button(mainframe, text="Finished", command=lambda: Finished(b, b2, text=t, text2=t2))
    b.pack(anchor="e")

    b2 = ttk.Button(mainframe, text="Details", command=lambda: Details())
    b2.pack(anchor="e")


    counter += 1

    return

def Clear(field):
    field.delete(0, END)

    return

def Finished(*button, text=None, text2=None):
    global status
    
    if len(button) == 2:
        button1, button2 = button
    else:
        return

    if status[1] == False:
        top = Toplevel()
        top.iconbitmap("awd.ico")
        t = ttk.Label(top, text="Confirm?", font=20, padding=30, width=20, anchor="center")
        t.pack()
        b1 = ttk.Button(top, text="Yes", command=lambda: Finished_Script(button1, button2, text=text, text2=text2, window=top, member=1))
        b2 = ttk.Button(top, text="No", command=lambda: Close(top, 1))
        b1.pack()
        b2.pack()
        status[1] = True
    else:
        print("Opening")
        
        return
    
def Finished_Script(*button, text=None, text2=None, window, member):
    # destroy things
    Close(window, member)
    for b in button:
        b.destroy()
    if text == None or text2 == None:
        return
    else:
        text.destroy()
        text2.destroy()

    return

#### fix the ok button wrong opening state
def Details():
    global status
    global d_counter

    d_counter += 1
    

    if status[0] == False:
        top = Toplevel()
        f = ttk.Entry(top, width=40)
        f.pack()
        b = ttk.Button(top, text="Ok", command=lambda: Ok_button(top, 0, f))
        b.pack()
        status[0] = True
    else:
        print("Opening")
        
        return
    
def Refresh_Details(mainframe, field):
    field.destroy()
    new_details_field = ttk.Label(mainframe, text=details)
    new_details_field.pack(anchor="w")

    return new_details_field

def Ok_button(window, member, field):
    global status
    global details

    details[f"Task_{d_counter}"] = field.get()
    print(details)
    window.destroy()
    status[member] = False

    return


def Close(window, member):
    global status
    window.destroy()
    status[member] = False

    return
